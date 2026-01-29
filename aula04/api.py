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

@app.post("/name")
async def name(request:Request):
    data = await request.json()
    nametxt = data.get("name","")
    return {"response": f"Olá {nametxt}, bem vindo a minha API!"}

@app.post("/square")
async def square(request:Request):
    data = await request.json()
    number = data.get("number", 0)
    quadrado = number * number
    return {"response": quadrado}

@app.post("/triangle")
async def triangle(request:Request):
    data = await request.json()
    base = data.get("base", 1)
    height = data.get("height",1)
    area = base * height /2
    return {"response": area} 

@app.post("/age_verification")
async def age_verification(request:Request):
    data = await request.json()
    age = data.get("age", 1)
    if age < 18:
        return {"response": "menor de idade"}
    else:
        return {"response": "maior de idade"}
    

@app.post("/calculator")
async def calculator(request:Request):
    data = await request.json()
    num1 = data.get("num1", 1)
    num2 = data.get("num2", 1)
    operation = data.get("operation", "+")
    match operation:
        case "soma":
            return {"response":num1 + num2 }
        case "sub":
            return {"response":num1 - num2}
        case "mult":
            return {"response":num1 * num2}
        case "div":
            return {"response":num1 / num2}

@app.post("/total_letters")
async def total_letters(request:Request):
    data = await request.json()
    text = data.get("text", "")
    return {"response", len(text.replace(" ", ""))}

@app.post("/no_spaces")
async def no_spaces(request:Request):
    data = await request.json()
    text = data.get("text","")
    return {"response", text.replace(" ", "")}
    
@app.post("/double_list")
async def double_list(request:Request):
    data = await request.json()
    numbers = data.get("numbers", [])
    double_num_list = []
    for num in numbers:
        double_num_list.append(num * 2)
    return {"response": double_num_list}

@app.post("/strong_password")
async def strong_password(request:Request):
    data = await request.json()
    password = data.get("password")
    if len(password) <8:
        return {"response":"Senha fraca"}
    else:
        return {"response":"Senha forte"}
    
@app.post("/multiplication_table")
async def multiplication_table(request:Request):
    data = await request.json()
    number = data.get("number", 1)
    multiplication_table = []
    times_1 = number *1
    multiplication_table.append(times_1)
    times_2 = number *2
    multiplication_table.append(times_2)
    times_3 = number *3
    multiplication_table.append(times_3)
    times_4 = number *4
    multiplication_table.append(times_4)
    times_5 = number *5
    multiplication_table.append(times_5)
    times_6 = number *6
    multiplication_table.append(times_6)
    times_7 = number *7
    multiplication_table.append(times_7)
    times_8 = number *8
    multiplication_table.append(times_8)
    times_9 = number *9
    multiplication_table.append(times_9)
    times_10 = number *10
    multiplication_table.append(times_10)
    return {"response":multiplication_table}









if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "api:app",
        host=os.getenv("HOST", "localhost"),
        port=int(os.getenv("PORT", "8000")),
        reload=True
    ) 