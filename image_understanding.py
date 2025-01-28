import torch
import numpy as np
from PIL import Image

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

    def understand_image(self, model, processor, image, question):
        """
        Analyze an image using DeepSeek's multi-modal model
        
        Args:
            model: DeepSeek vision-language model
            processor: Model's image processor
            image: Input torch tensor image
            question: User's query about the image
        
        Returns:
            Textual analysis of the image
        """
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

        try:
            # 准备模型输入
            model_inputs = processor(
                conversations=conversation, 
                images=[pil_image], 
                return_tensors='pt'
            ).to(model.device)

            # 生成响应
            outputs = model.generate(
                **model_inputs,
                max_new_tokens=512,
                do_sample=False
            )

            # 解码响应
            answer = processor.decode(outputs[0], skip_special_tokens=True)
            
            return (answer,)

        except Exception as e:
            print(f"Error in image understanding: {e}")
            return ("An error occurred during image analysis.",)

# 节点类映射
NODE_CLASS_MAPPINGS = {
    "DeepSeekImageUnderstanding": DeepSeekImageUnderstanding
}

# 节点显示名称映射
NODE_DISPLAY_NAME_MAPPINGS = {
    "DeepSeekImageUnderstanding": "DeepSeek Image Understanding"
}