import aiohttp
import asyncio
from aiohttp import ClientSession, ClientError
from typing import Optional
import base64
from PIL import Image
import io
import torch

class ImageUploader:
    """
    Custom node for uploading images to an image hosting service
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "api_key": ("STRING", {"default": ""}),
                "image": ("IMAGE", {}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("image_url",)
    FUNCTION = "upload_image"
    CATEGORY = "DeepSeek_Toolkit"

    async def upload_image_to_smms(self, image_data: bytes, api_key: str) -> Optional[str]:
        """
        Upload image to SM.MS image hosting service and return the URL.
        """
        url = "https://pnglog.com/api/v1/upload"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Accept": "application/json"
        }
        data = aiohttp.FormData()
        data.add_field('file', image_data, filename='image.png', content_type='image/png')

        try:
            async with ClientSession() as session:
                async with session.post(url, headers=headers, data=data) as response:
                    if response.status == 200:
                        result = await response.json()
                        if result.get("success"):
                            return result["data"]["url"]
                        else:
                            print(f"[ERROR] Image upload failed: {result.get('message')}")
                    else:
                        print(f"[ERROR] Image upload failed with status code: {response.status}")
        except Exception as e:
            print(f"[ERROR] Image upload error: {str(e)}")
        return None

    def upload_image(self, api_key: str, image: Optional[str]):
        content = []  # 将 content 初始化放在函数的最开始

        print(f"[DEBUG] Image parameter type: {type(image)}, value: {image}")

        if image is not None:  # 精简 image 处理逻辑，只保留一个 if image is not None 块
            buffered = None  # 初始化 buffered 变量
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

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            task = loop.create_task(self.upload_image_to_smms(buffered.getvalue() if buffered else image.encode(), api_key))
            image_url = loop.run_until_complete(task)
        finally:
            if hasattr(loop, 'shutdown_asyncgens'):
                loop.run_until_complete(loop.shutdown_asyncgens())
            loop.close()

        if image_url:
            return (image_url,)
        else:
            return ("",)


# 注册节点
NODE_CLASS_MAPPINGS = {"ImageUploader": ImageUploader}
NODE_DISPLAY_NAME_MAPPINGS = {"ImageUploader": "Image Uploader"}

WEB_DIRECTORY = "./web"
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']