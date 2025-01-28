# ComfyUI DeepSeek Janus Pro 中文说明

## 项目概述
本自定义节点为ComfyUI提供了DeepSeek Janus Pro多模态AI模型的支持，包含以下主要功能：
- 图像理解与分析
- 文生图生成
- 多模态处理能力

## 主要特点
- 支持本地和远程模型加载
- 自动设备选择（CPU/GPU）
- 批量图像生成
- 灵活的参数配置
- 完整的错误处理机制

## 安装步骤

### 前置条件
- 已安装ComfyUI
- Python 3.8+
- CUDA支持的GPU（推荐）

### 安装流程
1. 克隆项目到ComfyUI的custom_nodes目录：
```bash
cd custom_nodes
git clone https://github.com/yourusername/ComfyUI-DeepSeek_Janus.git
```

2. 安装依赖：
```bash
cd ComfyUI-DeepSeek_Janus
pip install -r requirements.txt
```

3. 下载DeepSeek Janus Pro模型：
- 将模型放置在`ComfyUI/models/deepseek_janus/`目录下

4. 重启ComfyUI即可使用新节点

## 节点说明

### 1. DeepSeek 模型加载器
- 加载DeepSeek Janus Pro模型
- 支持本地和远程模型
- 自动选择最佳精度（FP16/BF16）

参数说明：
- model_name: 模型名称
- use_local: 是否使用本地模型

### 2. 图像理解
- 分析图像内容
- 支持自定义问题
- 多模态理解能力

参数说明：
- image: 输入图像
- question: 提问内容
- max_length: 最大输出长度

### 3. 图像生成
- 根据文本生成图像
- 可配置生成参数
- 支持批量生成

参数说明：
- prompt: 文本提示
- batch_size: 批量大小
- temperature: 采样温度
- guidance_scale: 引导强度
- max_length: 最大序列长度

## 使用示例

### 图像理解
1. 加载模型
2. 连接图像输入
3. 输入问题
4. 获取分析结果

### 图像生成
1. 加载模型
2. 输入文本提示
3. 配置生成参数
4. 生成图像

## 注意事项
- 确保CUDA正确安装
- 检查模型下载和放置位置
- 验证依赖项是否正确安装

## 常见问题
Q: 模型加载失败怎么办？
A: 
1. 检查模型路径是否正确
2. 确认requirements.txt中的依赖已安装
3. 查看日志文件获取详细错误信息

Q: 图像生成质量不佳？
A:
1. 调整temperature参数
2. 修改guidance_scale值
3. 尝试不同的prompt描述

## 版本支持
- Janus Pro 1B
- Janus Pro 7B

## 贡献指南
欢迎提交PR或报告问题：
- 请确保代码符合PEP8规范
- 添加必要的单元测试
- 更新相关文档

## 致谢
- DeepSeek AI团队
- ComfyUI社区