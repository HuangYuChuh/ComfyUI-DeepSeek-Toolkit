# ComfyUI-DeepSeek_Toolkit

ComfyUI-DeepSeek_Toolkit是受到 DeepSeek 大模型爆发而来的灵感，既然如 DeepSeek 和 Qwen 这些国产大模型效果如此惊艳，为什么不能让更多人用最轻便的设备就能调用顶尖大模型。这个工具包没有复杂的架构，它只做两件事：把 DeepSeek、Qwen 等这些让我兴奋的大语言模型真正融进工作流，同时用 API 化的方式让每一台老旧的 MacBook/Windows 笔记本都能流畅运行。
或许有天某个刚入行的开发者，能用它在一台五年前的笔记本上实现原本需要服务器集群才能完成的事，那这个项目才算真正完成了使命。

## 👋 项目介绍
- 支持调用 9 家国产 AI 大语言模型（DeepSeek、通义千问、豆包、星火、智谱清言、月之暗面、百川、MiniMax、阶跃星辰），调用文档如下：[LLM API 调用指南（中国版）](https://github.com/HuangYuChuh/ComfyUI-DeepSeek-Toolkit/blob/main/LLM%20API%20%E8%B0%83%E7%94%A8%E6%8C%87%E5%8D%97%EF%BC%88%E4%B8%AD%E5%9B%BD%E7%89%88%EF%BC%89.md)

## 🛠️ 安装说明

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
