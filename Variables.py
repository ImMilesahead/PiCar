import platform
import os

MEDIA_FILE=True
currentos = platform.system()
if currentos == 'Windows':
    SLASH = '\\'
    MEDIA_PATH='C:\\Users\\Kuuhaku\\Desktop\\Picar\\Media\\'
    MUSIC_PATH=MEDIA_PATH+'Music\\'
    PICTURES_PATH=MEDIA_PATH+'Pictures\\'
    VIEOS_PATH=MEDIA_PATH+'Videos\\'
else:
    MEDIA_PATH='/home/pi/PiCar/Media/'
    MUSIC_PATH = MEDIA_PATH + 'Music/'
    PICTURES_PATH = MEDIA_PATH + 'Pictures/'
    VIDEOS_PATH = MEDIA_PATH + 'Videos/'
    SLASH = '/'
BACKGROUNDS={'Main' : 'bg-chuuni.jpg',
             'Music': 'bg.jpg'}

version = 0.3
name = "karu"

def load_images():
    pass
def save_images():
    pass
