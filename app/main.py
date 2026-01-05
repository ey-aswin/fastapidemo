from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


@app.get("/hello-world")
def homePageTest():
    return {"msg":"Working","ENV":os.getenv('PYTHON_ENV')}  