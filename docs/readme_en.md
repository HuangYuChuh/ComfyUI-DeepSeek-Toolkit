# 🚀 ComfyUI-LLMs-Toolkit

<div align="right">

**Language / 语言**
| [🇨🇳 中文](../README.md) | [🇺🇸 English](readme_en.md) |
|---------|---------|

</div>

**Inject powerful Large Language Models into your ComfyUI workflows!**

[![GitHub Stars](https://img.shields.io/github/stars/HuangYuChuh/ComfyUI-LLMs-Toolkit?style=flat-square&logo=github)](https://github.com/HuangYuChuh/ComfyUI-LLMs-Toolkit/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/HuangYuChuh/ComfyUI-LLMs-Toolkit?style=flat-square&logo=github)](https://github.com/HuangYuChuh/ComfyUI-LLMs-Toolkit/network)
[![License](https://img.shields.io/github/license/HuangYuChuh/ComfyUI-LLMs-Toolkit?style=flat-square)](https://github.com/HuangYuChuh/ComfyUI-LLMs-Toolkit/blob/main/LICENSE)

> A ComfyUI custom node suite integrating leading Large Language Models worldwide

## 📖 Project Overview

ComfyUI-LLMs-Toolkit is designed specifically for ComfyUI, seamlessly integrating excellent Large Language Models such as DeepSeek, Qwen, GPT, and others into your AI workflows.

## 🚀 Quick Start

### 📋 Installation Steps

```bash
# 1. Clone the project to ComfyUI's custom_nodes directory
cd ComfyUI/custom_nodes/
git clone https://github.com/HuangYuChuh/ComfyUI-LLMs-Toolkit.git

# 2. Enter project directory
cd ComfyUI-LLMs-Toolkit

# 3. Install dependencies
pip install -r requirements.txt
```

### ⚙️ Environment Configuration

#### 1. Create Environment Variable File

```bash
# Copy the environment variable example file
cp config/env.example .env
```

#### 2. Configure API Keys

Edit the `.env` file and fill in your API configuration:

```bash
# DeepSeek Configuration (fill in at least one)
DEEPSEEK_API_KEY=your_deepseek_api_key_here
DEEPSEEK_BASE_URL=https://api.deepseek.com
DEEPSEEK_MODEL_NAME=deepseek-chat

# Qwen Configuration
QWEN_API_KEY=your_qwen_api_key_here
QWEN_BASE_URL=https://dashscope.aliyun.com/api/v1
QWEN_MODEL_NAME=qwen-max

# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_BASE_URL=https://api.openai.com/v1
OPENAI_MODEL_NAME=gpt-3.5-turbo
```

### 🎯 Basic Usage

1. **Restart ComfyUI** - Restart ComfyUI after configuration to load nodes
2. **Add Nodes** - Find the \`LLMs Toolkit\` category in the node menu
3. **Configure Model** - Select the LLM model and parameters you want to use
4. **Start Creating** - Connect workflows to begin your AI creation journey

## 🌟 Supported Models

### 🇨🇳 Chinese Large Language Models

| Model | Provider | Key Features | Config Prefix |
|-------|----------|--------------|---------------|
| DeepSeek-V3 | DeepSeek | Superior reasoning, code generation | \`DEEPSEEK_\` |
| Qwen-Max | Alibaba Cloud | Multimodal understanding, Chinese optimization | \`QWEN_\` |
| Doubao-Pro | ByteDance | Dialogue generation, creative writing | \`DOUBAO_\` |
| Spark-Max | iFLYTEK | Language understanding, text analysis | \`SPARK_\` |
| GLM-4 | Zhipu AI | Knowledge Q&A, logical reasoning | \`GLM_\` |
| Moonshot-V1 | Moonshot AI | Long text processing | \`MOONSHOT_\` |

### 🌍 International Large Language Models

| Model | Provider | Key Features | Config Prefix |
|-------|----------|--------------|---------------|
| GPT-4 | OpenAI | General intelligence, multimodal | \`OPENAI_\` |
| Claude | Anthropic | Safe dialogue, long text | \`CLAUDE_\` |
| Gemini | Google | Multimodal understanding | \`GEMINI_\` |

## 📄 License

This project is licensed under the [GPL-2.0](../LICENSE) open source license.

---

<div align="center">

**⭐ If this project helps you, please give us a Star!**

[![Star History Chart](https://api.star-history.com/svg?repos=HuangYuChuh/ComfyUI-LLMs-Toolkit&type=Date)](https://star-history.com/#HuangYuChuh/ComfyUI-LLMs-Toolkit&Date)

</div>
