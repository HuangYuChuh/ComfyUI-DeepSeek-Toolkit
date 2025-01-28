import os
import torch
import folder_paths
from typing import Tuple

class DeepSeekModelLoader:
    """Model loader node for DeepSeek Janus Pro"""
    
    def __init__(self):
        self.local_model_path = None
        
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model_name": (["janus-pro-7b"],),
                "use_local": ([True, False], {
                    "default": True
                }),
            },
        }
    
    RETURN_TYPES = ("DEEPSEEK_MODEL", "DEEPSEEK_TOKENIZER")
    RETURN_NAMES = ("model", "tokenizer")
    FUNCTION = "load_model"
    CATEGORY = "DeepSeek_Toolkit/Loader"

    def load_model(self, model_name: str, use_local: bool) -> Tuple:
        """Load DeepSeek Janus Pro model and processor"""
        try:
            from transformers import AutoProcessor, AutoModelForVision2Seq
        except ImportError:
            raise ImportError("Please install required packages using 'pip install -r requirements.txt'")

        # 设置设备和数据类型
        device = "cuda" if torch.cuda.is_available() else "cpu"
        try:
            dtype = torch.bfloat16
            torch.zeros(1, dtype=dtype, device=device)
        except RuntimeError:
            dtype = torch.float16

        try:
            if use_local:
                # 获取ComfyUI根目录
                models_path = folder_paths.models_dir
                # 构建模型路径
                model_dir = os.path.join(
                    models_path,
                    "ComfyUI/models/deepseek_janus",
                    os.path.basename(model_name)
                )
                
                if not os.path.exists(model_dir):
                    raise ValueError(
                        f"Local model not found at {model_dir}. "
                        "Please download the model and place it in the ComfyUI/models/deepseek_janus folder."
                    )
                model_path = model_dir
            else:
                model_path = model_name

            print(f"Loading DeepSeek Janus model from {model_path}")
            
            # 加载处理器和模型
            processor = AutoProcessor.from_pretrained(model_path)
            model = AutoModelForVision2Seq.from_pretrained(
                model_path,
                trust_remote_code=True,
                torch_dtype=dtype,
                device_map="auto"
            )
            
            # 将模型移到正确的设备和数据类型
            model = model.to(dtype).to(device).eval()
            
            print("DeepSeek Janus model loaded successfully")
            return (model, processor)

        except Exception as e:
            print(f"Error loading model: {str(e)}")
            raise

# 节点类映射
NODE_CLASS_MAPPINGS = {
    "DeepSeekModelLoader": DeepSeekModelLoader
}

# 节点显示名称映射
NODE_DISPLAY_NAME_MAPPINGS = {
    "DeepSeekModelLoader": "Multimodal Loader"
}