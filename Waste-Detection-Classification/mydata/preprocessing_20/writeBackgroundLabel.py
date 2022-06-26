import os
import cv2
from os.path import join
from pathlib import Path
#from PIL import Image
import re

def writeFile(src, f):
    b_empty = False
    file = f
    print("FILE: ",file)
    fn, fext = os.path.splitext(file)
    if fext==".txt":
        with open(os.path.join(src, file), 'r') as f:
            for row in f:
                print("ROW: ", row)
                if row == "":
                    f.close()
                    b_empty = True
                    break
            if b_empty:
                with open(os.path.join(src, file), 'w') as f:
                    print("Background Label")
                    cat = "nowaste"
                    x = 0.5
                    y = 0.5
                    w = 1.0
                    h = 1.0
                    line = cat + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h)
                    f.write(line)
                    f.close()

def main(src):
    src = src
    print("src: ", src)
    #print("dest: ", dest)
    #convert_to_jpeg(src)
    #print("Rename file & convert it to .jpeg ...")
    for file in os.listdir(src):
        print(file)
        print("")
        fn, fext = os.path.splitext(file)
        if fext == ".txt":
            check_path = Path(os.path.join(src, fn + ".jpeg"))
            if check_path.is_file():
                print("We have a match !")
                img_path = os.path.join(src, fn + ".jpeg")
                writeFile(src, file)
                #print("Bbx-Liste: ", bbx_list)
                #coord_list = convertYoloCoordinates(bbx_list, img_path)
                #saveBBxImage(coord_list, img_path, dest, fn)
            else:
                print("No matching image-file. Next File...")

if __name__ == "__main__":
    src = "/home/stec102594/YOLO-Darknet/darknet/data/validation"
    main(src)
