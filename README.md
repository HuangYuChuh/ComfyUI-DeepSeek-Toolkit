# ComfyUI DeepSeek Janus Pro Node

## Overview
This custom node for ComfyUI provides advanced multi-modal AI capabilities using DeepSeek Janus Pro models, enabling image generation, understanding, and analysis.

## Features
- 🔍 Image Understanding
- 🖼️ Image Generation
- 🤖 Multi-modal AI Processing

## Installation

### Prerequisites
- ComfyUI
- Python 3.8+
- CUDA-capable GPU (recommended)

### Setup
1. Clone the repository into your ComfyUI `custom_nodes` directory:
```bash
cd custom_nodes
git clone https://github.com/yourusername/ComfyUI-DeepSeek_Janus.git
```

2. Install dependencies:
```bash
cd ComfyUI-DeepSeek_Janus
pip install -r requirements.txt
```

3. Download DeepSeek Janus Pro model:
- Place the model in `ComfyUI/models/deepseek_janus/`

## Available Nodes

### 1. DeepSeek Model Loader
- Load DeepSeek Janus Pro models
- Supports local and remote model loading
- Automatic device and precision selection

### 2. Image Understanding
- Analyze images with detailed descriptions
- Supports custom prompts and questions
- Multi-modal understanding capabilities

### 3. Image Generation
- Generate images from text prompts
- Configurable generation parameters
- Batch image generation support

## Usage Examples

### Basic Image Understanding
1. Load Model
2. Connect an Image
3. Provide a Question
4. Get Detailed Analysis

### Image Generation
1. Load Model
2. Input Prompt
3. Configure Generation Parameters
4. Generate Images

## Model Versions
- Janus Pro 1B
- Janus Pro 7B

## Troubleshooting
- Ensure CUDA is properly installed
- Check model download and placement
- Verify dependencies are correctly installed

## Contributing
Contributions are welcome! Please submit pull requests or open issues.

## License
[Your License Here]

## Acknowledgements
- DeepSeek AI
- ComfyUI Community
