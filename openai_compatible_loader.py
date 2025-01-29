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
                "model": ("STRING", {"default": "gpt-3.5-turbo"}),
                "api_base": ("STRING", {"default": "https://api.openai.com"}),
                "api_key": ("PASSWORD", {"default": ""}),
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

    async def async_generate(self, session: ClientSession, payload: dict, api_base: str, api_key: str):
        try:
            async with session.post(
                f"{api_base}/chat/completions",
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

    def generate(self, api_base: str, api_key: str, prompt: str, model: str,
                temperature: float, max_tokens: int, context: Optional[str] = None):
        messages = [{
            "role": "user",
            "content": prompt
        }]
        
        if context:
            messages.insert(0, {
                "role": "system",
                "content": context
            })

        payload = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }

        try:
            # 使用异步请求（需要ComfyUI运行在支持async的环境中）
            async def run_async():
                async with ClientSession() as session:
                    return await self.async_generate(session, payload, api_base, api_key)

            import asyncio
            response = asyncio.run(run_async())
            
            return (response,)
        
        except Exception as e:
            # Fallback to synchronous request
            try:
                import requests
                response = requests.post(
                    f"{api_base}/v1/chat/completions",
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