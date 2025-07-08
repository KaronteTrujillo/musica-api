from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from downloader.download import download_video, download_audio
import os
import uuid

app = FastAPI()

@app.get("/download/video")
async def download_video_endpoint(url: str):
    output_file = f"downloads/{uuid.uuid4()}.mp4"
    os.makedirs("downloads", exist_ok=True)
    
    try:
        await download_video(url, output_file)
        return FileResponse(output_file, media_type="video/mp4", filename=os.path.basename(output_file))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/download/audio")
async def download_audio_endpoint(url: str):
    output_file = f"downloads/{uuid.uuid4()}.mp3"
    os.makedirs("downloads", exist_ok=True)
    
    try:
        await download_audio(url, output_file)
        return FileResponse(output_file, media_type="audio/mpeg", filename=os.path.basename(output_file))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
