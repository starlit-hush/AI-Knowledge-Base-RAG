# 企业知识库智能问答系统(RAG)

## 项目介绍
基于RAG架构实现企业知识库智能问答系统。
系统支持对 PDF 文档进行解析、文本切分、向量化存储，通过语义检索获取相关知识片段，并结合大语言模型生成准确回答，实现企业内部知识的智能查询。

## 项目功能
- 支持 PDF 企业文档解析与内容提取
- 基于文本切分策略构建知识片段
- 使用 BGE Embedding 模型生成文本向量
- 使用 FAISS 构建本地向量数据库
- 基于语义相似度检索相关知识
- 调用大语言模型生成最终答案
- 使用 Gradio 搭建交互式 Web 问答界面

## 技术栈
- Python
- LangChain
- BGE Embedding
- FAISS
- Doubao API
- Gradio

## 系统架构
PDF文档
↓
文本解析(PDF Loader)
↓
文本切分(Text Splitter)
↓
Embedding模型向量化
↓
FAISS向量数据库
↓
相似度检索 Top-K
↓
Prompt构造
↓
LLM生成回答

## 项目结构
AI-Knowledge-Base-RAG
│
├── app.py              # Gradio应用入口
├── build_vector.py     # 构建向量数据库
├── chat_rag.py         # RAG问答流程
├── config.py           # 配置管理
│
├── utils
│   ├── pdf_loader.py
│   └── splitter.py
│
├── docs                # 知识库文档目录
│
├── requirements.txt
└── README.md


## 运行方式
1.安装依赖:
pip install -r requirements.txt

2.配置.env
API_KEY=your_api_key
ENDPOINT_ID=your_endpoint_id

3.构建知识库:
python build_vector.py

4.启动:
python app.py

## 项目效果
用户输入问题后，系统会根据知识库内容检索相关信息，并由大语言模型生成对应回答。

## 后续优化方向
	•	增加多轮对话能力
	•	引入 Rerank 模型提升检索准确率
	•	支持多格式文档解析（Word、Markdown等）
	•	增加用户权限管理和企业级部署能力
