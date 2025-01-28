import torch
import numpy as np
import logging
from typing import Tuple, Optional, Union, Dict, Any
from PIL import Image

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DeepSeekImageGeneration:
    """Enhanced Image Generation Node for DeepSeek Janus Pro"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model": ("DEEPSEEK_MODEL",),
                "tokenizer": ("DEEPSEEK_TOKENIZER",),
                "prompt": ("STRING", {
                    "multiline": True,
                    "default": "A beautiful photorealistic scene"
                }),
                "batch_size": ("INT", {
                    "default": 1,
                    "min": 1,
                    "max": 16
                }),
                "temperature": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.1,
                    "max": 2.0,
                    "step": 0.1
                }),
                "guidance_scale": ("FLOAT", {
                    "default": 7.5,
                    "min": 1.0,
                    "max": 20.0,
                    "step": 0.5
                }),
                "max_length": ("INT", {
                    "default": 77,
                    "min": 1,
                    "max": 256
                }),
                "image_size": ("INT", {
                    "default": 384,
                    "min": 256,
                    "max": 1024,
                    "step": 64
                })
            },
            "optional": {
                "negative_prompt": ("STRING", {
                    "multiline": True,
                    "default": ""
                })
            }
        }
    
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("images",)
    FUNCTION = "generate_images"
    CATEGORY = "DeepSeek_Toolkit/DeepSeek_Multimodal"

    def generate_images(self,
                        model,
                        tokenizer,
                        prompt: str,
                        batch_size: int = 1,
                        temperature: float = 1.0,
                        guidance_scale: float = 7.5,
                        max_length: int = 77,
                        image_size: int = 384,
                        negative_prompt: Optional[str] = None) -> Tuple[torch.Tensor]:
        """
        Advanced image generation using DeepSeek's multi-modal model
        
        Args:
            model: DeepSeek vision-language model
            processor: Model's processor
            prompt: Primary text prompt for image generation
            batch_size: Number of images to generate
            temperature: Sampling temperature
            guidance_scale: Classifier-free guidance scale
            max_length: Maximum sequence length
            image_size: Output image size
            negative_prompt: Optional negative prompt to guide generation
            
        Returns:
            Generated images as tensor
        """
        try:
            # Input validation
            if not prompt or not isinstance(prompt, str):
                raise ValueError("Invalid prompt: Must be a non-empty string")
            
            # Prepare conversation context
            conversation = [
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": ""}
            ]

            # Optional negative prompt handling
            if negative_prompt:
                conversation.insert(0, {"role": "user", "content": negative_prompt})

            # Prepare inputs
            inputs = processor(
                conversations=conversation,
                return_tensors="pt",
                truncation=True,
                max_length=max_length,
                padding=True
            ).to(model.device)

            # Prepare batch inputs for Classifier-Free Guidance
            batch_inputs = {
                k: torch.cat([v] * 2 * batch_size) 
                for k, v in inputs.items()
            }

            # Generate images
            with torch.no_grad():
                outputs = model.generate(
                    **batch_inputs,
                    do_sample=True,
                    temperature=temperature,
                    guidance_scale=guidance_scale,
                    num_beams=batch_size * 2,
                    max_length=max_length + 20,
                    pad_token_id=processor.tokenizer.pad_token_id,
                    eos_token_id=processor.tokenizer.eos_token_id,
                )

            # Decode and process images
            images = model.decode_images(outputs)
            images = images.cpu().numpy()
            
            # Ensure RGB format
            if images.shape[1] != 3:
                images = np.repeat(images, 3, axis=1)
            
            # Normalize and clip
            images = (images + 1) / 2
            images = np.clip(images, 0, 1)
            
            # Transpose to [B,H,W,C]
            images = np.transpose(images, (0, 2, 3, 1))
            
            # Convert to tensor
            images = torch.from_numpy(images).float()
            
            logger.info(f"Generated {batch_size} images with size {images.shape}")
            
            return (images,)

        except Exception as e:
            logger.error(f"Image generation error: {e}", exc_info=True)
            # Return a black image as error indicator
            error_image = torch.zeros((1, image_size, image_size, 3))
            return (error_image,)

# Node class and display name mappings
NODE_CLASS_MAPPINGS = {
    "DeepSeekImageGeneration": DeepSeekImageGeneration
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DeepSeekImageGeneration": "DeepSeek Image Generation Pro"
}