import comfy
import folder_paths
import nodes
import aiohttp
import json
from aiohttp import ClientSession, ClientError
from typing import Optional

class OpenAICompatibleLoader:
    """
    Custom node for OpenAI compatible API integration
    """
    def __init__(self):
        self.client = None

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "auto_detect": ("BOOLEAN", {"default": True, "label": "自动检测模型"}),
                "model": ("STRING", {"default": "", "label": "手动指定模型(当自动检测失败时)"}),
                "base_url": ("STRING", {"default": "https://api.openai.com"}),
                "api_key": ("STRING", {"default": ""}),
                "prompt": ("STRING", {"multiline": True}),
                "temperature": ("FLOAT", {"default": 0.7, "min": 0.0, "max": 2.0}),
                "max_tokens": ("INT", {"default": 512, "min": 1, "max": 4096}),
            },
            "optional": {
                "context": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("response",)
    FUNCTION = "generate"
    CATEGORY = "DeepSeek_Toolkit"

    async def fetch_models(self, session: ClientSession, base_url: str, api_key: str):
        try:
            async with session.get(
                f"{base_url}/models",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {api_key}"
                }
            ) as response:
                response.raise_for_status()
                data = await response.json()
                return [model['id'] for model in data.get('data', [])]
        except ClientError as e:
            raise Exception(f"Failed to fetch models: {str(e)}")

    async def async_generate(self, session: ClientSession, payload: dict, base_url: str, api_key: str):
        try:
            async with session.post(
                f"{base_url}/chat/completions",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {api_key}"
                },
                json=payload
            ) as response:
                response.raise_for_status()
                data = await response.json()
                return data['choices'][0]['message']['content']
        except ClientError as e:
            raise Exception(f"API request failed: {str(e)}")

    def generate(self, base_url: str, api_key: str, prompt: str, model: str,
                temperature: float, max_tokens: int, context: Optional[str] = None):
        # 模型检测逻辑
        async def detect_model():
            models = await self.fetch_models(session, base_url, api_key)
            if not models:
                raise ValueError("无法从API获取模型列表")
            return models
        
        # 构建消息体
        messages = []
        if context:
            messages.append({
                "role": "system",
                "content": context
            })
        messages.append({
            "role": "user",
            "content": prompt
        })
        
        # 确定最终使用的模型
        available_models = []
        selected_model = model
        async def run_model_detection():
            if auto_detect:
                try:
                    models = await self.fetch_models(session, base_url, api_key)
                    if not models:
                        raise ValueError("无法从API获取模型列表")
                    return models
                except Exception as e:
                    if not model:
                        raise ValueError(f"自动检测模型失败且未提供手动模型: {str(e)}")
            return []
        
        # 模型检测逻辑
        available_models = await run_model_detection()
                if model and model not in available_models:
                    print(f"警告: 手动指定的模型 '{model}' 不在可用模型列表中")
                elif not model:
                    selected_model = available_models[0] if available_models else ""
            except Exception as e:
                if not model:
                    raise ValueError(f"自动检测模型失败且未提供手动模型: {str(e)}")
        
        if not selected_model:
            raise ValueError("无法确定使用的模型，请检查base url或手动指定有效模型")
        
        payload = {
            "model": selected_model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }

        try:
            # 使用异步请求（需要ComfyUI运行在支持async的环境中）
            async def run_async():
                async with ClientSession() as session:
                    models = await self.fetch_models(session, base_url, api_key)
                    if model not in models:
                        raise ValueError(f"Model '{model}' not found in available models.")
                    return await self.async_generate(session, payload, base_url, api_key)

            import asyncio
            response = asyncio.run(run_async())
            
            return (response,)
        
        except Exception as e:
            # Fallback to synchronous request
            try:
                import requests
                response = requests.post(
                    f"{base_url}/v1/chat/completions",
                    headers={
                        "Content-Type": "application/json",
                        "Authorization": f"Bearer {api_key}"
                    },
                    json=payload
                )
                response.raise_for_status()
                data = response.json()
                return (data['choices'][0]['message']['content'],)
            except Exception as sync_e:
                raise Exception(f"All request attempts failed:\nAsync: {str(e)}\nSync: {str(sync_e)}")

# 注册节点
NODE_CLASS_MAPPINGS = {"OpenAICompatibleLoader": OpenAICompatibleLoader}
NODE_DISPLAY_NAME_MAPPINGS = {"OpenAICompatibleLoader": "OpenAI Compatible Loader"}

WEB_DIRECTORY = "./web"
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']