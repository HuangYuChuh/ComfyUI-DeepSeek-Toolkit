import os
import torch
import folder_paths
from typing import Tuple
from transformers import AutoModelForCausalLM, AutoProcessor  # 添加正确导入
from janus.models import MultiModalityCausalLM, VLChatProcessor  # type: ignore

class DeepSeekModelLoader:
    """Model loader node for DeepSeek Janus Pro"""
    
    def __init__(self):
        self.local_model_path = None
    
    @staticmethod
    def get_available_models():
        """Scan models/deepseek_janus directory and return subfolder names"""
        import os
        models_path = folder_paths.models_dir
        deepseek_janus_path = os.path.join(models_path, "deepseek_janus")
        if not os.path.exists(deepseek_janus_path):
            raise ValueError(
                f"目录未找到: {deepseek_janus_path}. "
                "请确保模型放置在正确的位置。"
            )
        # 获取所有子文件夹名称
        model_names = [
            name for name in os.listdir(deepseek_janus_path)
            if os.path.isdir(os.path.join(deepseek_janus_path, name))
        ]
        if not model_names:
            raise ValueError(
                f"{deepseek_janus_path} 中未找到模型. "
                "请下载并将模型放置在正确的位置。"
            )
        return model_names
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model_name": (cls.get_available_models(),),
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
                model_dir = os.path.join(models_path, "deepseek_janus", model_name)
                
                if not os.path.exists(model_dir):
                    raise ValueError(
                        f"本地模型未在 {model_dir} 找到. "
                        "请下载模型并将其放置在 ComfyUI/models/deepseek_janus 文件夹中。"
                    )
                model_path = model_dir
            else:
                model_path = model_name

            print(f"从 {model_path} 加载 DeepSeek Janus 模型")
            
            # 加载处理器和模型
            try:
                processor = VLChatProcessor.from_pretrained(
                    str(model_path),
                    trust_remote_code=True,
                    use_fast=False
                )
            except Exception as e:
                raise ValueError(
                    f"无法从 {model_path} 加载处理器. 请确保已下载正确的模型文件并将其放置在 models/deepseek_janus 文件夹中. 错误：{str(e)}"
                )

            try:
                model = AutoModelForCausalLM.from_pretrained(
                    model_path,
                    trust_remote_code=True,
                    torch_dtype=dtype,
                    device_map="auto"
                )
            except Exception as e:
                raise ValueError(
                    f"无法从 {model_path} 加载模型. 请确保已下载正确的模型文件并将其放置在 models/deepseek_janus 文件夹中. 错误：{str(e)}"
                )
            
            # 将模型移动到正确的设备和数据类型
            model = model.to(dtype).to(device).eval()
            
            print("DeepSeek Janus 模型加载成功")
            return (model, processor)

        except Exception as e:
            print(f"加载模型时出错: {str(e)}")
            raise

# 节点类映射
NODE_CLASS_MAPPINGS = {
    "DeepSeekModelLoader": DeepSeekModelLoader
}

# 节点显示名称映射
NODE_DISPLAY_NAME_MAPPINGS = {
    "DeepSeekModelLoader": "Multimodal Loader"
}