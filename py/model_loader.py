import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import logging

logger = logging.getLogger(__name__)

class DeepSeekModelLoader:
    """Loader for DeepSeek models"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model_path": ("STRING", {"default": ""}),
                "device": (["cuda", "cpu"], {"default": "cuda"})
            }
        }

    RETURN_TYPES = ("MODEL", "TOKENIZER")
    FUNCTION = "load_model"
    CATEGORY = "DeepSeek"

    def load_model(self, model_path: str, device: str = "cuda"):
        logger.info(f"Loading model from {model_path} onto {device}")
        try:
            model = AutoModelForCausalLM.from_pretrained(
                model_path,
                trust_remote_code=True,
                torch_dtype=torch.float16,
                low_cpu_mem_usage=True
            ).to(device)
            
            tokenizer = AutoTokenizer.from_pretrained(
                model_path,
                trust_remote_code=True
            )
            
            # Verify tokenizer components
            required_attrs = {
                'eos_token_id': "End-of-sequence token ID",
                'encode': "Text encoding function",
                'decode': "Text decoding function",
                '__call__': "Tokenizer main method"
            }
            
            missing = {}
            for attr, desc in required_attrs.items():
                if not hasattr(tokenizer, attr):
                    missing[attr] = desc
            
            if missing:
                error_msg = (
                    "Loaded tokenizer is incomplete. Missing critical components:\n" +
                    "\n".join([f"- {attr}: {desc}" for attr, desc in missing.items()]) +
                    "\n\nPlease ensure you're using a compatible tokenizer implementation."
                )
                logger.error(error_msg)
                raise ValueError(error_msg)
                
            return (model, tokenizer)
            
        except Exception as e:
            logger.error(f"Failed to load model or tokenizer: {str(e)}", exc_info=True)
            raise

# Node mappings
NODE_CLASS_MAPPINGS = {
    "DeepSeekModelLoader": DeepSeekModelLoader
}

# Node display name mappings
NODE_DISPLAY_NAME_MAPPINGS = {
    "DeepSeekModelLoader": "DeepSeek Model Loader"
}
