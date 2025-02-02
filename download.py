import yt_dlp as youtube_dl
import os

# Définir le chemin de téléchargement
download_video_path = "download/vidéo"
os.makedirs(download_video_path, exist_ok=True)

# Fonction de téléchargement
def download_video(url):
    ydl_opts = {
        'outtmpl': os.path.join(download_video_path, '%(title)s.%(ext)s'),  # Format de nommage du fichier
    }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print(f"Téléchargement terminé ! La vidéo a été enregistrée dans : {download_video_path}")

url = "URL"

download_video(url)
