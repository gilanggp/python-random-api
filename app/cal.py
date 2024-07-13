import re
from fastapi import FastAPI

app = FastAPI()

# aritmatik function
def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    return x / y

@app.get("/cal/{command}")
def calculator(command: str):
    split = re.compile(r"(\d*\.?\d+)([-+*/])(\d*\.?\d+)")
    res = split.match(command)
    
    if res:
        n1 = float(res.group(1))
        op = res.group(2)
        n2 = float(res.group(3))

        if op == '+':
            result = tambah(n1, n2)
        elif op == '-':
            result = kurang(n1, n2)
        elif op == '*':
            result = kali(n1, n2)
        elif op == '/':
            result = bagi(n1, n2)
        else:
            return {"error": "Invalid operator"}
        
        return {"command": command, "result": result}
    else:
        return {"error": "Invalid input format"}
