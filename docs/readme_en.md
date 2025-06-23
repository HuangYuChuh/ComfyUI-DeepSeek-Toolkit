# ComfyUI-DeepSeek-Toolkit Technical Documentation

## 1. Project Introduction

ComfyUI-DeepSeek-Toolkit is a custom node package for ComfyUI that enables users to leverage powerful AI large language models (LLMs) from various Chinese providers, such as DeepSeek, Qwen, and others. The toolkit aims to make these advanced models accessible to a wider audience, even those with limited computational resources.

The project was inspired by the emergence of impressive LLMs like DeepSeek and Qwen. It seeks to bridge the gap between cutting-edge AI technology and everyday users by providing a lightweight and API-driven solution for integrating these models into ComfyUI workflows.

The mission of ComfyUI-DeepSeek-Toolkit is to empower developers and creatives to accomplish tasks that would typically require significant computational power on readily available hardware, such as older laptops. The project envisions a future where AI is democratized and accessible to all.

## 2. Functionality

This toolkit supports calling a diverse range of Chinese AI large language models, including:

*   **DeepSeek**
*   **通义千问 (Qwen)**
*   **豆包 (Doubao)**
*   **星火 (Spark)**
*   **智谱清言 (GLM)**
*   **月之暗面 (Moonshot)**
*   **百川 (Baichuan)**
*   **MiniMax**
*   **阶跃星辰**

For detailed instructions on how to call each model, please refer to the [LLM API 调用指南（中国版）](https://github.com/HuangYuChuh/ComfyUI-DeepSeek-Toolkit/blob/main/LLM%20API%20%E8%B0%83%E7%94%A8%E6%8C%87%E5%8D%97%EF%BC%88%E4%B8%AD%E5%9B%BD%E7%89%88%EF%BC%89.md).

The toolkit includes modules for:

*   **LLM Loading:** Nodes for loading and configuring different LLMs.
*   **Image Generation:** Nodes for generating images using LLMs.
*   **Image Understanding:** Nodes for analyzing and understanding images using LLMs.
*   **Model Loading:** Nodes for loading various models required for different tasks.
*   **OpenAI Compatible Loading:** Nodes for loading models compatible with the OpenAI API.
*   **Image Preprocessing:** Nodes for preprocessing images before feeding them into LLMs.

These modules can be seamlessly integrated into ComfyUI workflows, allowing users to create complex and customized AI-powered applications.

## 3. Technical Stack

*   **Programming Language:** Python
*   **Dependencies:**
    *   git+https://github.com/deepseek-ai/Janus.git
    *   torch
    *   numpy
    *   Pillow
    *   aiohttp
    *   transformers

The toolkit utilizes an API-centric approach to interact with the various LLMs. The API details, including base URLs and API key acquisition instructions, can be found in the [LLM API 调用指南（中国版）](https://github.com/HuangYuChuh/ComfyUI-DeepSeek-Toolkit/blob/main/LLM%20API%20%E8%B0%83%E7%94%A8%E6%8C%87%E5%8D%97%EF%BC%88%E4%B8%AD%E5%9B%BD%E7%89%88%EF%BC%89.md).

## 4. Target Audience

ComfyUI-DeepSeek-Toolkit is designed for:

*   **ComfyUI users:** Those who want to integrate powerful LLMs into their workflows.
*   **AI developers:** Those who want to experiment with and build applications using Chinese LLMs.
*   **Researchers:** Those who want to study and analyze the capabilities of different LLMs.
*   **Creatives:** Those who want to use AI to enhance their creative process.

The toolkit is suitable for users with a basic understanding of ComfyUI and Python. Familiarity with AI concepts and LLMs is helpful but not required.

## 5. Next Steps

The project roadmap includes the following planned features and improvements:

*   **Expanding support for more LLMs:** Continuously adding support for new and emerging Chinese LLMs.
*   **Optimizing performance:** Improving the efficiency and speed of the toolkit.
*   **Adding more pre-built workflows:** Providing more ready-to-use workflows for common tasks.
*   **Improving documentation:** Creating more comprehensive and user-friendly documentation.
*   **Adding more image processing nodes:** Expanding the image processing capabilities of the toolkit.

## 6. Humanistic Conception

ComfyUI-DeepSeek-Toolkit is driven by a vision of democratizing AI and making it accessible to everyone. The project aims to empower developers and creatives, especially those with limited resources, to leverage the power of AI to create innovative solutions and express their creativity.

The project's humanistic conception is rooted in the belief that AI should be a tool for empowerment, not a source of inequality. By providing a lightweight and accessible solution for integrating powerful LLMs into ComfyUI workflows, ComfyUI-DeepSeek-Toolkit strives to make AI a more inclusive and equitable technology.