import os
from dashscope import Generation
import dashscope
dashscope.base_http_api_url = 'https://dashscope.aliyuncs.com/api/v1'
from config import API_KEY
from chunker import split_text



try:
    knowledge  = ""
    document = []

    for filename in os.listdir("knowledge"):
        if filename.endswith(".txt"):
            file_path = os.path.join("knowledge",filename)

            with open(file_path, "r", encoding="utf-8") as file:
                knowledge += file.read() + "\n"
                chunks = split_text(knowledge, chunk_size=1000, overlap=200)
                document.append({
                    "file_name":filename,
                    "chunks":chunks
                })
except FileNotFoundError:
    print("错误：找不到知识库文件")
    exit(1)
except UnicodeDecodeError:
    print("错误：无法解码知识库文件，请确保文件是UTF-8编码 ")
    exit(1)

question = input("请输入你的问题：")


prompt = f"""
请根据下面的知识库内容回答用户的问题。

知识库内容：
{document}

用户问题：
{question}

要求：
1. 优先根据知识库内容回答
2. 不要随意编造知识库中不存在的信息
3. 如果知识库中没有相关信息，请明确告诉用户
"""


messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt},
]

try:
    response = Generation.call(
        # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key = "sk-xxx",
        api_key=API_KEY,
        model="qwen3-max-2026-01-23",
        messages=messages,
        result_format="message",
        # 开启深度思考
        enable_thinking=True,
    )

    if response.status_code == 200:
        # 打印思考过程
        print("=" * 20 + "思考过程" + "=" * 20)
        if hasattr(response.output.choices[0].message, 'reasoning_content'):
            print(response.output.choices[0].message.reasoning_content)
        
        # 打印回复
        print("=" * 20 + "完整回复" + "=" * 20)
        print(response.output.choices[0].message.content)
    else:
        print(f"HTTP返回码：  {response.status_code}")
        print(f"错误码：{response.code}")
        print(f"错误信息：{response.message}")
except Exception as e:
    print(f"请求过程中发生错误：{str(e)}")