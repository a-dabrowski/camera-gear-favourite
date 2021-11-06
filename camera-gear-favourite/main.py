from os import listdir
from os.path import isfile
from PIL import Image, UnidentifiedImageError
from PIL.ExifTags import TAGS

for item in listdir():
    if isfile(item):
        try:
            image = Image.open(item)
            for tag, value in image._getexif().items():
                try:
                    print(TAGS[tag], value)

                except(KeyError):
                    print('error')
        except(UnidentifiedImageError):
            print('not file')
    else:
        print('directory')
        # TODO recursion on directory
