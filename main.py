from fastapi import FastAPI, UploadFile, File
import pandas as pd
from model_starter import model_pipeline
app = FastAPI()

@app.get("/")
def root():
    return {"message:": "Hello World"}


@app.post("/ask")
def upload_file(file: UploadFile = File(...)):
    testdata = pd.read_csv(file.file)
    file.file.close()

    result = model_pipeline(testdata)
    return result