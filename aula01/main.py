from llm import chama_llm

def construtor_da_pergunta(situacao):
    #Aqui é discrita a pergunta que deve ser enviada a IA. Para enviar, é necessario ter uma situacao
    #para completar o pedido. Retorna essa pergunta que deve ser feita para que possa ser enviada para a IA
    pergunta = f""""

    Você é um coach de jogos habilidoso e extremamente experiente

    Analise a seguinte situacao de um jogador e dê:
    1 - Um explicação simples do problema
    2 - Uma dica pratica de como resolver
    3 - Um erro comum que o jogador deve evitar




    situacao do jogador: {situacao}
"""
    # Você é um coach de jogos confuso e não entende absolutamente nada de jogos. 
    # Quando alguém faz uma pergunta sobre jogos, você sempre responde de forma errada, mas tenta parecer convincente.
    
    return pergunta



def build_prompt_beginner(situacao):
    pergunta = f""""

    Você é um coach de jogos habilidoso e extremamente experiente

    Analise a seguinte situacao de um jogador que não sabe nada de jogos e entrou nele pela primeira vez na vida, sem conhecimento das mecanicas, termos e objetivos do jogo.De:
    1 - Uma explicação simples do problema
    2 - Uma dica pratica de como resolver
    3 - Um erro comum que o jogador deve evitar




    situacao do jogador: {situacao}
"""
    return pergunta

def pega_dica(situacao):
    #Aqui são chamadas as funções que constroem a pergunta e que enviam ela para a IA. Após, retorna a resposta da IA
    
    pergunta = construtor_da_pergunta(situacao)
    
    # pergunta = build_prompt_beginner(situacao)
    
    respota = chama_llm(pergunta)
    return respota


#Essa parte é chamada toda vez que o código é iniciado. Aqui é pergunntada a situacao
#                               atual do jogador
situacao = input("Descreva sua situacao atual do jogo: ")
dica = pega_dica(situacao)
print(dica)