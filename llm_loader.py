import comfy
import folder_paths
import nodes
import aiohttp
import json
import asyncio
from aiohttp import ClientSession, ClientError


class LLM_Loader:
    """
    Custom node for loading LLM models via a base URL and model name
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "base_url": ([
                    "Qwen/通义千问",
                    "DeepSeek",
                    "DouBao",
                    "Spark",
                    "GLM",
                    "Moonshot",
                    "Baichuan",
                    "MiniMax",
                    "StepFun"
                ], {}),
                "model": ("STRING", {
                    "default": "",
                    "label": "模型名称",
                    "allow_edit": True
                }),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("base_url", "model")
    FUNCTION = "generate"
    CATEGORY = "DeepSeek_Toolkit"

    # 定义 base_url 和模型的映射关系
    MODEL_MAPPING = {
        "Qwen/通义千问": ["qwen-turbo", "qwen-plus", "qwen-max"],
        "DeepSeek": ["deepseek-7b", "deepseek-33b"],
        "DouBao": ["doubao-lite", "doubao-pro"],
        "Spark": ["spark-mini", "spark-max"],
        "GLM": ["glm-130b"],
        "Moonshot": ["moonshot-v1"],
        "Baichuan": ["baichuan-7b", "baichuan-13b"],
        "MiniMax": ["minimax-turbo", "minimax-plus"],
        "StepFun": ["stepfun-base", "stepfun-large"]
    }

    async def async_generate(self, payload: dict, base_url: str):
        try:
            async with ClientSession() as session:
                async with session.post(
                    f"{base_url}/chat/completions",
                    headers={
                        "Content-Type": "application/json"
                    },
                    json=payload
                ) as response:
                    response.raise_for_status()
                    data = await response.json()
                    return data['choices'][0]['message']['content']
        except ClientError as e:
            raise Exception(f"API request failed: {str(e)}")
    
    def generate(self, base_url: str, model: str):
        # 构建默认的提示消息
        messages = [
            {
                "role": "user",
                "content": "Hello, how are you?"
            }
        ]
        
        # 定义 base_url 映射表
        base_url_mapping = {
            "Qwen/阿里巴巴": "https://dashscope.aliyuncs.com/compatible-mode/v1",
            "DeepSeek": "https://api.deepseek.com",
            "DouBao": "https://api.doubao.com",
            "Spark": "https://api.spark.com",
            "GLM": "https://api.glm.com",
            "Moonshot": "https://api.moonshot.com",
            "Baichuan": "https://api.baichuan.com",
            "MiniMax": "https://api.minimax.com",
            "StepFun": "https://api.stepfun.com"
        }
        
        # 获取实际的 base_url
        actual_base_url = base_url_mapping.get(base_url, base_url)
        
        # 使用指定的模型
        selected_model = model if model else "default-model"
        print(f"[INFO] 使用模型: {selected_model}")
        
        payload = {
            "model": selected_model,
            "messages": messages
        }
        
        try:
            # 返回 base_url 和 model
            return (actual_base_url, selected_model)
        except Exception as e:
            raise Exception(f"请求失败: {str(e)}")

# 注册节点
NODE_CLASS_MAPPINGS = {"LLM_Loader": LLM_Loader}
NODE_DISPLAY_NAME_MAPPINGS = {"LLM_Loader": "LLM Loader"}

WEB_DIRECTORY = "./web"
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']