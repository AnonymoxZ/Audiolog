from mutagen.id3 import ID3, APIC, PictureType
from mutagen.mp4 import MP4, MP4Cover
from pydub import AudioSegment
from pytubefix import YouTube
import requests
import os
import mimetypes



class DownloaderYtb:
    OUTPUT_FILES_AUDIO = '../output/audio/' # change for input files from CTkinter
    OUTPUT_FILES_VIDEO = '../output/video/'
    OUTPUT_FILES_COVER = '../output/covers/'
    FILES_TYPE = ['mp4','m4a','mp3']

    def __init__(self, url:str):
        self.url = url

    # metadata methods
    def _insert_tags(self, file_type:str):
        url_video = YouTube(self.url)
        file_path_cover = f'{self.OUTPUT_FILES_COVER}{url_video.title}.jpg'
        file_path_video = f'{self.OUTPUT_FILES_VIDEO}{url_video.title}.mp4'
        file_path_m4a = f'{self.OUTPUT_FILES_AUDIO}{url_video.title}.m4a'
        file_path_mp3 = f'{self.OUTPUT_FILES_AUDIO}{url_video.title}.mp3'
        
        match file_type:        
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
            

    def _get_thumbnail(self):
        url_video = YouTube(self.url)
        res = requests.get(url_video.thumbnail_url) # https://i.ytimg.com/vi/{THUMBNAIL_URL}/hq720.jpg?v=68e03988
        if res.status_code == 200:
            with open(f'{self.OUTPUT_FILES_COVER}{url_video.title}.jpg', 'wb') as file:
                file.write(res.content)
            print("Suscefull download!")
        else:
            print(f"Download failed: {response.status_code}")


    def download_m4a(self):
        url_video = YouTube(self.url)
        type_f = self.FILES_TYPE[1]
        streams = url_video.streams.get_audio_only()
        streams.download(output_path=self.OUTPUT_FILES_AUDIO)
        self._get_thumbnail()
        if os.path.exists(f'{self.OUTPUT_FILES_AUDIO}{url_video.title}.m4a'):
            self._insert_tags(file_type=type_f)


    def convert_to_mp3(self):
        # ---------------------------------
        url_video = YouTube(self.url)
        type_f = self.FILES_TYPE[2]
        path_file_m4a = f'../output/audio/{url_video.title}.m4a'
        path_file_mp3 = f'../output/audio/{url_video.title}.mp3'
        # ---------------------------------
        audio = AudioSegment.from_file(path_file_m4a, format='m4a')
        file_convert = audio.export(path_file_mp3,
        format='mp3',
        bitrate='192k',
        tags={'album': f'{url_video.author}', 'artist': f'{url_video.author}'})
        self._insert_tags(file_type=type_f)
        # remove m4a
        if os.path.isfile(path_file_mp3):
            os.remove(path_file_m4a)



test = DownloaderYtb('https://youtu.be/ko70cExuzZM?si=Mc_OJrDe8l9zNXB6')