from fastapi import FastAPI, Request  # Importa as classes FastAPI e Request do framework
import os  # Importa o módulo para acessar variáveis de ambiente
from dotenv import load_dotenv  # Importa a função para carregar variáveis do arquivo .env

app = FastAPI()  # Cria uma instância da aplicação FastAPI


# --------------------
# ENDPOINT GET
# --------------------
@app.get("/")  # Decorator que define uma rota GET na raiz "/"
def home():  # Função que retorna a resposta do endpoint
    # teste=input("")
    return {"message": f"Bernardo Gheno Xavier"}  # Retorna um JSON com uma mensagem
@app.get("/status")
def status():
    return {"status":"ok",
            "server":"running"}


# --------------------
# ENDPOINT POST
# --------------------
@app.post("/message")  # Decorator que define uma rota POST em "/message"
async def receive_message(request: Request):  # Função assíncrona que recebe uma requisição
    data = await request.json()  # Aguarda e extrai o corpo JSON da requisição
    text = data.get("text", "") # Obtém o valor do campo "text", retorna string vazia se não existir
    if text =="s":
        return {"message":"Nenhum texto reccebido"}
    else:  

        return {  # Retorna um objeto JSON com os dados processados
            "received_text": text,  # Texto recebido na requisição
            "length": len(text),# Comprimento do texto em caracteres
            "maiusculo":text.upper(),
            "quantidade_de_palavras":len(text.split())    
        }


# --------------------
# RODAR A API
# --------------------
if __name__ == "__main__":  # Verifica se o script está sendo executado diretamente
    load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env
    import uvicorn  # Importa o servidor ASGI Uvicorn
    uvicorn.run(  # Inicia o servidor Uvicorn
        "api:app",  # Especifica o módulo e a instância da aplicação
        host=os.getenv("HOST"),  # Define o host a partir da variável de ambiente HOST
        port=int(os.getenv("PORT")),  # Define a porta a partir da variável de ambiente PORT convertida para inteiro
        reload=True  # Ativa o modo de recarga automática ao detectar mudanças no código
    )
