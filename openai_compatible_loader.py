import comfy
import folder_paths
import nodes
import aiohttp
import json
import asyncio
from aiohttp import ClientSession, ClientError
from typing import Optional, List, Dict


class OpenAICompatibleLoader:
    """
    Custom node for OpenAI compatible API integration
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "base_url": ("STRING", {"default": "https://api.openai.com"}),
                "api_key": ("STRING", {"default": ""}),
                "prompt": ("STRING", {"multiline": True}),
                "temperature": ("FLOAT", {"default": 0.7, "min": 0.0, "max": 2.0}),
                "max_tokens": ("INT", {"default": 512, "min": 1, "max": 4096}),
                "model": ("STRING", {
                    "default": "",
                    "label": "模型名称",
                    "allow_edit": True
                }),
            },
            "optional": {
                "context": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("response",)
    FUNCTION = "generate"
    CATEGORY = "DeepSeek_Toolkit"

    async def async_generate(self, payload: dict, base_url: str, api_key: str):
        try:
            async with ClientSession() as session:
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
    
    def generate(self, base_url: str, api_key: str, prompt: str,
                 model: str, temperature: float,
                 max_tokens: int, context: Optional[str] = None):
        
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
        
        # 模型选择逻辑
        selected_model = model if model else "default-model"
        print(f"[INFO] 使用模型: {selected_model}")
        
        payload = {
            "model": selected_model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        
        try:
            return asyncio.run(self.async_generate(payload, base_url, api_key))
        except Exception as e:
            raise Exception(f"请求失败: {str(e)}")

# 注册节点
NODE_CLASS_MAPPINGS = {"OpenAICompatibleLoader": OpenAICompatibleLoader}
NODE_DISPLAY_NAME_MAPPINGS = {"OpenAI Compatible Loader": "OpenAI Compatible Loader"}

WEB_DIRECTORY = "./web"
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']