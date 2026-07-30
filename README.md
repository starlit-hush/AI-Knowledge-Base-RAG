# 企业知识库智能问答系统

## 项目介绍
基于RAG架构实现企业知识库问答系统。
支持PDF文档解析、文本切分、Embedding向量检索，并结合大语言模型生成答案。

## 技术栈
- Python
- LangChain
- BGE Embedding
- FAISS
- Doubao API
- Gradio

## 系统架构
PDF
↓
文本切分
↓
Embedding
↓
FAISS
↓
检索
↓
LLM生成回答


## 运行方式
安装依赖:
pip install -r requirements.txt

配置.env

构建知识库:
python build_vector.py

启动:
python app.py