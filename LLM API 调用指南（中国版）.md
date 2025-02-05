# 1. Qwen/通义千问
- **官方文档**：https://help.aliyun.com/zh/model-studio/getting-started/what-is-model-studio?spm=a2c4g.11186623.help-menu-2400256.d_0_0.58b91d1cyMbRCF&scm=20140722.H_2579562._.OR_help-T_cn~zh-V_1
- **可调用模型**：（每一个系列下有很多不同权重的模型，模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models?spm=a2c4g.11186623.0.0.3fd248237PxAvQ#9f8890ce29g5u）
  - **「通义千问-Max」**：通义千问系列效果最好的模型，适合复杂、多步骤的任务。（`qwen-max`、`qwen-max-latest`、`qwen-max-2025-01-25`、`qwen-max-2024-09-19`、`qwen-max-2024-04-28`、`qwen-max-2024-04-03`、`qwen-max-2024-01-07`）
  - **「通义千问-Plus」**：能力均衡，推理效果、成本和速度介于通义千问-Max和通义千问-Turbo之间，适合中等复杂任务。（`qwen-plus`、`qwen-plus-latest`、`qwen-plus-2025-01-12`、`qwen-plus-2024-12-20`、`qwen-plus-2024-11-27`、`qwen-plus-2024-11-25`、`qwen-plus-2024-09-19`、`qwen-plus-2024-08-06`、`qwen-plus-2024-07-23`、`qwen-plus-2024-06-24`、`qwen-plus-2024-02-06`）
  - **「通义千问-Turbo」**：通义千问系列速度最快、成本极低的模型，适合简单任务。（`qwen-turbo、qwen-turbo-latest`、`qwen-turbo-2024-11-01`、`qwen-turbo-2024-09-19`、`qwen-turbo-2024-06-24`、`qwen-turbo-2024-02-06`）
  - **「Qwen-Long」**：通义千问系列上下文窗口最长，能力均衡且成本较低的模型，适合长文本分析、信息抽取、总结摘要和分类打标等任务。（qwen-long）
  - **「通义千问 VL」**：通义千问VL是具有视觉（图像）理解能力的文本生成模型，不仅能进行OCR（图片文字识别），还能进一步总结和推理，例如从商品照片中提取属性，根据习题图进行解题等。（`qwen-vl-max`、`qwen-vl-max-latest`、`qwen-vl-max-2024-12-30`、`qwen-vl-max-2024-11-19`、`qwen-vl-max-2024-10-30`、`qwen-vl-max-2024-08-09`、`qwen-vl-max-2024-02-01`、`qwen-vl-plus`、`qwen-vl-plus-latest`、`qwen-vl-plus-2025-01-02`、`qwen-vl-plus-2024-08-09`、`qwen-vl-plus-2023-12-01`）
  - **「通义千问 OCR」**：通义千问OCR模型是专用于文字提取的模型。相较于通义千问VL模型，它更专注于文档、表格、试题、手写体文字等类型图像的文字提取能力。它能够识别多种语言，包括英语、法语、日语、韩语、德语、俄语和意大利语等。（`qwen-vl-ocr`、`qwen-vl-ocr-latest`、`qwen-vl-ocr-2024-10-28`）
- **Base url**：https://dashscope.aliyuncs.com/compatible-mode/v1
- **API KEY获取**：https://bailian.console.aliyun.com/?apiKey=1#/api-key
- **价格**：https://help.aliyun.com/zh/model-studio/getting-started/models?spm=a2c4g.11186623.0.0.28722918BtgtOs#cf6cc4aa2aokf

# 2. DouBao/豆包
- **官方文档**：https://www.volcengine.com/docs/82379
- **可调用模型**：
  - **「Doubao-1.5-pro」**：最新一代专业版大模型，单价不提升的同时，模型能力有大幅提升，在知识（MMLU_PRO：80.2； GPQA：66.2）、代码（FullStackBench：65.1）、推理（DROP：92.6）、中文（C-Eval：91.5）等相关的多项测评中获得高分，达到行业SOTA水平。（Doubao-1.5-pro-32k、Doubao-1.5-pro-256k）
  - **「Doubao-1.5-lite」**：最新一代轻量版大模型，单价不提升的同时，模型能力有大幅提升，模型效果比肩专业版模型Doubao-pro-32k-0828，您享受轻量版模型的成本和性能，获得过去专业版模型的效果。（Doubao-1.5-lite-32k）
  - **「Doubao-1.5-vision」**：最新一代视觉理解模型，在单价不提升的同时，在多模态数据合成、动态分辨率、多模态对齐、混合训练上进行了全面的技术升级，进一步增强了模型在视觉推理、文字文档识别、细粒度信息理解、指令遵循方面的能力，并让模型的回复模式变得更加精简、友好。（Doubao-1.5-vision-pro-32k）
  - **「Doubao-pro」**：行业领先的专业版大模型，在参考问答、摘要总结、创作等广泛的应用场景上能提供优质的回答，是同时具备高质量与低成本的极具性价比模型。（Doubao-pro-4k、Doubao-pro-32k、Doubao-pro-128k、Doubao-pro-256k）
  - **「Doubao-lite」**：轻量级大模型，具备极致的响应速度，适用于对时延有更高要求的场景，模型配合精调使用可以获得更优质的效果。（Doubao-lite-4k、Doubao-lite-32k、Doubao-lite-128k）
