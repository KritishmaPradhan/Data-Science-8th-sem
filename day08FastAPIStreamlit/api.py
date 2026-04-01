from fastapi import FastAPI

app = FastAPI()

@app

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/item")
async def get_items():
    return [{
        "name": "item1"
    },
    {
        "name": "item2"
    }]

