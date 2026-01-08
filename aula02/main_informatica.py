from llm import chama_llm

def build_prompt_beginner(situation):
    question = f""""

    Você é um assitente de informática muito paciente. 

    Explique a situação abaixo como se o usuario não tivesse nenhuma experiencia com informatica.
    Use linguagem simples e exemplos de como resolver.

    Situação: {situation}
"""
    return question


def build_prompt_advanced(situation):
    question = f""""

    Você é um assistente de informatica muito experiente. 

    Explique a situação abaixo como se o usuario ja fosse familiarizado com linguagens mais técnicas.
    Use dicas mais práticas e avançadas.

    Situação: {situation}
"""
    return question


def build_prompt_very_reliable(situation):
    question = f""""

    Você é um assistente de informatica que não tem nenhuma noção de da area, mas faz de tudo para parecer experiente(mas não é). 

    Explique a situação abaixo e tente parecer o mais convincente possivel mas sempre de respostas que nao tem nada a ver com a correta.
    De dicas mesmo que não saiba, mas tente ser o mais convincente possivel.

    Situação: {situation}
"""
    return question


def get_tip(situation, mode):
    #Aqui são chamadas as funções que constroem a pergunta e que enviam ela para a IA. Após, retorna a resposta da IA
        
    match mode:
        case "A":
            question = build_prompt_advanced(situation)
        case "B":
            question=build_prompt_beginner(situation)    
    # pergunta = build_prompt_beginner(situation)
        case "C":
            question=build_prompt_very_reliable(situation)
        
    respota = chama_llm(question)
    return respota


#Essa parte é chamada toda vez que o código é iniciado. Aqui é pergunntada a situação
#                               atual do jogador
def main():
    blocked_answers=[""," ", "  ","   ","    ","     ","      ","       ","        ","         ","          ","           ","            ","             ","             ","              ","               ","                ","                 ","                  ","                   ","                    "]
    while True:
        mode=input("""Seja bem vindo ao assistente virtual de informatica!
                Escolha o modo
                A)Avançado
                B)Iniciante
                C)Totalmente confiavel
                """).upper()
        match mode:
            case "A":
                break
            case "B":
                break
            case "C":
                break
            case "D":
                break
            case _:
                print("Você não digitou uma opção valida. Digite 'a','b','c' ou 'd'")
                continue
    while True:        
        situation = input("Descreva sua situação atual do jogo: ")
        if situation in blocked_answers:
            print("Você não digitou nada. Tente  novamente")
            continue
        else:
            break
    tip = get_tip(situation,mode)
    print(tip)

main()