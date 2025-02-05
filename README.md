# ComfyUI-DeepSeek_Toolkit

ComfyUI-DeepSeek_Toolkit是受到 DeepSeek 大模型爆发而来的灵感，既然如 DeepSeek 和 Qwen 这些国产大模型效果如此惊艳，为什么不能让更多人用最轻便的设备就能调用顶尖大模型。这个工具包没有复杂的架构，它只做两件事：把 DeepSeek、Qwen 等这些让我兴奋的大语言模型真正融进工作流，同时用 API 化的方式让每一台老旧的 MacBook/Windows 笔记本都能流畅运行。
或许有天某个刚入行的开发者，能用它在一台五年前的笔记本上实现原本需要服务器集群才能完成的事，那这个项目才算真正完成了使命。

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


## 贡献指南

欢迎提交 Pull Requests 或 Issues。在提交之前，请确保：

1. 代码符合 PEP 8 规范
2. 添加了适当的测试用例
3. 更新了相关文档
