import os
import sys
from typing import Dict, Any

# Add the current directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

# Import node mappings from each module
# 使用相对导入
from .model_loader import NODE_CLASS_MAPPINGS as MODEL_LOADER_NODES
from .image_understanding import NODE_CLASS_MAPPINGS as IMAGE_UNDERSTANDING_NODES
from .image_generation import NODE_CLASS_MAPPINGS as IMAGE_GENERATION_NODES
from .openai_compatible_loader import NODE_CLASS_MAPPINGS as OPENAI_LOADER_NODES, NODE_DISPLAY_NAME_MAPPINGS as OPENAI_LOADER_DISPLAY_NAMES

# Combine all node mappings
NODE_CLASS_MAPPINGS: Dict[str, Any] = {
    **MODEL_LOADER_NODES,
    **IMAGE_UNDERSTANDING_NODES,
    **IMAGE_GENERATION_NODES,
    **OPENAI_LOADER_NODES,
}

# Initialize display name mappings
NODE_DISPLAY_NAME_MAPPINGS = {}

# Update display name mappings
NODE_DISPLAY_NAME_MAPPINGS.update(OPENAI_LOADER_DISPLAY_NAMES)

# Define display names for nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "DeepSeekModelLoader": "Multimodal Loader",
    "DeepSeekImageUnderstanding": "DeepSeek Image Understanding",
    "DeepSeekImageGeneration": "DeepSeek Image Generation",
    "OpenAICompatibleLoader": "OpenAI Compatible Loader"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

# from .Loader import *
def init_custom_nodes():
    """Initialize any custom nodes setup here"""
    print("Initializing DeepSeek Janus Pro nodes...")