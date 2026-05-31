from fastapi import FastAPI

import sys
import os
sys.path.insert(0, os.path.abspath("../db"))

for path in sys.path:
    print(path)

import database

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Hello, World!"}

@app.get("/enemies")
async def getEnemies():
    enemies = database.returnEnemies()
    return enemies

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)