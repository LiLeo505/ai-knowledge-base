from fastapi import FastAPI
from rag import ask

from pydantic import BaseModel

app = FastAPI()
  

class Question(BaseModel):
    question: str

@app.get("/")
def home():

    return {
        "message": "AI知识库运行成功"

    }

@app.post("/ask")
def ask_question(data:Question):

    answer = ask(data.question)

    return {
        "question": data.question,
        "answer": answer
    }