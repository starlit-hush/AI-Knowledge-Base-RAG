from pypdf import PdfReader     #导入pdf工具

def load_pdf(file_path):

    reader = PdfReader(file_path)       #打开pdf

    text = ""

    for page in reader.pages:       #获取页面（逐页读取）
        text += page.extract_text()     #提取文字

    return text