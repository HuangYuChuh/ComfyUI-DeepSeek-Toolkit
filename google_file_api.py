import os
import io
import base64
from typing import Tuple, Optional
import google.generativeai as genai  # 导入 Gemini API
import time
import folder_paths
import json

class GoogleDriveUpload:
    """
    A ComfyUI node for uploading video files to Gemini via File API.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "api_key": ("STRING", {"multiline": False, "default": ""}),  # API 密钥字符串
                "file_path": ("STRING", {"default": "", "label": "Video File Path"}),
                "file_name": ("STRING", {"default": "", "label": "File Name"}),
                # "mime_type": (["video/mp4", "video/avi", "video/quicktime", "video/x-matroska"], {"default": "video/mp4", "label": "MIME Type"}), # Gemini File API 不需要mime_type
                # "folder_id": ("STRING", {"default": "", "label": "Google Drive Folder ID", "description": "Optional: If empty, uploads to root."}), # Gemini File API 不需要folder_id
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("file_uri",)
    FUNCTION = "upload_file"
    CATEGORY = "DeepSeek_Toolkit/Google Drive"

    def upload_file(self, api_key: str, file_path: str, file_name: str) -> Tuple[str]:
        """
        Uploads a file to Gemini via File API.

        Args:
            api_key (str): The Gemini API key.
            file_path (str): The path to the file to upload.
            file_name (str): The desired name for the file on Gemini.

        Returns:
            str: The URI of the uploaded file.
        """
        try:
            # 1. 验证 API 密钥
            if not api_key:
                raise ValueError("API 密钥不能为空")

            # 2. 验证文件路径
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"文件未找到: {file_path}")

            # 3. 构建 Gemini API 客户端
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel(model_name="gemini-1.5-pro") # 假设使用 gemini-1.5-pro 模型
            client = model

            # 4. 上传文件
            print("Uploading file...")
            video_file = client.upload(path=file_path, name=file_name)
            file_uri = video_file.uri
            print(f"Completed upload: {file_uri}")

            return (file_uri,)

        except Exception as e:
            print(f"上传文件时发生错误: {e}")
            return (f"Error: {str(e)}",)


# 节点类映射
NODE_CLASS_MAPPINGS = {
    "GoogleDriveUpload": GoogleDriveUpload
}

# 节点显示名称映射
NODE_DISPLAY_NAME_MAPPINGS = {
    "GoogleDriveUpload": "Google Drive Upload (Gemini File API)"
}