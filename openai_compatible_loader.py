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
                "model": ("STRING", {
                    "default": "",
                    "label": "模型名称",
                    "allow_edit": True
                }),
                "api_key": ("STRING", {"default": ""}),
                "system_prompt": ("STRING", {"default": "我是一个可以使用LLM构建实用功能的Toolkit", "multiline": True}),
                "prompt": ("STRING", {"multiline": True}),
                "temperature": ("FLOAT", {"default": 0.7, "min": 0.0, "max": 2.0}),
                "max_tokens": ("INT", {"default": 512, "min": 1, "max": 4096}),
                "image": ("IMAGE", {"label": "输入图像"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "generate"
    CATEGORY = "DeepSeek_Toolkit"

    async def async_generate(self, payload: dict, actual_base_url: str, api_key: str):
        try:
            async with ClientSession() as session:
                async with session.post(
                    f"{actual_base_url}/chat/completions",
                    headers={
                        "Content-Type": "application/json",
                        "Authorization": f"Bearer {api_key}"
                    },
                    json=payload
                ) as response:
                    response.raise_for_status()
                    data = await response.json()
                    print(f"[DEBUG] API Response: {data}")  # 调试日志
                    response_content = data['choices'][0]['message']['content']
                    print(f"[DEBUG] Extracted Response Content: {response_content}")  # 调试日志
                    return [response_content]  # 返回值改为列表形式
        except ClientError as e:
            raise Exception(f"API request failed: {str(e)}")
    
    def generate(self, base_url: str, api_key: str, prompt: str,
                 model: str, temperature: float,
                 max_tokens: int, image: Optional[str] = None, system_prompt: Optional[str] = None):
        
        messages = []
        if system_prompt:
            messages.append({
                "role": "system",
                "content": system_prompt
            })
        # 验证图像数据是否为 Base64 编码
        import base64
        try:
            if image is not None and hasattr(image, "numpy"):
                # 检查输入类型并转换为 Base64
                if hasattr(image, "numpy"):  # 检查是否为张量
                    import numpy as np
                    image_np = image.numpy()  # 转换为 NumPy 数组
                    if image_np.size > 1:  # 确保张量不是单值
                        image = image_np.tobytes()  # 转换为字节流
                    else:
                        raise ValueError("图像张量必须包含多值数据")
                elif isinstance(image, bytes):
                    # 上传图像到图床并获取 URL
                    import requests
                    from io import BytesIO

                    # 使用 Imgur API 上传图像
                    imgur_client_id = "YOUR_IMGUR_CLIENT_ID"  # 替换为实际的 Imgur Client ID
                    headers = {"Authorization": f"Client-ID {imgur_client_id}"}
                    response = requests.post(
                        "https://api.imgur.com/3/image",
                        headers=headers,
                        files={"image": BytesIO(image)}
                    )
                    response.raise_for_status()
                    image_url = response.json()["data"]["link"]
                    print(f"[DEBUG] Uploaded Image URL: {image_url}")  # 调试日志
                    image = image_url
                elif isinstance(image, str):
                    # 如果已经是 Base64 字符串，则直接使用
                    pass
                else:
                    raise ValueError("图像数据必须是 Base64 字符串或字节流")
                messages.append({
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image}"}}
                    ]
                })
            else:
                messages.append({
                    "role": "user",
                    "content": prompt
                })
        except Exception as e:
            raise ValueError(f"无效的图像数据: {str(e)}")
        
        # 模型选择逻辑
        selected_model = model if model else "default-model"
        print(f"[INFO] 使用模型: {selected_model}")
        
        # 定义 base_url 映射表
        base_url_mapping = {
            "Qwen/通义千问": "https://dashscope.aliyuncs.com/compatible-mode/v1",
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
        
        payload = {
            "model": selected_model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        print(f"[DEBUG] Generated Payload: {json.dumps(payload, indent=2)}")  # 调试日志
        
        try:
            return asyncio.run(self.async_generate(payload, actual_base_url, api_key))
        except Exception as e:
            raise Exception(f"请求失败: {str(e)}")

# 注册节点
NODE_CLASS_MAPPINGS = {"OpenAICompatibleLoader": OpenAICompatibleLoader}
NODE_DISPLAY_NAME_MAPPINGS = {"OpenAICompatibleLoader": "OpenAI Compatible Loader"}

WEB_DIRECTORY = "./web"
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']