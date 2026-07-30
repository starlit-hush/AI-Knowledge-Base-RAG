from sentence_transformers import SentenceTransformer
import faiss
import pickle

from utils.pdf_loader import load_pdf
from utils.splitter import split_text
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import EMBEDDING_MODEL

# 1.读取PDF
text = load_pdf("docs/test.pdf")

chunks = split_text(text)

# 3.加载Embedding模型
model = SentenceTransformer(        #为embedding模型，可以把文字变成向量
   EMBEDDING_MODEL
)

# 4.文本转向量
vectors = model.encode(chunks)

print("文本数量：", len(chunks))
print("向量维度：", vectors.shape)

# 5.创建FAISS数据库
dimension = vectors.shape[1]

index = faiss.IndexFlatL2(dimension)        #用FALSS搜索，快速寻找最相似的文本

# 添加向量
index.add(vectors)


# 保存数据库
faiss.write_index(
    index,
    "knowledge.faiss"
)

# 保存文本
with open(
    "chunks.pkl",
    "wb"
) as f:
    pickle.dump(chunks,f)

print("向量数据库创建完成")