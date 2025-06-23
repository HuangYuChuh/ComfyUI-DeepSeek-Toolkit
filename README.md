<div align="center">

# 🚀 ComfyUI-DeepSeek-Toolkit

**为ComfyUI工作流程注入强大的大语言模型力量！**

[![GitHub Stars](https://img.shields.io/github/stars/HuangYuChuh/ComfyUI-DeepSeek-Toolkit?style=flat-square&logo=github)](https://github.com/HuangYuChuh/ComfyUI-DeepSeek-Toolkit/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/HuangYuChuh/ComfyUI-DeepSeek-Toolkit?style=flat-square&logo=github)](https://github.com/HuangYuChuh/ComfyUI-DeepSeek-Toolkit/network)
[![License](https://img.shields.io/github/license/HuangYuChuh/ComfyUI-DeepSeek-Toolkit?style=flat-square)](https://github.com/HuangYuChuh/ComfyUI-DeepSeek-Toolkit/blob/main/LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)](https://www.python.org/)

**一个集成中国领先大语言模型的ComfyUI自定义节点套件**

</div>

---

## 📖 项目介绍

ComfyUI-DeepSeek-Toolkit 是一个专为ComfyUI设计的自定义节点包，致力于将中国最优秀的大语言模型（如DeepSeek、通义千问等）无缝集成到您的AI工作流程中。通过轻量级的API驱动方案，即使是计算资源有限的用户也能轻松体验到前沿AI技术的强大能力。

### 🎯 项目愿景

> **让AI技术惠及每一个创作者**
> 
> 我们相信AI应该是赋能工具，而非不平等的根源。通过提供易于访问的解决方案，我们致力于让AI成为一种更具包容性和公平性的技术。

---

## ✨ 核心特性

### 🤖 支持的大语言模型

| 模型提供商 | 模型名称 | 特色功能 |
|-----------|---------|---------|
| 🔥 **DeepSeek** | DeepSeek-V2/V3 | 超强推理能力，代码生成专家 |
| 🌟 **通义千问** | Qwen-Max/Plus | 多模态理解，中文优化 |
| 🚀 **豆包** | Doubao-Pro | 对话生成，创意写作 |
| ⚡ **星火** | Spark-Max | 语言理解，文本分析 |
| 🧠 **智谱清言** | GLM-4 | 知识问答，逻辑推理 |
| 🌙 **月之暗面** | Moonshot-V1 | 长文本处理，上下文理解 |
| 🌊 **百川** | Baichuan-Turbo | 快速响应，高效处理 |
| 🎭 **MiniMax** | ABAB-6.5 | 角色扮演，创意生成 |
| 🔮 **阶跃星辰** | Step-1X | 多任务处理，智能推理 |

### 🛠️ 功能模块

<div align="center">

| 模块名称 | 功能描述 | 适用场景 |
|---------|---------|----------|
| 🔧 **LLM加载器** | 配置和加载不同的大语言模型 | 模型切换、参数调优 |
| 🎨 **图像生成** | 基于文本描述生成高质量图像 | 创意设计、内容创作 |
| 👁️ **图像理解** | 智能分析和描述图像内容 | 图像标注、内容审核 |
| 📦 **模型管理** | 统一管理各种AI模型资源 | 模型版本控制、资源优化 |
| 🔌 **OpenAI兼容** | 支持OpenAI格式的API调用 | 兼容性扩展、迁移便利 |
| 🖼️ **图像预处理** | 智能优化图像质量和格式 | 数据清洗、格式转换 |

</div>

---

## 🚀 快速开始

### 📋 环境要求

- **Python**: 3.8 或更高版本
- **ComfyUI**: 最新稳定版本
- **操作系统**: Windows / macOS / Linux

### 🔧 安装指南

#### 方法一：通过ComfyUI Manager安装（推荐）

1. 在ComfyUI中打开 **Manager** 面板
2. 搜索 \`ComfyUI-DeepSeek-Toolkit\`
3. 点击 **安装** 并重启ComfyUI

#### 方法二：手动安装

\`\`\`bash
# 进入ComfyUI的custom_nodes目录
cd ComfyUI/custom_nodes/

# 克隆项目
git clone https://github.com/HuangYuChuh/ComfyUI-DeepSeek-Toolkit.git

# 进入项目目录
cd ComfyUI-DeepSeek-Toolkit

# 安装依赖
pip install -r requirements.txt
\`\`\`

### 🔑 API密钥配置

在使用前，您需要获取相应模型的API密钥：

1. **DeepSeek**: [获取API密钥](https://platform.deepseek.com/)
2. **通义千问**: [获取API密钥](https://dashscope.aliyun.com/)
3. **其他模型**: 请参考 [LLM API调用指南](./LLM%20API%20调用指南（中国版）.md)

---

## 📚 使用指南

### 🎯 基础工作流程

1. **加载LLM节点**
   - 在ComfyUI中添加 \`DeepSeek LLM Loader\` 节点
   - 配置API密钥和模型参数

2. **连接功能节点**
   - 根据需求添加图像生成/理解节点
   - 配置输入输出连接

3. **运行工作流程**
   - 设置提示词和参数
   - 执行并查看结果

---

## 🛠️ 技术架构

### 📦 依赖项

\`\`\`txt
torch>=1.9.0
numpy>=1.21.0
Pillow>=8.3.0
aiohttp>=3.8.0
transformers>=4.20.0
git+https://github.com/deepseek-ai/Janus.git
\`\`\`

### 🏗️ 项目结构

\`\`\`
ComfyUI-DeepSeek-Toolkit/
├── 📁 py/                          # 核心模块目录
│   ├── 🔧 llm_loader.py            # LLM加载器
│   ├── 🎨 image_generation.py      # 图像生成模块
│   ├── 👁️ image_understanding.py   # 图像理解模块
│   ├── 📦 model_loader.py          # 模型管理器
│   ├── 🔌 openai_compatible_loader.py # OpenAI兼容层
│   └── 🖼️ image_preprocessor.py    # 图像预处理器
├── 📄 __init__.py                   # 主入口文件
├── 📋 requirements.txt              # 依赖列表
├── 📖 README.md                     # 项目文档
├── 📘 readme_en.md                  # 英文文档
├── 📙 LLM API 调用指南（中国版）.md  # API调用指南
└── 📜 LICENSE                       # 开源协议
\`\`\`

---

## 🤝 贡献指南

我们欢迎所有形式的贡献！

### 🐛 报告问题

如果您发现了bug或有功能建议：

1. 在 [Issues](https://github.com/HuangYuChuh/ComfyUI-DeepSeek-Toolkit/issues) 中搜索相似问题
2. 如果没有找到，请创建新的issue
3. 请提供详细的描述和复现步骤

### 💡 提交代码

1. Fork本项目
2. 创建功能分支 (\`git checkout -b feature/AmazingFeature\`)
3. 提交更改 (\`git commit -m 'Add some AmazingFeature'\`)
4. 推送到分支 (\`git push origin feature/AmazingFeature\`)
5. 创建Pull Request

---

## 📈 发展路线图

### 🎯 近期计划

- [ ] 🚀 **v1.1.0**
  - [ ] 支持更多视频理解模型
  - [ ] 增加批处理功能
  - [ ] 优化内存使用

- [ ] 🌟 **v1.2.0**
  - [ ] 集成更多中国AI模型
  - [ ] 添加模型微调功能
  - [ ] 提供预构建工作流模板

### 🔮 长期规划

- 🧠 **智能化升级**: 自适应模型选择和参数优化
- 🌐 **生态扩展**: 与更多AI平台和工具集成
- 📊 **性能监控**: 实时性能分析和优化建议
- 🎓 **教育资源**: 完善的教程和案例库

---

## 📞 支持与反馈

### 💬 社区交流

- **GitHub Issues**: [问题反馈](https://github.com/HuangYuChuh/ComfyUI-DeepSeek-Toolkit/issues)
- **GitHub Discussions**: [社区讨论](https://github.com/HuangYuChuh/ComfyUI-DeepSeek-Toolkit/discussions)

### 📧 联系方式

如有商务合作或其他询问，请通过以下方式联系：

- **项目维护者**: [@HuangYuChuh](https://github.com/HuangYuChuh)
- **项目主页**: [ComfyUI-DeepSeek-Toolkit](https://github.com/HuangYuChuh/ComfyUI-DeepSeek-Toolkit)

---

## 📄 开源协议

本项目采用 [GPL-2.0 License](https://github.com/HuangYuChuh/ComfyUI-DeepSeek-Toolkit/blob/main/LICENSE) 开源协议。

---

## 🙏 致谢

感谢以下项目和社区的支持：

- 🎨 [ComfyUI](https://github.com/comfyanonymous/ComfyUI) - 强大的AI工作流平台
- 🤖 [DeepSeek](https://www.deepseek.com/) - 优秀的大语言模型
- 🌟 [阿里云通义千问](https://tongyi.aliyun.com/) - 多模态AI助手
- 👥 所有贡献者和用户的支持与反馈

---

<div align="center">

**⭐ 如果这个项目对您有帮助，请给我们一个Star！**

[![Star History Chart](https://api.star-history.com/svg?repos=HuangYuChuh/ComfyUI-DeepSeek-Toolkit&type=Date)](https://star-history.com/#HuangYuChuh/ComfyUI-DeepSeek-Toolkit&Date)

</div>
