import yt_dlp
import asyncio

async def download_video(url: str, output_file: str):
    ydl_opts = {
        'outtmpl': output_file,
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True,
        'socket_timeout': 10,
        'retries': 3,
    }

    loop = asyncio.get_event_loop()
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        await loop.run_in_executor(None, ydl.download, [url])

async def download_audio(url: str, output_file: str):
    ydl_opts = {
        'outtmpl': output_file,
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True,
        'socket_timeout': 10,
        'retries': 3,
    }

    loop = asyncio.get_event_loop()
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        await loop.run_in_executor(None, ydl.download, [url])
