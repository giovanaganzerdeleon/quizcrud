import json
import os

perguntas = "questions.json"


def load_questions():
    if os.path.exists(perguntas):
        try:
            with open(perguntas, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []


def save_questions(pergunta):
    with open(perguntas,"w",encoding="UTF-8") as f:
        json.dump(perguntas,f,ensure_ascii=False,indent=4)
    