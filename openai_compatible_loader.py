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
                try:
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
                except Exception as e:
                    print(f"[ERROR] 请求失败: {str(e)}")  # 打印错误信息
                    raise
        except ClientError as e:
            raise Exception(f"API request failed: {str(e)}")

    def generate(self, base_url: str, api_key: str, prompt: str,
                 model: str, temperature: float,
                 max_tokens: int, system_prompt: Optional[str] = None, image: Optional[str] = None):
        content = []  # ⭐️ 关键修改：将 content 初始化放在函数的最开始

        print(f"[DEBUG] Image parameter type: {type(image)}, value: {image}")

        if image is not None: # ⭐️ 精简 image 处理逻辑，只保留一个 if image is not None 块
            # 统一处理 Tensor 和 字符串类型的 image 输入
            if isinstance(image, torch.Tensor):
                import base64
                from PIL import Image
                import io

                # 将 Tensor 转换为 PIL 图像
                image = image.squeeze(0).cpu().numpy()  # [H, W, C]
                if image.shape[2] == 1:  # 灰度图像
                    image = image.squeeze(-1)
                image = (image * 255).astype('uint8')
                image = Image.fromarray(image)

                # 将 PIL 图像转换为 Base64 编码
                buffered = io.BytesIO()
                image.save(buffered, format="PNG", quality=95)  # 添加质量参数以提高图像清晰度
                img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
                image = f"data:image/png;base64,{img_str}"

            # 如果 image 是字符串类型，验证其是否符合 Base64 格式
            elif isinstance(image, str):
                import re
                if not re.match(r"^data:image\/[a-zA-Z]+;base64,", image):
                    raise ValueError("Invalid Base64 image format")

            # 将 Base64 编码的图像添加到 content 中
            content.append({"type": "image_url", "image_url": {"url": image}})

        if prompt.strip():
            content.append({"type": "text", "text": prompt})

        messages = [] # 初始化 messages 列表
        if system_prompt:
            messages.append({
                "role": "system",
                "content": system_prompt
            })

        if content: # ⭐️ 修改：只有当 content 列表不为空时才添加到 messages
            messages.append({
                "role": "user",
                "content": content
            })
            print(f"[DEBUG] Messages with image content: {json.dumps(messages, indent=2)}")  # 添加调试日志
        elif not prompt.strip() and not system_prompt and image is None: # ⭐️ 修改：更精确的判断用户是否提供了有效输入
            raise ValueError("用户输入的 prompt 不能为空")

        # 模型选择逻辑 (保持不变)
        selected_model = model if model else "glm-4"  # 默认模型为 glm-4
        print(f"[INFO] 使用模型: {selected_model}")

        # base_url 映射表 (保持不变)
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

        actual_base_url = base_url_mapping.get(base_url.strip(), base_url)

        # 对话历史和 payload 构建 (保持不变)
        if not hasattr(self, "_conversation_history"):
            self._conversation_history = []

        if system_prompt and not any(msg["role"] == "system" for msg in self._conversation_history):
            self._conversation_history.append({"role": "system", "content": system_prompt})

        # 避免重复添加内容
        if not any(msg["role"] == "user" and msg["content"] == content for msg in self._conversation_history):
            self._conversation_history.append({"role": "user", "content": content})

        messages = self._conversation_history # 重新从对话历史中获取 messages

        payload = {
            "model": selected_model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        print(f"[DEBUG] Full Payload with Image: {json.dumps(payload, indent=2)}")  # 添加调试日志
        print(f"[DEBUG] Full Payload Sent to API: {json.dumps(payload, indent=2)}")

        try:
            time.sleep(1)
            import asyncio

            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            try:
                task = loop.create_task(self.async_generate(payload, actual_base_url, api_key))
                return loop.run_until_complete(task)
            except Exception as e:
                print(f"[ERROR] 异步任务失败: {str(e)}")
                raise
            finally:
                if hasattr(loop, 'shutdown_asyncgens'):
                    loop.run_until_complete(loop.shutdown_asyncgens())
                loop.close()
        except Exception as e:
            raise Exception(f"请求失败: {str(e)}")


# 注册节点 (保持不变)
NODE_CLASS_MAPPINGS = {"OpenAICompatibleLoader": OpenAICompatibleLoader}
NODE_DISPLAY_NAME_MAPPINGS = {"OpenAICompatibleLoader": "OpenAI Compatible Adapter"}

WEB_DIRECTORY = "./web"
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
