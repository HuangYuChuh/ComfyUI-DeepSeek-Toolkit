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
                "processed_image": ("STRING", {"default": ""}),
                "system_prompt": ("STRING", {"default": "你是一个AI大模型", "multiline": True}),
                "prompt": ("STRING", {"multiline": True}),
                "temperature": ("FLOAT", {"default": 0.7, "min": 0.0, "max": 2.0}),
                "max_tokens": ("INT", {"default": 512, "min": 1, "max": 4096}),
                "enable_memory": ("BOOLEAN", {"default": False, "label": "Enable Memory"}),
            }
        }

    RETURN_TYPES = ("STRING", "INT", "INT")
    RETURN_NAMES = ("text", "input_tokens", "output_tokens")
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
                        # 移除冗长的API响应日志
                        response_content = data['choices'][0]['message']['content']
                        # 简化后的响应内容日志
                        print(f"Output: {response_content[:50]}...")  # 只保留前50个字符
                        return [response_content, data]  # 返回值包括 response_content 和 data
                except Exception as e:
                    print(f"[ERROR] 请求失败: {str(e)}")  # 打印错误信息
                    raise
        except ClientError as e:
            raise Exception(f"API request failed: {str(e)}")

    def generate(self, base_url: str, api_key: str, prompt: str,
                 model: str, temperature: float,
                 max_tokens: int, system_prompt: Optional[str] = None, processed_image: Optional[str] = None, enable_memory: bool = False):
        content = []  # 将 content 初始化放在函数的最开始

        # 移除图像参数类型的日志

        if processed_image:
            # 验证 processed_image 是否为有效的 base64 编码字符串
            if not processed_image.startswith("data:image"):
                raise ValueError("Processed image must be a valid base64 encoded string")

            # 将 processed_image 添加到 content 中
            content.append({"type": "image_url", "image_url": {"url": processed_image}})

        if prompt.strip():
            content.append({"type": "text", "text": prompt})

        messages = [] # 初始化 messages 列表
        if system_prompt:
            messages.append({
                "role": "system",
                "content": system_prompt
            })

        if content: # 只有当 content 列表不为空时才添加到 messages
            messages.append({
                "role": "user",
                "content": content
            })
            # 移除带有图像内容的消息日志
        elif not prompt.strip() and not system_prompt and processed_image is None: # 更精确的判断用户是否提供了有效输入
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
        if not enable_memory:
            self._conversation_history = []

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
        # 移除完整的payload日志
        # 简化后的调用日志
        # 使用时间戳代替 uuid 生成唯一标识符
        print(f"[{time.strftime('%Y/%m/%d %H:%M:%S')}] INFO PromptTask {int(time.time())}")
        print(f"Input: {prompt}")
        print(f"HTTP Request: POST {actual_base_url}/chat/completions \"HTTP/1.1 200 OK\"")

        # Token 计算逻辑
        def count_tokens(content):
            return sum(len(str(item).split()) for item in content)

        # 按字符分割
        input_tokens = len(prompt)
        if system_prompt:
            input_tokens += len(system_prompt)
        if processed_image:
            # 根据 processed_image 计算 token
            if isinstance(processed_image, str):  # Base64 编码的字符串
                # 估算 token 数量（基于字符串长度）
                image_tokens = len(processed_image) // 1000
            else:
                image_tokens = 0  # 未知类型，默认为 0
            input_tokens += image_tokens

        try:
            time.sleep(1)
            import asyncio

            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            try:
                task = loop.create_task(self.async_generate(payload, actual_base_url, api_key))
                response_content, data = loop.run_until_complete(task)
                # Extract completion_tokens from API response
                completion_tokens = data.get("usage", {}).get("completion_tokens", 0)
                return [[response_content], int(input_tokens), int(completion_tokens)]
            except Exception as e:
                print(f"[ERROR] 异步任务失败: {str(e)}")
                raise
            finally:
                try:
                    if hasattr(loop, 'shutdown_asyncgens'):
                        loop.run_until_complete(loop.shutdown_asyncgens())
                    # Ensure all tasks are done before closing the loop
                    pending = asyncio.all_tasks(loop)
                    if pending:
                        print(f"[WARNING] There are {len(pending)} pending tasks. Waiting for them to complete...")
                        loop.run_until_complete(asyncio.gather(*pending))
                finally:
                    loop.close()
        except Exception as e:
            raise Exception(f"请求失败: {str(e)}")


# 注册节点 (保持不变)
NODE_CLASS_MAPPINGS = {"OpenAICompatibleLoader": OpenAICompatibleLoader}
NODE_DISPLAY_NAME_MAPPINGS = {"OpenAICompatibleLoader": "OpenAI Compatible Adapter"}

WEB_DIRECTORY = "./web"
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
