from os import listdir
from os.path import isfile
from PIL import Image, UnidentifiedImageError
from PIL.ExifTags import TAGS

specific = ['LensModel', 'FocalLength', 'Make', 'Model']
result ={} 

for item in listdir():
    if isfile(item):
        try:
            image = Image.open(item)
            for tag, value in image._getexif().items():
                try:
                    if TAGS[tag] in specific:
                        result[TAGS[tag]] = {value: 1}
                        print(TAGS[tag], value)
                        print(result[TAGS[tag]][value])
                        if result[TAGS[tag]][value] > 0:
                            print('hello')
                            result[TAGS[tag]][value] = result[TAGS[tag]][value] + 1
                        else:
                            print('e')
                            result[TAGS[tag]] = {value: 1}
                except(KeyError):
                    print('error')
        except(UnidentifiedImageError):
            print('not file')
    else:
        print('directory')
        # TODO recursion on directory
print(result)
