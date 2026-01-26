import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request


app = FastAPI()

@app.get("/")
def home():
    return {"message":"API rodando"}

@app.get("/ping")
def ping():
    return {"response":"pong"}

@app.get("/health")
def health():
    return {"status":"ok"}

@app.post("/uppercase")
async def uppercase(request:Request):
    data=await request.json()
    text=data.get("text", "")
    return {"result":text.upper()}

@app.post("/reverse")
async def reverse(request:Request):
    data = await request.json()
    text=data.get("text","")
    return {"result":text[::-1]}

@app.post("/double")
async def double(request:Request):
    data = await request.json()
    number = data.get("number",0)
    return {"result":number*2}

@app.post("/sum")
async def sum(request: Request):
    data = await request.json()
    number1 = data.get("number1",1)
    number2 = data.get("number2",1)
    return {"result":number1 + number2}

@app.post("/multiply")
async def multiply(request:Request):
    data = await request.json()
    number1 = data.get("number1", 1)
    number2 = data.get("number2", 1)
    return {"result": number1*number2}

@app.post("/lowercase")
async def lowercase(request:Request):
    data = await request.json()
    text = data.get("text", "")
    return {"response": text.lower()}

@app.post("/count_words")
async def count_words(request:Request):
    data = await request.json()
    text = data.get("text", "")
    words = text.split()
    return {"result":len(words)}

@app.post("/is_palindrome")
async def is_palindrome(request:Request):
    data = await request.json()
    text = data.get("text", "")
    text_reverse = text[::-1]
    if text_reverse == text:
        return {"response": "Sim"}
    else:
        return {"response":"Não"}
    
@app.post("/is_palindrome2")
async def is_palindrome2(request:Request):
    data = await request.json()
    text = data.get("text", "")
    is_palindrome = text == text[::-1]
    return {"result": is_palindrome}

@app.post("/repeat")
async def repeat(request:Request):
    data = await request.json()
    text = data.get("text","")
    times = data.get("times", 1)
    return {"result": text*times}

@app.post("/is_even")
async def is_even(request:Request):
    data = await request.json()
    number = data.get("number", 0)
    is_even = number % 2 == 0
    return {"result": is_even}

@app.post("/max_number")
async def max_number(request:Request):
    data = await request.json()
    numbers = data.get("numbers",[])
    max_num = max(numbers)
    return {"response": max_num}    

@app.post("/min_number")
async def min_number(request:Request):
    data = await request.json()
    numbers = data.get("numbers",[])
    min_num = min(numbers)
    return {"response": min_num}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "api:app",
        host=os.getenv("HOST", "localhost"),
        port=int(os.getenv("PORT", "8000")),
        reload=True
    ) 