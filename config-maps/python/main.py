from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
import os

app = FastAPI()
CONFIGMAP_IMAGE_PATH = os.getenv("IMAGE_PATH")


@app.get("/", response_class=HTMLResponse)
def read_root():
    env_var = os.getenv("ENV_VAR", "don't work")
    html_content = f"""
    <html>
        <head><title>ConfigMap</title></head>
        <body>
            <h1>FastAPI</h1>
            <p>Environment Variable: {env_var}</p>
        </body>
    </html>
    """
    return html_content

@app.get("/image")
def get_image():

    if os.path.exists(CONFIGMAP_IMAGE_PATH):
        return FileResponse(CONFIGMAP_IMAGE_PATH, media_type="image/png")
    else:
        return {"error": "Image not found"}
