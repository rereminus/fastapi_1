from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def f_index():
    return {"FIO": "Жигулина Мария Александровна"}

@app.get('/tools')
async def f_indexT():
    return {"Skills": "Базовые навыки работы с языками программирования C# и Python"}

@app.get('/users')
async def f_indexU():
    return {"Phone": "89006005533"}
