import os
import torch
from typing import Tuple
from transformers import AutoTokenizer
from janus.models import MultiModalityCausalLM, VLChatProcessor  # type: ignore
import folder_paths

class DeepSeekModelLoader:
    """Model loader node for DeepSeek Janus Pro"""

    DEFAULT_MODELS = ["Janus-Pro-1B", "Janus-Pro-7B"]

    def __init__(self):
        self.local_model_path = None

    @staticmethod
    def get_available_models():
        """Scan models/deepseek_janus/Janus-Pro directory and return subfolder names"""
        models_path = folder_paths.models_dir
        deepseek_janus_path = os.path.join(models_path, "deepseek_janus", "Janus-Pro")
        
        if not os.path.exists(deepseek_janus_path):
            print(f"目录未找到: {deepseek_janus_path}")
            return DeepSeekModelLoader.DEFAULT_MODELS

        model_names = [
            name for name in os.listdir(deepseek_janus_path)
            if os.path.isdir(os.path.join(deepseek_janus_path, name))
        ]

        if not model_names:
            # print(f"在 {deepseek_janus_path} 中未找到模型，使用默认列表")
            return DeepSeekModelLoader.DEFAULT_MODELS

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
        device = "cuda" if torch.cuda.is_available() else "cpu"
        try:
            dtype = torch.bfloat16
            torch.zeros(1, dtype=dtype, device=device)
        except RuntimeError:
            dtype = torch.float16

        try:
            if use_local:
                models_path = folder_paths.models_dir
                model_dir = os.path.join(models_path, "deepseek_janus", "Janus-Pro", os.path.basename(model_name))

                if not os.path.exists(model_dir):
                    raise ValueError(
                        f"本地模型未在 {model_dir} 找到。\n\n"
                        "您需要：\n"
                        "1. 创建目录：models/deepseek_janus/Janus-Pro\n"
                        "2. 下载模型文件\n"
                        "3. 将模型文件放入上述目录中\n\n"
                        "如需帮助，请查看项目文档。"
                    )
                model_path = model_dir
            else:
                model_path = model_name

            # 确保 model_path 是字符串
            model_path = str(model_path)

            print(f"从 {model_path} 加载 DeepSeek Janus 模型")

            # 创建临时文件夹用于模型权重
            temp_folder = os.path.join(folder_paths.temp_directory, "janus_model_weights")
            os.makedirs(temp_folder, exist_ok=True)

            # 加载 tokenizer
            tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)

            # 加载处理器
            processor = VLChatProcessor.from_pretrained(
                model_path,
                tokenizer=tokenizer,
                trust_remote_code=True
            )

            # 加载模型
            model = MultiModalityCausalLM.from_pretrained(
                model_path,
                trust_remote_code=True,
                torch_dtype=dtype,
                device_map="auto",
                offload_folder=temp_folder
            )

            model = model.to(dtype).to(device).eval()

            return (model, processor)

        except Exception as e:
            raise ValueError(f"加载模型时出错: {str(e)}")

# 节点类映射
NODE_CLASS_MAPPINGS = {
    "DeepSeekModelLoader": DeepSeekModelLoader
}

# 节点显示名称映射
NODE_DISPLAY_NAME_MAPPINGS = {
    "DeepSeekModelLoader": "Multimodal Loader"
}
