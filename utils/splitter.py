from langchain_text_splitters import RecursiveCharacterTextSplitter     #导入文本分割工具

def split_text(text):

    spliter = RecursiveCharacterTextSplitter(
        chunk_size=500,      #每个文本块的最大长度:500
        chunk_overlap=50       #文本块之间的重叠长度:50
    )

    chunks = spliter.split_text(text)

    return chunks