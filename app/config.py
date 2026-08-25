import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("DASHSCOPE_API_KEY")
if not API_KEY:
    raise RuntimeError("未找到 DASHSCOPE_API_KEY，请检查项目根目录的 .env 文件")
