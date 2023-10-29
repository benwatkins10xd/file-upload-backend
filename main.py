from fastapi import FastAPI, UploadFile
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# setup CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all HTTP headers
)

UPLOAD_DIR = Path.cwd() / 'uploads'
print(UPLOAD_DIR)

@app.get("/")
async def hello():
    return {"hello": "world"}

@app.post("/upload")
async def create_upload_file(file_upload: UploadFile):
    print('file : ', file_upload)
    data = await file_upload.read()
    # open file in binary mode
    with open(UPLOAD_DIR / file_upload.filename, "wb") as fh:
        fh.write(data)

    print(file_upload.filename)
    return {"filename": file_upload.filename}
