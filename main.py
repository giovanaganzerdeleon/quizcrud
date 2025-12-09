import json
import os

dados = "questions.json"

def delete_question(id_question):
    perguntas = load_questions()

    nova_lista = [p for p in perguntas if p["id"] != id_question]

    if len(nova_lista) == len(perguntas):
        return False 

    save_questions(nova_lista)
    return True



def update_question(id_question, novos_campos: dict):
    perguntas = load_questions()

    for item in perguntas:
        if item["id"] == id_question:
            item.update(novos_campos)
            save_questions(perguntas)
            return True
    return False   # passar como um dicionario (igual o arquivo json)




def save_questions(perguntas):
    with open(dados,"w",encoding="UTF-8") as f:
        json.dump(perguntas,f,ensure_ascii=False,indent=4) #--- testado e aprovado!
    


def load_questions():
    if os.path.exists(dados):
        try:
            with open(dados, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return [] #--testado e aprovado!


def id_questions(dados):
    dados = load_questions()
    if not dados:
        return 1
    return max(p.get(int("id",0))for p in dados) +1 #testado e aprovado!


def add_questions(pergunta,opcoes,correta):
        perguntas =load_questions()
        new_id = id_questions(pergunta)

        new_questions ={
            "id" : new_id,
            "pergunta": pergunta,
            "opcoes" : opcoes,
            "correta" : correta
        }
        perguntas.append(new_questions)
        save_questions(perguntas)# testado | passar as opcoes como lista (passar as respostas com o nome certo)
        return new_id


def mostrar():
    with open("questions.json","r",encoding="UTF-8") as f:
        perguntas = json.load(f)
        print(perguntas) #---> ok, aparece!



if __name__ == "__main__":
    update_question(1,{"pergunta":"teste de sorte","opcoes":["1","4","6"],"correta":2})