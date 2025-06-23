# 🚀 ComfyUI-LLMs-Toolkit

<div align="right">

**Language / 语言**
| [🇨🇳 中文](README.md) | [🇺🇸 English](docs/readme_en.md) |
|---------|---------|

</div>

**为ComfyUI工作流程注入强大的大语言模型力量！**

[![GitHub Stars](https://img.shields.io/github/stars/HuangYuChuh/ComfyUI-LLMs-Toolkit?style=flat-square&logo=github)](https://github.com/HuangYuChuh/ComfyUI-LLMs-Toolkit/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/HuangYuChuh/ComfyUI-LLMs-Toolkit?style=flat-square&logo=github)](https://github.com/HuangYuChuh/ComfyUI-LLMs-Toolkit/network)
[![License](https://img.shields.io/github/license/HuangYuChuh/ComfyUI-LLMs-Toolkit?style=flat-square)](https://github.com/HuangYuChuh/ComfyUI-LLMs-Toolkit/blob/main/LICENSE)

> 一个集成全球领先大语言模型的ComfyUI自定义节点套件

## 📖 项目简介

ComfyUI-LLMs-Toolkit 专为ComfyUI设计，将DeepSeek、通义千问、GPT等优秀的大语言模型无缝集成到您的AI工作流程中。

## 🚀 快速开始

### 📋 安装步骤

```bash
# 1. 克隆项目到ComfyUI的custom_nodes目录
cd ComfyUI/custom_nodes/
git clone https://github.com/HuangYuChuh/ComfyUI-LLMs-Toolkit.git

# 2. 进入项目目录
cd ComfyUI-LLMs-Toolkit

# 3. 安装依赖
pip install -r requirements.txt
```

### ⚙️ 环境配置

#### 1. 创建环境变量文件

```bash
# 复制环境变量示例文件
cp config/env.example .env
```

#### 2. 配置API密钥

编辑 `.env` 文件，填入您的API配置：

```bash
# DeepSeek配置（必填其中之一）
DEEPSEEK_API_KEY=your_deepseek_api_key_here
DEEPSEEK_BASE_URL=https://api.deepseek.com
DEEPSEEK_MODEL_NAME=deepseek-chat

# 通义千问配置
QWEN_API_KEY=your_qwen_api_key_here
QWEN_BASE_URL=https://dashscope.aliyun.com/api/v1
QWEN_MODEL_NAME=qwen-max

# OpenAI配置
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_BASE_URL=https://api.openai.com/v1
OPENAI_MODEL_NAME=gpt-3.5-turbo

# 更多模型配置请参考 config/env.example
```

#### 3. 获取API密钥

| 模型提供商 | 获取地址 | 说明 |
|-----------|---------|------|
| 🔥 **DeepSeek** | [platform.deepseek.com](https://platform.deepseek.com/) | 新用户有免费额度 |
| 🌟 **通义千问** | [dashscope.aliyun.com](https://dashscope.aliyun.com/) | 阿里云账号登录 |
| 🤖 **OpenAI** | [platform.openai.com](https://platform.openai.com/) | GPT系列模型 |
| 🚀 **豆包** | [console.volcengine.com](https://console.volcengine.com/) | 字节跳动产品 |
| ⚡ **星火** | [console.xfyun.cn](https://console.xfyun.cn/) | 科大讯飞产品 |
| 🧠 **智谱清言** | [open.bigmodel.cn](https://open.bigmodel.cn/) | 清华技术 |
| 🌙 **月之暗面** | [platform.moonshot.cn](https://platform.moonshot.cn/) | Kimi Chat团队 |

### 🎯 基础使用

1. **重启ComfyUI** - 配置完成后重启ComfyUI以加载节点
2. **添加节点** - 在节点菜单中找到 \`LLMs Toolkit\` 分类
3. **配置模型** - 选择要使用的LLM模型和参数
4. **开始创作** - 连接工作流开始您的AI创作之旅

## 📄 许可证

本项目采用 [GPL-2.0](LICENSE) 开源协议。

---

<div align="center">

**⭐ 如果这个项目对您有帮助，请给我们一个Star！**

[![Star History Chart](https://api.star-history.com/svg?repos=HuangYuChuh/ComfyUI-LLMs-Toolkit&type=Date)](https://star-history.com/#HuangYuChuh/ComfyUI-LLMs-Toolkit&Date)

</div>
