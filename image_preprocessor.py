import base64
import io
from PIL import Image
from typing import Optional, Union
import torch

class ImagePreprocessor:
    """
    Custom node for preprocessing images before passing them to LLMs.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE", {"default": None}),
            },
            "optional": {
                "format": ("STRING", {"default": "PNG"}),
                "quality": ("INT", {"default": 95, "min": 1, "max": 100}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("processed_image",)
    FUNCTION = "preprocess"
    CATEGORY = "DeepSeek_Toolkit"

    def preprocess(self, image: Optional[Union[str, Image.Image]], format: str = "PNG", quality: int = 95):
        if image is None:
            raise ValueError("Image input cannot be None")

        # Convert image to PIL object if it's a tensor
        if isinstance(image, torch.Tensor):
            image = image.squeeze(0).cpu().numpy()  # [H, W, C]
            if image.shape[2] == 1:  # Grayscale image
                image = image.squeeze(-1)
            image = (image * 255).astype('uint8')
            image = Image.fromarray(image)

        # Ensure the image is a PIL object
        elif not isinstance(image, Image.Image):
            raise ValueError("Unsupported image type. Expected torch.Tensor or PIL.Image.")

        # Convert PIL image to base64 string
        buffered = io.BytesIO()
        image.save(buffered, format=format, quality=quality)
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
        image_url = f"data:image/{format.lower()};base64,{img_str}"

        return (image_url,)


# Register the node with ComfyUI
NODE_CLASS_MAPPINGS = {"ImagePreprocessor": ImagePreprocessor}
NODE_DISPLAY_NAME_MAPPINGS = {"ImagePreprocessor": "Image Preprocessor"}