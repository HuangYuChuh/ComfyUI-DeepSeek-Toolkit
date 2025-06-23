# 🚀 ComfyUI-LLMs-Toolkit

<div align="center">

**🌐 Language / 语言切换**

[![🇨🇳 简体中文](https://img.shields.io/badge/README-简体中文-red?style=for-the-badge)](README.md)
[![��🇸 English](https://img.shields.io/badge/README-English-blue?style=for-the-badge)](docs/readme_en.md)

---

[![GitHub Stars](https://img.shields.io/github/stars/HuangYuChuh/ComfyUI-LLMs-Toolkit?style=flat-square&logo=github&color=yellow)](https://github.com/HuangYuChuh/ComfyUI-LLMs-Toolkit/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/HuangYuChuh/ComfyUI-LLMs-Toolkit?style=flat-square&logo=github&color=green)](https://github.com/HuangYuChuh/ComfyUI-LLMs-Toolkit/network)
[![GitHub Issues](https://img.shields.io/github/issues/HuangYuChuh/ComfyUI-LLMs-Toolkit?style=flat-square&logo=github&color=red)](https://github.com/HuangYuChuh/ComfyUI-LLMs-Toolkit/issues)
[![License](https://img.shields.io/github/license/HuangYuChuh/ComfyUI-LLMs-Toolkit?style=flat-square&color=blue)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/HuangYuChuh/ComfyUI-LLMs-Toolkit?style=flat-square&color=orange)](https://github.com/HuangYuChuh/ComfyUI-LLMs-Toolkit/commits)

**🔥 为ComfyUI工作流程注入强大的大语言模型力量！**

*一个专业级的ComfyUI自定义节点套件，支持全球领先的大语言模型*

</div>

---

## 📖 项目简介

ComfyUI-LLMs-Toolkit 是一个高性能的ComfyUI扩展，专为AI创作者设计。通过轻量级API驱动方案，即使在有限计算资源下也能轻松接入DeepSeek、通义千问、GPT等世界级大语言模型，让AI创作民主化。

### 🎯 为什么选择我们？

- **🚀 零硬件门槛**：无需高端GPU，仅需API即可享受前沿AI能力
- **🌍 全球模型支持**：集成中外主流LLM，一站式解决方案
- **⚡ 高性能架构**：优化的并发处理，大幅提升工作流效率
- **��️ 极客友好** - 环境变量配置，开发者至上

---

## ✨ 核心特性

### 🧠 强大的LLM生态系统

| 类别 | 支持模型 | 特色能力 |
|------|----------|----------|
| **🇨🇳 中国领军** | DeepSeek-V3, Qwen-Max, GLM-4 | 中文理解、代码生成、数学推理 |
| **🇺🇸 国际巨头** | GPT-4, Claude-3, Gemini | 多模态处理、创意写作、复杂推理 |
| **⚡ 专业垂直** | Doubao, Spark, Moonshot | 对话生成、长文本、角色扮演 |

### 🔧 技术亮点

- **✨ 闪电部署**：一键安装，五分钟上手
- **⚡ 并发优化**：多线程处理，支持批量请求
- **🛡️ 安全为先**：环境变量配置，密钥安全管理
- **🔄 热重载**：动态配置更新，无需重启ComfyUI
- **📊 智能缓存**：响应缓存机制，降低API调用成本

---

## 🚀 快速开始

### 📋 系统要求

- **Python**: \`>= 3.8\`
- **ComfyUI**: 最新版本
- **内存**: \`>= 4GB RAM\`
- **网络**: 稳定的互联网连接

### ⚡ 安装步骤

#### 方法一：ComfyUI Manager（推荐）

1. 在ComfyUI中打开 **Manager** 面板
2. 搜索 `ComfyUI-LLMs-Toolkit`
3. 点击 **安装** 并重启ComfyUI

#### 方法二：手动安装

```bash
# 进入ComfyUI的custom_nodes目录
cd ComfyUI/custom_nodes/

# 克隆项目
git clone https://github.com/HuangYuChuh/ComfyUI-LLMs-Toolkit.git

# 进入项目目录
cd ComfyUI-LLMs-Toolkit

# 安装依赖
pip install -r requirements.txt
```

### ⚙️ 环境配置

#### 1️⃣ 创建配置文件

\`\`\`bash
# 复制环境变量模板
cp config/env.example .env
\`\`\`

#### 2️⃣ 配置API密钥

编辑 \`.env\` 文件，选择您要使用的模型：

\`\`\`bash
# 🔥 DeepSeek（推荐新手）
DEEPSEEK_API_KEY=sk-your_deepseek_key_here
DEEPSEEK_BASE_URL=https://api.deepseek.com
DEEPSEEK_MODEL_NAME=deepseek-chat

# 🌟 通义千问（中文优化）
QWEN_API_KEY=your_qwen_key_here
QWEN_BASE_URL=https://dashscope.aliyuncs.com/api/v1
QWEN_MODEL_NAME=qwen-max

# 🤖 OpenAI GPT（国际标准）
OPENAI_API_KEY=sk-your_openai_key_here
OPENAI_BASE_URL=https://api.openai.com/v1
OPENAI_MODEL_NAME=gpt-4o-mini

# 🚀 更多配置参见 config/env.example
\`\`\`

#### 3️⃣ API密钥获取指南

| 🏢 提供商 | 🔗 获取地址 | 💰 免费额度 | ⭐ 推荐指数 |
|-----------|-------------|-------------|-------------|
| **DeepSeek** | [platform.deepseek.com](https://platform.deepseek.com/) | ¥500免费额度 | ⭐⭐⭐⭐⭐ |
| **通义千问** | [dashscope.aliyun.com](https://dashscope.aliyun.com/) | 每月100万tokens | ⭐⭐⭐⭐ |
| **OpenAI** | [platform.openai.com](https://platform.openai.com/) | $5体验额度 | ⭐⭐⭐⭐⭐ |
| **智谱清言** | [open.bigmodel.cn](https://open.bigmodel.cn/) | 每月500万tokens | ⭐⭐⭐⭐ |

### 🎯 第一次运行

1. **🔄 重启ComfyUI**：
   \`\`\`bash
   # 重启ComfyUI以加载新节点
   cd /path/to/ComfyUI
   python main.py
   \`\`\`

2. **🔍 查找节点**：
   - 在ComfyUI界面中右键
   - 导航至 \`Add Node\` → \`LLMs Toolkit\`
   - 选择您需要的节点类型

3. **⚡ 开始创作**：
   - 拖入LLM节点
   - 配置模型参数
   - 连接输入输出
   - 享受AI创作之旅！

---

## 🌟 支持的模型矩阵

### 🇨🇳 中国AI军团

| 模型 | 提供商 | 核心优势 | 价格等级 | 配置前缀 |
|------|--------|----------|----------|----------|
| **DeepSeek-V3** | DeepSeek | 🧮 数学推理、💻 代码生成 | 💚 超低价 | \`DEEPSEEK_\` |
| **Qwen-Max** | 阿里巴巴 | 🌏 多模态、🇨🇳 中文优化 | 💛 中等 | \`QWEN_\` |
| **GLM-4** | 智谱AI | 🤔 逻辑推理、📚 知识问答 | 💚 低价 | \`GLM_\` |
| **Doubao-Pro** | 字节跳动 | 💬 对话生成、✍️ 创意写作 | 💛 中等 | \`DOUBAO_\` |
| **Spark-Max** | 科大讯飞 | 🗣️ 语言理解、📊 文本分析 | 💚 低价 | \`SPARK_\` |
| **Moonshot-V1** | 月之暗面 | 📖 长文本、🧠 深度理解 | 💛 中等 | \`MOONSHOT_\` |

### 🌍 国际AI豪门

| 模型 | 提供商 | 核心优势 | 价格等级 | 配置前缀 |
|------|--------|----------|----------|----------|
| **GPT-4o** | OpenAI | 🧠 通用智能、🎨 多模态 | 🧡 高价 | \`OPENAI_\` |
| **Claude-3.5** | Anthropic | 🛡️ 安全对话、📚 长文本 | 🧡 高价 | \`CLAUDE_\` |
| **Gemini-Pro** | Google | 🔍 搜索增强、🌐 多语言 | 💛 中等 | \`GEMINI_\` |

---

## ❓ 常见问题

<details>
<summary><strong>🔑 Q: 如何获取API密钥？</strong></summary>

**A**: 各大厂商都提供免费试用额度：
- **DeepSeek**: 注册即送¥500额度，适合新手试用
- **通义千问**: 阿里云账号认证后可获得大额度
- **OpenAI**: 新用户有$5免费额度，需要国外支付方式

</details>

<details>
<summary><strong>🖥️ Q: 支持本地模型吗？</strong></summary>

**A**: 目前主要支持API调用，本地模型支持已在开发路线图中：
- **v2.0**: 计划支持Ollama本地模型
- **v2.1**: 支持GGUF格式模型
- **v3.0**: 支持自定义模型微调

</details>

<details>
<summary><strong>❌ Q: 遇到连接错误怎么办？</strong></summary>

**A**: 常见解决方案：
1. **检查网络**：确保能访问对应API服务
2. **验证密钥**：确认API密钥正确且有余额
3. **检查配置**：确认BASE_URL格式正确
4. **查看日志**：检查ComfyUI控制台输出

</details>

---

## 📄 开源协议

本项目采用 **[GNU General Public License v2.0](LICENSE)** 开源协议。

**这意味着：**
- ✅ **自由使用**：个人和商业使用均可
- ✅ **自由修改**：可以修改源代码
- ✅ **自由分发**：可以分发原版或修改版
- ⚠️ **开源义务**：修改版必须开源

---

<div align="center">

### 🌟 如果这个项目对您有帮助，请给我们一个Star！

[![Star History Chart](https://api.star-history.com/svg?repos=HuangYuChuh/ComfyUI-LLMs-Toolkit&type=Date)](https://star-history.com/#HuangYuChuh/ComfyUI-LLMs-Toolkit&Date)

**📞 联系我们**

[![GitHub](https://img.shields.io/badge/GitHub-@HuangYuChuh-181717?style=flat-square&logo=github)](https://github.com/HuangYuChuh)
[![Email](https://img.shields.io/badge/Email-联系邮箱-red?style=flat-square&logo=gmail)](mailto:your-email@example.com)

---

**💡 Made with ❤️ for the ComfyUI community**

*让AI创作更简单，让技术更有温度*

</div>


