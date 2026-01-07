from llm import chama_llm

def construtor_da_pergunta(situacao):
    #Aqui é discrita a pergunta que deve ser enviada a IA. Para enviar, é necessario ter uma situação
    #para completar o pedido. Retorna essa pergunta que deve ser feita para que possa ser enviada para a IA
    pergunta = f""""

    Você é um coach de jogos habilidoso e extremamente experiente

    Analise a seguinte situação de um jogador e dê:
    1 - Um explicação simples do problema
    2 - Uma dica pratica de como resolver
    3 - Um erro comum que o jogador deve evitar




    Situação do jogador: {situacao}
"""
    # Você é um coach de jogos confuso e não entende absolutamente nada de jogos. 
    # Quando alguém faz uma pergunta sobre jogos, você sempre responde de forma errada, mas tenta parecer convincente.
    
    return pergunta



def build_prompt_beginner(situacao):
    pergunta = f""""

    Você é um coach de jogos muito paciente. 

    Explique a situação abaixo como se o jogador nunca tivesse jogado o jogo antes.
    Use linguagem simples e exemplos.

    Situação: {situacao}
"""
    return pergunta


def build_prompt_advanced(situacao):
    pergunta = f""""

    Você é um coach de jogos muito experiente. 

    Explique a situação abaixo como se o jogador ja fosse familiarizado com as mecanicas e objetivos do jogo.
    Use dicas mais estratégicas e avançadas.

    Situação: {situacao}
"""
    return pergunta


def build_prompt_muito_confiavel(situacao):
    pergunta = f""""

    Você é um coach de jogos que nunca jogu nada na vida e não tem nenhuma noção de jogos, mas faz de tudo para parecer experiente(mas não é). 

    Explique a situação abaixo e tente parecer o mais convincente possivel mas sempre de respostas que nao tem nada a ver com a correta.
    De dicas mesmo que não saiba, mas tente ser o mais convincente possivel.

    Situação: {situacao}
"""
    return pergunta


def pega_dica(situacao, modo):
    #Aqui são chamadas as funções que constroem a pergunta e que enviam ela para a IA. Após, retorna a resposta da IA
        
    if modo=="B":
        pergunta = build_prompt_beginner(situacao)
    elif modo=="A":
        pergunta=build_prompt_advanced(situacao)    
    # pergunta = build_prompt_beginner(situacao)
    else:
        pergunta=build_prompt_muito_confiavel(situacao)
    respota = chama_llm(pergunta)
    return respota


#Essa parte é chamada toda vez que o código é iniciado. Aqui é pergunntada a situação
#                               atual do jogador
def main():
    repostas_bloqueadas=[""," ", "  ","   ","    ","     ","      ","       ","        ","         ","          ","           ","            ","             ","             ","              ","               ","                ","                 ","                  ","                   ","                    "]
    while True:
        modo=input("""Seja bem vindo ao assistente virtual de jogos!
                Escolha o modo
                A)Avançado
                B)Iniciante
                C)Totalmente confiavel
                """).upper()
        match modo:
            case "A":
                break
            case "B":
                break
            case "C":
                break
            case _:
                print("Você não digitou uma opção valida. Digite 'a','b' ou 'c'")
                continue
    while True:        
        situacao = input("Descreva sua situação atual do jogo: ")
        if situacao in repostas_bloqueadas:
            print("Você não digitou nada. Tente  novamente")
            continue
        else:
            break
    dica = pega_dica(situacao,modo)
    print(dica)

main()