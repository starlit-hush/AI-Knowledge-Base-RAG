import gradio as gr
from chat_rag import ask
from config import API_KEY, ENDPOINT_ID


demo = gr.Interface(     #创建网络接口
    fn=ask,

    inputs=gr.Textbox(
        label="请输入问题："
    ),      #用户输入文本
    outputs=gr.Textbox(
        label="AI回答："
    ),      #显示文本答案
    title="企业知识库AI助手"    #显示文本答案
)  

demo.launch(
    server_name="127.0.0.1"
)   #打开网页