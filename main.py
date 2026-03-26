from fastapi import FastAPI


app = FastAPI(title='Request Body bilan ishlash')


@app.post('/api/products')
async def create_product(
    data: dict
):
    return data

