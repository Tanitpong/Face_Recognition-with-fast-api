from face_non_train import *
from face_train import *
from fastapi import FastAPI, File, UploadFile
import cv2
import numpy as np


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "post:/img   get:/train  get:/whos"}

# upload single file
@app.post("/img")
async def analyze_image(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.fromstring(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    img_dimensions = str(img.shape)
    predict = searching(img)

    # _, encoded_img = cv2.imencode('.PNG', return_img)

    # encoded_img = base64.b64encode(encoded_img)

    return  { "File Name": file.filename, "Size:": str(len(contents))+" Byte", "Dimension": img_dimensions, "name": predict}

@app.get("/train")
async def train_image():
    str_return = training()
    return {"message": str(str_return)}

@app.get("/whos")
async def who_image():
    str_return = check_who()
    return {"message": str(str_return)}
