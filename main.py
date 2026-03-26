from fastapi import FastAPI


app = FastAPI(title='Request Body bilan ishlash')


@app.post('/api/products')
async def create_product(
    data: dict
):
    return data

# POST /api/calculate {"a": 3, "b": 4, "operator": "+"} -> {"result": 7}
