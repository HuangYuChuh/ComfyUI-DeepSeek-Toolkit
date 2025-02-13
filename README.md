# ComfyUI-DeepSeek-Toolkit 技术文档

## 1. 项目介绍

ComfyUI-DeepSeek-Toolkit 是一个 ComfyUI 的自定义节点包，旨在帮助用户利用来自中国供应商的强大 AI 大语言模型 (LLM)，例如 DeepSeek、Qwen 等。该工具包致力于让更广泛的受众能够访问这些先进的模型，即使是那些计算资源有限的用户。

该项目的灵感来自于 DeepSeek 和 Qwen 等令人印象深刻的 LLM 的出现。它旨在通过提供轻量级和 API 驱动的解决方案，将这些前沿 AI 技术与日常用户连接起来，从而将这些模型集成到 ComfyUI 工作流程中。

ComfyUI-DeepSeek-Toolkit 的使命是使开发人员和创意人员能够在现成的硬件（如旧笔记本电脑）上完成通常需要大量计算能力的任务。该项目设想了一个 AI 民主化并为所有人所用的未来。

## 2. 功能特性

该工具包支持调用各种中国 AI 大语言模型，包括：

*   **DeepSeek**
*   **通义千问 (Qwen)**
*   **豆包 (Doubao)**
*   **星火 (Spark)**
*   **智谱清言 (GLM)**
*   **月之暗面 (Moonshot)**
*   **百川 (Baichuan)**
*   **MiniMax**
*   **阶跃星辰**

有关如何调用每个模型的详细说明，请参阅 [LLM API 调用指南（中国版）](https://github.com/HuangYuChuh/ComfyUI-DeepSeek-Toolkit/blob/main/LLM%20API%20%E8%B0%83%E7%94%A8%E6%8C%87%E5%8D%97%EF%BC%88%E4%B8%AD%E5%9B%BD%E7%89%88%EF%BC%89.md)。

该工具包包括以下模块：

*   **LLM 加载:** 用于加载和配置不同 LLM 的节点。
*   **图像生成:** 用于使用 LLM 生成图像的节点。
*   **图像理解:** 用于使用 LLM 分析和理解图像的节点。
*   **模型加载:** 用于加载不同任务所需的各种模型的节点。
*   **OpenAI 兼容加载:** 用于加载与 OpenAI API 兼容的模型的节点。
*   **图像预处理:** 用于在将图像馈送到 LLM 之前对其进行预处理的节点。

这些模块可以无缝集成到 ComfyUI 工作流程中，允许用户创建复杂且自定义的 AI 驱动应用程序。

## 3. 技术栈

*   **编程语言:** Python
*   **依赖项:**
    *   git+https://github.com/deepseek-ai/Janus.git
    *   torch
    *   numpy
    *   Pillow
    *   aiohttp
    *   transformers

该工具包采用以 API 为中心的方法与各种 LLM 进行交互。API 详细信息，包括基本 URL 和 API 密钥获取说明，请参阅 [LLM API 调用指南（中国版）](https://github.com/HuangYuChuh/ComfyUI-DeepSeek-Toolkit/blob/main/LLM%20API%20%E8%B0%83%E7%94%A8%E6%8C%87%E5%8D%97%EF%BC%88%E4%B8%AD%E5%9B%BD%E7%89%88%EF%BC%89.md)。

## 4. 目标受众

ComfyUI-DeepSeek-Toolkit 专为以下人员设计：

*   **ComfyUI 用户:** 那些希望将强大的 LLM 集成到其工作流程中的人。
*   **AI 开发人员:** 那些希望使用中国 LLM 试验和构建应用程序的人。
*   **研究人员:** 那些希望研究和分析不同 LLM 的功能的人。
*   **创意人员:** 那些希望使用 AI 来增强其创作过程的人。

该工具包适用于对 ComfyUI 和 Python 有基本了解的用户。熟悉 AI 概念和 LLM 会有所帮助，但不是必需的。

## 5. 下一步计划

项目路线图包括以下计划的功能和改进：

*   **扩展对更多 LLM 的支持:** 不断增加对新的和新兴的中国 LLM 的支持。
*   **优化性能:** 提高工具包的效率和速度。
*   **添加更多预构建的工作流程:** 为常见任务提供更多即用型工作流程。
*   **改进文档:** 创建更全面和用户友好的文档。
*   **添加更多图像处理节点:** 扩展工具包的图像处理能力。

## 6. 人文理念

ComfyUI-DeepSeek-Toolkit 的驱动力是 AI 民主化并使其为所有人所用的愿景。该项目旨在使开发人员和创意人员，特别是那些资源有限的人，能够利用 AI 的力量来创建创新的解决方案并表达他们的创造力。

该项目的人文理念植根于这样一种信念，即 AI 应该是一种赋权工具，而不是不平等的根源。通过提供轻量级且易于访问的解决方案，将强大的 LLM 集成到 ComfyUI 工作流程中，ComfyUI-DeepSeek-Toolkit 致力于使 AI 成为一种更具包容性和公平性的技术。
