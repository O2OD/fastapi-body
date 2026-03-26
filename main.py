from fastapi import FastAPI

from schemas import Data


app = FastAPI(title='Request Body bilan ishlash')


@app.post('/api/products')
async def create_product(
    data: dict
):
    return data


@app.post('/api/calculate')
async def calculate(data: Data):
    if data.operator == '+':
        return {'result': data.a + data.b}
    elif data.operator == '-':
        return {'result': data.a - data.b}
    elif data.operator == '*':
        return {'result': data.a * data.b}
    elif data.operator == '/':
        return {'result': data.a / data.b}
    else:
        return {'error': 'operator not found'}
