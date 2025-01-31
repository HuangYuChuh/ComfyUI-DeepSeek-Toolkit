import comfy
import folder_paths
import nodes
import aiohttp
import json
import asyncio
from aiohttp import ClientSession, ClientError
from typing import Optional, List, Dict
import re


class OpenAICompatibleLoader:
    """
    Custom node for OpenAI compatible API integration
    """
    available_models = []
    
    @classmethod
    def get_model_choices(cls):
        return cls.available_models or ["无法获取模型列表"]
    
    def __init__(self):
        self.client = None

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "auto_detect": ("BOOLEAN", {"default": True, "label": "自动检测模型"}),
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

    async def fetch_models(self, session: ClientSession, base_url: str, api_key: str, timeout: int = 5) -> List[str]:
        """核心检测方法"""
        self.base_url = base_url.rstrip('/')
        
        # 尝试不同兼容服务的端点
        endpoints_to_try = [
            "/v1/models",          # OpenAI 标准格式
            "/api/tags",           # Ollama 格式
            "/models"              # 其他兼容服务格式
        ]

        for endpoint in endpoints_to_try:
            models = await self._try_fetch_models(session, endpoint, api_key, timeout)
            if models:
                return models

        return []
    
    async def _try_fetch_models(self, session: ClientSession, endpoint: str, api_key: str, timeout: int) -> List[str]:
        """尝试获取指定端点的模型列表"""
        try:
            response = await session.get(
                f"{self.base_url}{endpoint}",
                headers={
                    "Accept": "application/json",
                    "Authorization": f"Bearer {api_key}"
                },
                timeout=aiohttp.ClientTimeout(total=timeout)
            )
            response.raise_for_status()
            
            data = await response.json()
            return self._parse_response(endpoint, data)
            
        except (aiohttp.ClientError, KeyError):
            return []

    def _parse_response(self, endpoint: str, data: Dict) -> List[str]:
        """解析不同服务的响应格式"""
        # 处理 OpenAI 标准格式
        if endpoint == "/v1/models":
            return [model["id"] for model in data.get("data", [])]
        
        # 处理 Ollama 的 /api/tags 格式
        elif endpoint == "/api/tags":
            return [model["name"] for model in data.get("models", [])]
        
        # 处理其他通用格式
        return data.get("models", [])

    def smart_select_model(self, models: List[str]) -> Optional[str]:
        """智能选择默认模型"""
        if not models:
            return None

        # 优先选择规则（可根据需求扩展）
        priority_patterns = [
            r"gpt-4(-?\d+k)?-preview",
            r"gpt-3.5-turbo(-?\d+k)?-preview",
            r"llama2-\d+b-chat",
            r"mistral-7b-instruct"
        ]

        for pattern in priority_patterns:
            for model in models:
                if re.search(pattern, model, re.IGNORECASE):
                    return model

        # 返回第一个可用模型
        return models[0]

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
    
    def generate(self, auto_detect: bool, base_url: str, api_key: str, prompt: str,
                 model: str, temperature: float,
                 max_tokens: int, context: Optional[str] = None):
        
        async def run_model_detection():
            if auto_detect:
                try:
                    async with ClientSession() as session:
                        models = await self.fetch_models(session, base_url, api_key)
                        # 更新可用模型列表
                        OpenAICompatibleLoader.available_models = models or ["无法获取模型列表"]
                        return models
                except Exception as e:
                    print(f"[ERROR] 自动检测失败: {str(e)}")
                    return []
            return []
        
        async def main():
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
            detected_models = await run_model_detection()
            selected_model = None
            
            if auto_detect and detected_models:
                selected_model = self.smart_select_model(detected_models)
                print(f"[INFO] 使用自动检测模型: {selected_model}")
            elif model:
                selected_model = model
                print(f"[INFO] 使用手动指定模型: {selected_model}")
            else:
                selected_model = "default-model"
                print(f"[INFO] 使用默认模型: {selected_model}")
            
            payload = {
                "model": selected_model,
                "messages": messages,
                "temperature": temperature,
                "max_tokens": max_tokens
            }
            
            try:
                return await self.async_generate(payload, base_url, api_key)
            except Exception as e:
                raise Exception(f"请求失败: {str(e)}")
        
        try:
            return asyncio.run(main())
        except Exception as e:
            raise Exception(f"执行失败: {str(e)}")

# 注册节点
NODE_CLASS_MAPPINGS = {"OpenAICompatibleLoader": OpenAICompatibleLoader}
NODE_DISPLAY_NAME_MAPPINGS = {"OpenAI Compatible Loader": "OpenAI Compatible Loader"}

WEB_DIRECTORY = "./web"
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']