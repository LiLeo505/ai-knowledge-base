from dashscope import Generation
import dashscope
dashscope.base_http_api_url = 'https://dashscope.aliyuncs.com/api/v1'
from config import API_KEY
from vector_db import search
import chromadb


def ask(question):
    client = chromadb.PersistentClient(path="./chromadb")

    collection = client.get_collection(name="knowledge")

    print("连接知识库成功")

    results = search(question, n_results=3)

    context = results["documents"][0]



    prompt = f"""
请根据下面的知识库内容回答用户的问题。

知识库内容：
{context}

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
        responses = Generation.call(
            api_key=API_KEY,
            model="qwen3-max-2026-01-23",
            messages=messages,
            result_format="message",
            # 开启深度思考（Qwen3 思考模式必须使用流式调用）
            enable_thinking=True,
            incremental_output=True,
            stream=True,
        )

        print("=" * 20 + "思考过程" + "=" * 20)
        print("=" * 20 + "完整回复" + "=" * 20)
        for response in responses:
            if response.status_code == 200:
                message = response.output.choices[0].message
                reasoning = getattr(message, "reasoning_content", None)
                if reasoning:
                    print(reasoning, end="")
                elif message.content:
                    print(message.content, end="", flush=True)
            else:
                print(f"\nHTTP返回码：  {response.status_code}")
                print(f"错误码：{response.code}")
                print(f"错误信息：{response.message}")
                break
        print()
    except Exception as e:
        print(f"请求过程中发生错误：{str(e)}")
