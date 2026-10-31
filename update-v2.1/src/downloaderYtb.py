from mutagen.id3 import ID3, APIC, PictureType
from mutagen.mp4 import MP4, MP4Cover
from pydub import AudioSegment
from pytubefix import YouTube
import requests
import os
import mimetypes
from pathlib import Path



class DownloaderYtb:
    # setup init
    # *****************************************
    OUTPUT_FILES_AUDIO_M4A = Path(r'output\\audio\\m4a\\')
    OUTPUT_FILES_AUDIO_MP3 = Path(r'output\\audio\\mp3\\')
    OUTPUT_FILES_COVER = Path(r'output\\covers\\')
    os.makedirs(OUTPUT_FILES_AUDIO_M4A, exist_ok=True)
    os.makedirs(OUTPUT_FILES_AUDIO_MP3, exist_ok=True)
    os.makedirs(OUTPUT_FILES_COVER, exist_ok=True)
    FILES_TYPE = ['m4a','mp3']
    def __init__(self, url:str, type_f:int):
        self.url = url
        self.type_f = type_f
    # *****************************************

    # metadata methods
    def _insert_tags(self):
        try:
            url_video = YouTube(self.url)
            file_path_cover = fr'{self.OUTPUT_FILES_COVER}/{url_video.title}.jpg'
            file_path_m4a = fr'{self.OUTPUT_FILES_AUDIO_M4A}/{url_video.title}.m4a'
            file_path_mp3 = fr'{self.OUTPUT_FILES_AUDIO_MP3}/{url_video.title}.mp3'
            
            match self.FILES_TYPE[self.type_f]:
                # m4a
                case 'm4a':
                    audio = MP4(file_path_m4a)
                    audio['\xa9ART'] = url_video.author # artist
                    audio['\xa9alb'] = url_video.author # album
                    # cover
                    with open(file_path_cover, 'rb') as f:
                        audio['covr'] = [MP4Cover(f.read(), imageformat=MP4Cover.FORMAT_JPEG)]
                    
                    audio.save()

                # mp3
                case 'mp3':
                    image_mime = mimetypes.guess_file_type(file_path_cover)[0]
                    audio = ID3(file_path_mp3)
                    with open(file_path_cover, 'rb') as f:
                        image_data = f.read()
                    
                    audio.setall('APIC', [APIC(
                        mime=image_mime,
                        type=PictureType.COVER_FRONT,
                        data=image_data
                    )])

                    audio.save()
        except Exception as err:
            print(f'ERROR _insert_tags(): {err}')
    

    def _get_thumbnail(self):
        try:
            url_video = YouTube(self.url)
            res = requests.get(url_video.thumbnail_url) # https://i.ytimg.com/vi/{THUMBNAIL_URL}/hq720.jpg?v=68e03988
            if res.status_code == 200:
                with open(fr'{self.OUTPUT_FILES_COVER}/{url_video.title}.jpg', 'wb') as file:
                    file.write(res.content)
                print("Suscefull download!")
            else:
                print(f"Download failed: {res.status_code}")
        except Exception as err:
            print(f'ERROR _get_thumbnail(): {err}')
    # *****************************************
    
    # download/convert methods
    def download_m4a(self):
        try:
            url_video = YouTube(self.url)
            streams = url_video.streams.get_audio_only()
            streams.download(output_path=self.OUTPUT_FILES_AUDIO_M4A)
            self._get_thumbnail()
            for f in self.OUTPUT_FILES_AUDIO_M4A.iterdir():
                if f.is_file() and f.name == f'{url_video.title}.m4a':
                    print(f'{f.name} exists in {self.OUTPUT_FILES_AUDIO_M4A}')
            self._insert_tags()
        except Exception as err:
            print(f'ERROR dowload_m4a(): {err}')


    def convert_to_mp3(self):
        try:
            url_video = YouTube(self.url)
            self._get_thumbnail()
            path_file_m4a = f'{self.OUTPUT_FILES_AUDIO_MP3}/{url_video.title}.m4a'
            path_file_mp3 = f'{self.OUTPUT_FILES_AUDIO_MP3}/{url_video.title}.mp3'
            stream = url_video.streams.get_audio_only()
            stream.download(output_path=self.OUTPUT_FILES_AUDIO_MP3)
            
            if os.path.exists(path_file_m4a):
                audio = AudioSegment.from_file(path_file_m4a, format='m4a')
                audio.export(
                    path_file_mp3,
                    format='mp3',
                    bitrate='192k',
                    tags={'album': url_video.author, 'artist': url_video.author}
                )
                if os.path.isfile(path_file_mp3) and os.path.isfile(path_file_m4a):
                    os.remove(path_file_m4a)
                    if not os.path.isfile(path_file_m4a):
                        self._insert_tags() # just add image for mp3
        except Exception as err:
            print(f'ERROR convert_to_mp3(): {err}')
    # *****************************************


audio = DownloaderYtb(url='https://youtu.be/RlFw72PHJO8?si=EajKDv0LgKmz6Kxz', type_f=1) # type_f-> file format

# download thumb
'''
[OK] audio._get_thumbnail()
- create and verify dirs
- request and download media jpg
'''

# download media/insert tags
'''
[OK] audio.download_m4a()
- request media/download audio from URL video
- insert tags MP4/AAC in M4A file
'''

# converter media
'''
[OK] audio.convert_to_mp3()
- download media/m4a
- convert to mp3
- insert tags ID3
'''