- **备注**：豆包不是直接填写Model名称进行调用，而是通过推理点ID进行调用，推理点获取地址：https://console.volcengine.com/ark/region:ark+cn-beijing/endpoint?config=%7B%7D 
- **Base url**：https://ark.cn-beijing.volces.com/api/v3
- **API KEY获取**：https://console.volcengine.com/ark/region:ark+cn-beijing/apiKey?apikey=%7B%7D
- **价格**：https://www.volcengine.com/docs/82379/1099320

# 3. DeepSeek-V3/深度求索
- **官方文档**：https://platform.deepseek.com/api-docs/zh-cn/
- **可调用模型**：
  - 「deepseek-reasoner」
  - 「deepseek-chat」
- **Base url**：https://api.deepseek.com/v1
- **API KEY获取**：https://platform.deepseek.com/api_keys
- **价格**：https://platform.deepseek.com/api-docs/zh-cn/pricing
---
# 4. spark/星火
- **官方文档**：https://www.xfyun.cn/doc/spark/Web.html
- **可调用模型**：（https://www.xfyun.cn/doc/spark/HTTP%E8%B0%83%E7%94%A8%E6%96%87%E6%A1%A3.html#_3-%E8%AF%B7%E6%B1%82%E8%AF%B4%E6%98%8E）
    - **「`Lite`」**：轻量级大语言模型，低延迟，全免费。支持在线联网搜索功能，响应快速、便捷，全面免费开放，适用于低算力推理与模型精调等定制化场景。
  - **「`pro-128k`」**：专业级大语言模型，兼顾模型效果与性能。数学、代码、医疗、教育等场景专项优化，支持联网搜索、天气、日期等多个内置插件，覆盖大部分知识问答、语言理解、文本创作等多个场景。
  - **「`max-32k`」**：最全面的星火大模型版本，功能丰富。基于最新版星火大模型引擎4.0 Turbo 量化而来，支持联网搜索、天气、日期等多个内置插件，核心能力全面升级，各场景应用效果普遍提升，支持System角色人设与FunctionCall函数调用。
  - **「`4.0Ultra`」**：最强大的星火大模型版本，效果极佳。升级为最新版星火大模型引擎：星火4.0 Turbo，全方位提升效果，引领智能巅峰，优化联网搜索链路，提供精准回答，强化文本总结能力，提升办公生产力
- **Base url**：https://spark-api-open.xf-yun.com/v1
- **API KEY获取**：
  - 先创建应用：https://console.xfyun.cn/app/myapp
  - 再获取key：https://console.xfyun.cn/services/cbm
- **价格**：https://xinghuo.xfyun.cn/sparkapi

# 5. GLM/智谱清言
- **官方文档**：https://bigmodel.cn/dev/api
- **可调用模型**：
  - **「GLM-4系列」**：GLM-4 系列提供了复杂推理、超长上下文、极快推理速度等多款模型，适用于多种应用场景。（`glm-4-plus`、`glm-4-air`、`glm-4-air-0111 Preview`、`glm-4-airx`、 `glm-4-long`、`glm-4-flashx`、`glm-4-flash`）
  - **「GLM-4V系列」**：GLM-4 系列提供了多图理解、视频理解、单图理解度等多款模型，适用于多种应用场景。（`glm-4v-plus-0111beta`、`glm-4v-plus`、`glm-4v`、`glm-4v-flash`）
  - **「GLM-Zero-Preview」**：GLM-Zero-Preview具备强大的复杂推理能力，在逻辑推理、数学、编程等领域表现优异。最大上下文长度为16K。(`glm-zero-preview`)
- **Base url**：https://open.bigmodel.cn/api/paas/v4 
- **API KEY获取**：https://bigmodel.cn/usercenter/apikeys
- **价格**：https://open.bigmodel.cn/pricing

# 6. MiniMax/MiniMax
- **官方文档**：https://platform.minimaxi.com/document/notice
- **可调用模型**：
  - 基于MiniMax端到端自研多模态大语言模型，我们为企业用户或企业开发者提供功能丰富的API，适用于大多数文本处理场景。以自然语言交互的形式帮助企业用户或个人开发者提高文本相关的生产效率，例如：文本续写、文案生成、文本扩写、文本改写、内容摘要、代码生成、知识检索等。（ `MiniMax-Text-01`、`abab6.5s-chat`）
- **Base url**：https://api.minimax.chat/v1
- **API KEY获取**：https://platform.minimaxi.com/user-center/basic-information/interface-key
- **价格**：https://platform.minimaxi.com/document/Price?key=66701c7e1d57f38758d5818c

# 7. Moonshot/月之暗面
- **官方文档**：https://platform.moonshot.cn/docs
- **可调用模型**：
  - **chat**：（`moonshot-v1-auto`、`moonshot-v1-8k`、`moonshot-v1-32k`、`moonshot-v1-128k`）
  - **vision**：能够理解图片内容，包括图片文字、图片颜色和物体形状等内容。（`moonshot-v1-8k-vision-preview`、`moonshot-v1-32k-vision-preview`、`moonshot-v1-128k-vision-preview`）
- **Base url**：https://api.moonshot.cn/v1
- **API KEY获取**：https://platform.moonshot.cn/console/api-keys
- **价格**：https://platform.moonshot.cn/docs/price/chat

# 8. Baichuan/百川智能
- **官方文档**：https://platform.baichuan-ai.com/docs/api
- **可调用模型**：
  - Baichuan4-Turbo
  - Baichuan4-Air
  - Baichuan4
  - Baichuan3-Turbo
  - Baichuan3-Turbo-128k
  - Baichuan2-Turbo
- **Base url**：https://api.baichuan-ai.com/v1
- **API KEY获取**：https://platform.baichuan-ai.com/console/apikey
- **价格**：https://platform.baichuan-ai.com/price
