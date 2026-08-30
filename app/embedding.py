import dashscope
from config import API_KEY

dashscope.base_http_api_url = 'https://dashscope.aliyuncs.com/api/v1'

def get_embedding(text: str) -> list[float]:
    response = dashscope.TextEmbedding.call(
        model='text-embedding-v2',
        input=text,
        api_key=API_KEY
    )
    if response.status_code != 200:
        raise RuntimeError(f"调用失败：{response.code} {response.message}")
    return response.output['embeddings'][0]['embedding']

