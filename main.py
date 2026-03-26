from fastapi import FastAPI

from schemas import Data, ProductCreate


app = FastAPI(title='Request Body bilan ishlash')

products: list[dict] = []


@app.post('/api/products')
async def create_product(data: ProductCreate):
    products.append(data)
    return {'message': 'ok'}


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
