import torch
import numpy as np
from PIL import Image
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DeepSeekImageUnderstanding:
    """Image Understanding Node for DeepSeek Janus"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model": ("DEEPSEEK_MODEL",),
                "tokenizer": ("DEEPSEEK_TOKENIZER",),
                "image": ("IMAGE",),
                "question": ("STRING", {
                    "multiline": True,
                    "default": "Describe this image in detail."
                }),
            },
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "understand_image"
    CATEGORY = "DeepSeek_Toolkit/DeepSeek_Multimodal"

    def understand_image(self, model, tokenizer, image, question):
        """
        Analyze an image using DeepSeek's multi-modal model
        
        Args:
            model: DeepSeek vision-language model
            tokenizer: Model's image processor
            image: Input torch tensor image
            question: User's query about the image
        
        Returns:
            Textual analysis of the image
        """
        try:
            # Log the image parameter
            logger.info(f"Received image tensor with shape: {image.shape}")

            # 图像预处理
            if len(image.shape) == 4:  # BCHW format
                if image.shape[0] == 1:
                    image = image.squeeze(0)  # Remove batch dimension
            
            # Normalize and convert to uint8 numpy
            image = (torch.clamp(image, 0, 1) * 255).cpu().numpy().astype(np.uint8)
            
            # Convert to PIL Image
            pil_image = Image.fromarray(image, mode='RGB')

            # 构建对话上下文
            conversation = [
                {
                    "role": "user",
                    "content": f"<image_placeholder>\n{question}",
                    "images": [pil_image],
                }
            ]

            # 准备模型输入
            model_inputs = tokenizer(
                conversations=conversation, 
                images=[pil_image], 
                return_tensors='pt'
            ).to(model.device)

            try:
                # 首先尝试使用 text_generate
                with torch.no_grad():
                    outputs = model.generate(
                        **model_inputs,
                        max_new_tokens=512,
                        do_sample=False
                    )
            except AttributeError:
                try:
                    # 如果 text_generate 不可用，尝试使用 chat
                    with torch.no_grad():
                        outputs = model.chat(
                            tokenizer,
                            question,
                            history=[],
                            images=[pil_image],
                            max_new_tokens=512,
                            do_sample=False
                        )
                        return (outputs,)
                except AttributeError:
                    # 如果 chat 也不可用，使用标准 generate
                    with torch.no_grad():
                        outputs = model.generate(
                            **model_inputs,
                            max_new_tokens=512,
                            do_sample=False
                        )

            # 解码响应
            answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
            
            return (answer,)

        except Exception as e:
            logger.error(f"Error in image understanding: {e}", exc_info=True)
            return ("An error occurred during image analysis.",)

# 节点类映射
NODE_CLASS_MAPPINGS = {
    "DeepSeekImageUnderstanding": DeepSeekImageUnderstanding
}

# 节点显示名称映射
NODE_DISPLAY_NAME_MAPPINGS = {
    "DeepSeekImageUnderstanding": "DeepSeek Image Understanding"
}