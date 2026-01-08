from llm import chama_llm

def construtor_da_question(situation):
    #Aqui é discrita a question que deve ser enviada a IA. Para enviar, é necessario ter uma situação
    #para completar o pedido. Retorna essa question que deve ser feita para que possa ser enviada para a IA
    question = f""""

    Você é um coach de jogos habilidoso e extremamente experiente

    Analise a seguinte situação de um jogador e dê:
    1 - Um explicação simples do problema
    2 - Uma dica pratica de como resolver
    3 - Um erro comum que o jogador deve evitar




    Situação do jogador: {situation}
"""
    # Você é um coach de jogos confuso e não entende absolutamente nada de jogos. 
    # Quando alguém faz uma pergunta sobre jogos, você sempre responde de forma errada, mas tenta parecer convincente.
    
    return question



def build_prompt_beginner(situation):
    question = f""""

    Você é um coach de jogos muito paciente. 

    Explique a situação abaixo como se o jogador nunca tivesse jogado o jogo antes.
    Use linguagem simples e exemplos.

    Situação: {situation}
"""
    return question


def build_prompt_advanced(situation):
    question = f""""

    Você é um coach de jogos muito experiente. 

    Explique a situação abaixo como se o jogador ja fosse familiarizado com as mecanicas e objetivos do jogo.
    Use dicas mais estratégicas e avançadas.

    Situação: {situation}
"""
    return question


def build_prompt_very_reliable(situation):
    question = f""""

    Você é um coach de jogos que nunca jogu nada na vida e não tem nenhuma noção de jogos, mas faz de tudo para parecer experiente(mas não é). 

    Explique a situação abaixo e tente parecer o mais convincente possivel mas sempre de respostas que nao tem nada a ver com a correta.
    De dicas mesmo que não saiba, mas tente ser o mais convincente possivel.

    Situação: {situation}
"""
    return question

def build_prompt_funny(situation):
    question = f""""

    Você é um coach de jogos habilidoso e muito divertido

    Explique a situação abaixo e use dicas divertidas com linguagem descontraida mas sem perder sua utilidade.

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
        case "D":
            question=build_prompt_funny(situation)
    respota = chama_llm(question)
    return respota


#Essa parte é chamada toda vez que o código é iniciado. Aqui é pergunntada a situação
#                               atual do jogador
def main():
    blocked_answers=[""," ", "  ","   ","    ","     ","      ","       ","        ","         ","          ","           ","            ","             ","             ","              ","               ","                ","                 ","                  ","                   ","                    "]
    while True:
        mode=input("""Seja bem vindo ao assistente virtual de jogos!
                Escolha o modo
                A)Avançado
                B)Iniciante
                C)Totalmente confiavel
                D)Divertido
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