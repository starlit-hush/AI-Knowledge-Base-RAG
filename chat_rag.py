import faiss
import pickle
from config import API_KEY, ENDPOINT_ID
from sentence_transformers import SentenceTransformer
from openai import OpenAI
from config import EMBEDDING_MODEL

#加载FAISS
index = faiss.read_index(
    "knowledge.faiss"
)


#加载文本块
with open(
    "chunks.pkl",
    "rb"
) as f:
    chunks = pickle.load(f)


#加载Embedding模型
model = SentenceTransformer(
    EMBEDDING_MODEL
)

#连接豆包API
client = OpenAI(
    base_url="https://ark.cn-beijing.volces.com/api/v3",
    api_key=API_KEY
)

def ask(question):

    # 问题转向量
    question_vector = model.encode(
        [question]
    )

    # 搜索最相似文本

    distance, indexes = index.search(
        question_vector,
        k=3
    )

    # 获取相关内容
    context = ""

    for i in indexes[0]:
        context += chunks[i] + "\n"


    #调用豆包
    response = client.responses.create(
        model=ENDPOINT_ID,
        input=f"""
你是一个知识库助手。

请根据下面资料回答问题。

资料：
{context}

问题：
{question}
"""
    )


    return response.output_text