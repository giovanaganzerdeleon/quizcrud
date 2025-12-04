import json
import os

dados = "questions.json"






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
    

# def delete_questions(dados,indice):
#         dados = load_questions()
#         if 0 <= indice <len(dados):
#             deletar = ["pergunta"[0],"opcoes"[1],"correta"[2]]
#             for item in deletar:
#                 del dados[deletar]
#                 return True
#         return False
            
    
def id_pergunta(dados):
    dados = load_questions()
    if not dados:
        novo_id = 1
    else:
        ultimo_id = [item.get("id",0)for item in dados if isinstance(item,dict)]
        novo_id = max(ultimo_id) +1
   



def mudar_perguntas(pergunta,indice,new_questions):
    with open (dados,"w",encoding="UTF-8") as f:
        if 0 <= indice <len(dados):
            dados[indice].update(new_questions)
            save_questions(pergunta)
            save_questions( dados)
            return True
        return False # n testado


def add_questions(id,pergunta,opcoes,correta):
        perguntas =load_questions()
        novo_id = id_pergunta(dados)
        new_questions ={
            "id" : novo_id,
            "pergunta": pergunta,
            "opcoes" : opcoes,
            "correta" : correta
        }
        perguntas.append(new_questions)
        save_questions(perguntas)# testado


def mostrar():
    with open("questions.json","r",encoding="UTF-8") as f:
        perguntas = json.load(f)
        print(perguntas) #---> ok, aparece!




if __name__ == "__main__":
    add_questions("oq e um zangao?",["uma abelha que n recebeu mel","um outro tipo de abelha","um besouro"],0)
    mostrar()
