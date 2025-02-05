# ComfyUI-DeepSeek_Toolkit

ComfyUI-DeepSeek_Toolkit是受到 DeepSeek 大模型爆发而来的灵感，既然如 DeepSeek 和 Qwen 这些国产大模型效果如此惊艳，为什么不能让更多人用最轻便的设备就能调用顶尖大模型。这个工具包没有复杂的架构，它只做两件事：把 DeepSeek、Qwen 等这些让我兴奋的大语言模型真正融进工作流，同时用 API 化的方式让每一台老旧的 MacBook/Windows 笔记本都能流畅运行。

## 功能特性

- **图像生成 (Image Generation)**
  - 支持使用 DeepSeek Janus Pro 模型进行图像生成
  - 可调节的参数包括：batch size、temperature、guidance scale 等
  - 支持正向提示词和负向提示词
 

- **图像理解 (Image Understanding)**
  - 基于 DeepSeek Janus 模型的图像理解功能
  - 支持图像问答和描述生成
  - 多模态交互支持

- **文本生成 (Text Generation)**
  - 集成多个 LLM 服务（如 Moonshot、DeepSeek、Spark 等）
  - 支持动态选择模型和 API 配置

## 系统要求

- Python 3.8+
- PyTorch 1.10+（推荐使用 CUDA 支持的版本）
- ComfyUI
- 足够的 GPU 内存（默认使用设备内存的 90%，可通过 `max_memory` 参数调整）

## 安装说明

1. 确保已安装 ComfyUI
2. 克隆本仓库到 ComfyUI 的 custom_nodes 目录：
   ```bash
   cd custom_nodes
   git clone https://github.com/your-username/ComfyUI-DeepSeek_Toolkit.git
   ```
3. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
4. 配置环境变量（可选）：
   - 设置 `CUDA_VISIBLE_DEVICES` 以指定 GPU 设备
   - 设置 `PYTORCH_CUDA_ALLOC_CONF` 以优化内存分配

## 使用方法

### 图像生成

1. 在 ComfyUI 工作流中添加 "DeepSeek Image Generation Pro" 节点
2. 配置以下参数：
   - Model: DeepSeek 模型实例
   - Tokenizer: DeepSeek tokenizer 实例
   - Prompt: 生成图像的文本描述
   - Batch Size: 生成图像的数量（1-16）
   - Temperature: 采样温度（0.1-2.0）
   - Guidance Scale: 引导比例（1.0-20.0）
   - Max Length: 最大序列长度（1-256）
   - Image Size: 输出图像尺寸（256-1024）
   - Negative Prompt（可选）: 负面提示词

### 图像理解

1. 在 ComfyUI 工作流中添加 "DeepSeek Image Understanding" 节点
2. 配置以下参数：
   - Model: DeepSeek 模型实例
   - Tokenizer: DeepSeek tokenizer 实例
   - Image: 输入图像
   - Question: 关于图像的问题或描述要求

### 文本生成

1. 在 ComfyUI 工作流中添加 "OpenAI Compatible Adapter" 节点
2. 配置以下参数：
   - Base URL: 选择的服务提供商（如 Moonshot、DeepSeek 等）
   - API Key: 对应服务的 API 密钥
   - Prompt: 输入的文本提示
   - Model: 选择的模型名称
   - Temperature: 采样温度
   - Max Tokens: 最大生成 token 数量

## 注意事项

1. 内存使用：
   - 默认使用 GPU 设备内存的 90%用于存储模型
   - 剩余 10% 用作缓冲区以避免 OOM
   - 可以通过设置 `max_memory` 参数来调整内存使用（需谨慎使用）

2. 已知问题：
   - MultiModalityCausalLM 模型类需要特殊处理语言模型头部
   - 某些处理器配置参数可能不会生效（包括：image_tag, mask_prompt, ignore_id, sft_format, num_image_tokens, add_special_token）

## 贡献指南

欢迎提交 Pull Requests 或 Issues。在提交之前，请确保：

1. 代码符合 PEP 8 规范
2. 添加了适当的测试用例
3. 更新了相关文档

## 许可证

本项目采用 MIT 许可证。详情请参见 [LICENSE](LICENSE) 文件。
