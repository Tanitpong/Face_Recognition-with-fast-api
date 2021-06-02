class Analyzer(BaseModel):
    filename: str
    img_dimensions: str
    encoded_img: str

@app.post("/analyze", response_model=Analyzer)
async def analyze_route(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.fromstring(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    img_dimensions = str(img.shape)
    return_img = processImage(img)

    # line that fixed it
    _, encoded_img = cv2.imencode('.PNG', return_img)

    encoded_img = base64.b64encode(encoded_img)

    return{
        'filename': file.filename,
        'dimensions': img_dimensions,
        'encoded_img': endcoded_img,
    }