# Audiolog - Downloader MP3 | testes v0.1
from pytubefix import YouTube

def BaixarMP3(link):
    try:
        video = YouTube(link)
        print(video.title)
        ys = video.streams.get_audio_only()
        ys.download(mp3=True,output_path='C:\\Users\\vitor\\OneDrive\\Área de Trabalho\\projetos\Audiolog\\baixados')
    except:
        print('Erro econtrado ao tentar realizar o download!')
