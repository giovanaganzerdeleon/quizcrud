import json
import os

dados = "questions.json"


def load_questions():
    if os.path.exists(dados):
        try:
            with open(dados, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return [] #-- n testado
    



def save_questions(perguntas):
    with open(dados,"w",encoding="UTF-8") as f:
        json.dump(perguntas,f,ensure_ascii=False,indent=4) #--- n testado
    




def delete_questions(pergunta,indice):
    with open ("questions.json","w",encoding="UTF-8") as f:
        if 0 <= indice <len(dados):
            pass
            
    




def mudar_perguntas(pergunta,indice,new_questions):
    with open (dados,"w",encoding="UTF-8") as f:
        if 0 <= indice <len(dados):
            dados[indice].update(new_questions)
            save_questions(pergunta)
            return True
        return False # n testado


def add_questions(pergunta,opcoes,correta):
        perguntas =load_questions()
        new_questions ={
            "pergunta": pergunta,
            "opcoes" : opcoes,
            "correta" : correta
        }
        perguntas.append(new_questions)
        save_questions(perguntas)


def mostrar():
    with open("questions.json","r",encoding="UTF-8") as f:
        perguntas = json.load(f)
        print(perguntas) #---> ok, aparece!




if __name__ == "__main__":
    add_questions("teste de sorte",["1,5,9"],2)
    mostrar()