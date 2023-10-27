from fastapi import FastAPI, File, UploadFile
from starlette.responses import JSONResponse
from functions import do_gray_image , do_avg_image ,do_sharpen_image, do_gaussian_image , do_edge_image

app = FastAPI()


@app.post("/gray-image")
async def upload_image(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        processed_image_path = do_gray_image(image_bytes)
        if processed_image_path:
            return JSONResponse(content={"message": "Image processed and saved", "path": processed_image_path})
        else:
            return JSONResponse(content={"error": "Image processing failed"}, status_code=400)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.post("/avg-image")
async def upload_image(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        processed_image_path = do_avg_image(image_bytes)
        if processed_image_path:
            return JSONResponse(content={"message": "Image processed and saved", "path": processed_image_path})
        else:
            return JSONResponse(content={"error": "Image processing failed"}, status_code=400)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/gaussian-image")
async def upload_image(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        processed_image_path = do_gaussian_image(image_bytes)
        if processed_image_path:
            return JSONResponse(content={"message": "Image processed and saved", "path": processed_image_path})
        else:
            return JSONResponse(content={"error": "Image processing failed"}, status_code=400)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/do_edge_detection")
async def upload_image(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        processed_image_path = do_edge_image(image_bytes)
        if processed_image_path:
            return JSONResponse(content={"message": "Image processed and saved", "path": processed_image_path})
        else:
            return JSONResponse(content={"error": "Image processing failed"}, status_code=400)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
 
@app.post("/do_sharpen_image")
async def upload_image(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        processed_image_path = do_sharpen_image(image_bytes)
        if processed_image_path:
            return JSONResponse(content={"message": "Image processed and saved", "path": processed_image_path})
        else:
            return JSONResponse(content={"error": "Image processing failed"}, status_code=400)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500) 