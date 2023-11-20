from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def f_index():
    return {"FIO": "Жигулина Мария Александровна"}

@app.get('/tools')
async def f_indexT():
    return {"message": "Hello", "hello": "asd"}

@app.get('/users')
async def f_index():
    return {"message": "Hello"}
