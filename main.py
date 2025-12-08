import json
import os

dados = "questions.json"





    



def delete_questions (dados,id_delete):
    id_delete =int(id_delete)
    for item in dados:
        if int(item("id",0)) == id_delete:
            dados.remove(item)
            return True
    return False
            
 
    



    


def changue_questions(indice,pergunta,new_question):
    with open (dados,"w",encoding="UTF-8") as f:
        indice= dados["id"]
        for indice in dados:
            pass





#tudo abaixo funciona




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
    #add_questions("qual o pais mais perto do polo norte?",["russia","greenland","Canada"],2)
   perguntas = load_questions()
   if delete_questions(perguntas,2):
       save_questions()
   else:
       print("id n achado")
       