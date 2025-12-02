#primeiros testes do quiz logica...
import json
import os
questions = ["oi cara de boi"]
if os.path.exists("questions.json"):
    with open ("question.json","r",encoding="utf=8") as j:
        questions= json.load(j)
else:
    questions =[]


def load_questions():
    try:
        with open ("questions.json","r",encoding="UTF-8") as f:
            return json.load(f)
        print(questions)
    except FileNotFoundError:
        #messagebox.showerror("erro:","arquivo musicas.json não encontrado!!")
        return []
    except json.JSONDecodeError:
        #messagebox.showerror("erro,","ocorreu um erro ao ler o arquivo JSON")
        return []

def edit_questions (nova,novo_item):
    questions ={}
    nova = novo_item
    for chave, valor in novo_item.items():
        dados[chave] = valor

    

if __name__ == "__main__":
    load_questions()

      