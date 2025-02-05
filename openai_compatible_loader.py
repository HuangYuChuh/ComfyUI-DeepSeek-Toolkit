import comfy
import folder_paths
import nodes
import aiohttp
import json
import asyncio
from aiohttp import ClientSession, ClientError
from typing import Optional, List, Dict
import time  # 添加时间模块
import torch


class OpenAICompatibleLoader:
    """
    Custom node for OpenAI compatible API integration
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "base_url": ("STRING", {"default": "Qwen/通义千问"}),
                "model": ("STRING", {
                    "default": "",
                    "label": "模型名称",
                    "allow_edit": True
                }),
                "api_key": ("STRING", {"default": ""}),
                },
            "optional": {
                "image": ("IMAGE", {"default": None}),
                "system_prompt": ("STRING", {"default": "我是一个可以使用LLM构建实用功能的Toolkit", "multiline": True}),
                "prompt": ("STRING", {"multiline": True}),
                "temperature": ("FLOAT", {"default": 0.7, "min": 0.0, "max": 2.0}),
                "max_tokens": ("INT", {"default": 512, "min": 1, "max": 4096}),
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
                 max_tokens: int, system_prompt: Optional[str] = None, image: Optional[str] = None):
        if image is not None:
            # Unified logic for handling both Tensor and string inputs
            if isinstance(image, torch.Tensor):
                import base64
                from PIL import Image
                import io

                # Convert tensor to PIL image
                image = image.squeeze(0).cpu().numpy()  # [H, W, C]
                if image.shape[2] == 1:  # Grayscale image
                    image = image.squeeze(-1)
                image = (image * 255).astype('uint8')
                image = Image.fromarray(image)

                # Convert PIL image to Base64
                buffered = io.BytesIO()
                image.save(buffered, format="PNG")
                img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
                image = f"data:image/png;base64,{img_str}"

            # At this point, `image` is guaranteed to be a Base64 string
            if image is not None:
                content.append({"type": "image_url", "image_url": {"url": image}})
        # Initialize messages list
        messages = []
        if system_prompt:
            messages.append({
                "role": "system",
                "content": system_prompt
            })
        content = []
        print(f"[DEBUG] Image parameter type: {type(image)}, value: {image}")
        if image is not None:
            # Check if image is Tensor and convert to Base64
            if isinstance(image, torch.Tensor):
                import base64
                from PIL import Image
                import io
                
                # Convert tensor to PIL image
                image = image.squeeze(0).cpu().numpy()  # [H, W, C]
                if image.shape[2] == 1:  # Grayscale image
                    image = image.squeeze(-1)
                image = (image * 255).astype('uint8')
                image = Image.fromarray(image)

                # Convert PIL image to Base64
                buffered = io.BytesIO()
                image.save(buffered, format="PNG")
                img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
                image = f"data:image/png;base64,{img_str}"
            
            # Add image to content only if it's not None
            content.append({"type": "image_url", "image_url": {"url": image}})

        if image is not None:
            content.append({"type": "image_url", "image_url": {"url": image}})
        if prompt.strip():
            content.append({"type": "text", "text": prompt})
        
        if content or prompt.strip():
            messages.append({
                "role": "user",
                "content": content
            })
        else:
            raise ValueError("用户输入的 prompt 不能为空")
        
        # 模型选择逻辑
        selected_model = model if model else "glm-4"  # 默认模型为 glm-4
        print(f"[INFO] 使用模型: {selected_model}")
        
        # 定义 base_url 映射表
        base_url_mapping = {
            "Qwen/通义千问": "https://dashscope.aliyuncs.com/compatible-mode/v1",
            "DeepSeek/深度求索": "https://api.deepseek.com/v1/",
            "DouBao/豆包": "https://ark.cn-beijing.volces.com/api/v3/",
            "Spark/星火": "https://spark-api-open.xf-yun.com/v1/",
            "GLM/智谱清言": "https://open.bigmodel.cn/api/paas/v4/",
            "Moonshot/月之暗面": "https://api.moonshot.cn/v1",
            "Baichuan/百川": "https://api.baichuan-ai.com/v1/",
            "MiniMax/MiniMax": "https://api.minimax.chat/v1/",
            "StepFun/阶跃星辰": "https://api.stepfun.com/v1/"
        }
        
        # 获取实际的 base_url
        actual_base_url = base_url_mapping.get(base_url.strip(), base_url)
        
        payload = {
            "model": selected_model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        print(f"[DEBUG] Full Payload Sent to API: {json.dumps(payload, indent=2)}")  # 更详细的调试日志
        
        try:
            # 添加延迟以避免触发速率限制
            time.sleep(1)  # 每次请求前等待 1 秒
            return asyncio.run(self.async_generate(payload, actual_base_url, api_key))
        except Exception as e:
            raise Exception(f"请求失败: {str(e)}")


# 注册节点
NODE_CLASS_MAPPINGS = {"OpenAICompatibleLoader": OpenAICompatibleLoader}
NODE_DISPLAY_NAME_MAPPINGS = {"OpenAICompatibleLoader": "OpenAI Compatible Adapter"}

WEB_DIRECTORY = "./web"
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
