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
#             deletar = ["id",pergunta","opcoes","correta"]
#             for item in deletar:
#                 del dados[deletar]
#                 return True
#         return False
            
    
def id_pergunta(dados):
    dados = load_questions()
    if not dados:
        return 1
    return max(p.get("id",0) for p in dados) +1
    



def mudar_perguntas(pergunta,indice,new_questions):
    with open (dados,"w",encoding="UTF-8") as f:
        if 0 <= indice <len(dados):
            dados[indice].update(new_questions)
            save_questions(pergunta)
            save_questions( dados)
            return True
        return False # n testado


def add_questions(pergunta,opcoes,correta):
        perguntas =load_questions()
        novo_id = id_pergunta(pergunta)

        new_questions ={
            "id" : novo_id,
            "pergunta": pergunta,
            "opcoes" : opcoes,
            "correta" : correta
        }
        perguntas.append(new_questions)
        save_questions(perguntas)# testado
        return novo_id


def mostrar():
    with open("questions.json","r",encoding="UTF-8") as f:
        perguntas = json.load(f)
        print(perguntas) #---> ok, aparece!




if __name__ == "__main__":
    add_questions("uma galinha pode virar galo?",["sim","n","noa sei"],0)
    mostrar()
