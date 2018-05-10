import platform

MEDIA_FILE=True
os = platform.system()
if os == 'Windows':
    MEDIA_PATH='Media\\'
    MUSIC_PATH=MEDIA_PATH+'Music\\'
    PICTURES_PATH=MEDIA_PATH+'Pictures\\'
    VIEOS_PATH=MEDIA_PATH+'Videos\\'
else:
    MEDIA_PATH='./Media/'
    MUSIC_PATH = MEDIA_PATH + 'Music/'
    PICTURES_PATH = MEDIA_PATH + 'Pictures/'
    VIDEOS_PATH = MEDIA_PATH + 'Videos/'
BACKGROUNDS={'Main' : 'bg-chuuni.jpg',
             'Music': 'bg.jpg'}

version = 0.222
name = "karu"

def load_images():
    pass
def save_images():
    pass
