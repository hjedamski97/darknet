import os
from os.path import join
from pathlib import Path
import re
from PIL import Image
from PIL import ExifTags
'''
takes a directory path as input and converts every .HEIC file to a jpg
'''
def check_rotation(src):
    src = src
    for f in os.listdir(src):
        if f.endswith('.jpeg') or f.endswith('.jpg') or f.endswith('.JPG'):
            try:
                image= Image.open(join(src, f))

                if hasattr(image, '_getexif'): # only present in JPEGs
                    for orientation in ExifTags.TAGS.keys():
                        if ExifTags.TAGS[orientation]=='Orientation':
                            break
                    e = image._getexif()       # returns None if no EXIF data
                    if e is not None:
                        exif=dict(e.items())
                        orientation = exif[orientation]

                        if orientation == 3:   image = image.transpose(Image.ROTATE_180)
                        elif orientation == 6: image = image.transpose(Image.ROTATE_270)
                        elif orientation == 8: image = image.transpose(Image.ROTATE_90)

                #fn,fext=os.path.splitext(f)
                #image.thumbnail(Size_2000,Image.ANTIALIAS)
                #image.save(join(pathdir,'resized','{}_2000.jpg').format(fn))
                #print(f + " saved. as" + " {}_2000.jpg".format(fn))
            except Exception as e :
                print(e)
        else:
            print("Datei ist kein Bild.")

def main(src):
    src = src
    check_rotation(src)

if __name__ == "__main__":
    src = "/home/datafleet/data/input"
    main(src)
