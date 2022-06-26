import os
import cv2
from os.path import join
from os.path import exists
from pathlib import Path
from PIL import Image
import re
import shutil

def check_category(file):
    k = 0
    fn, fext = os.path.splitext(file)
    if (fext==".txt"):
        with open(os.path.join(src, file), 'r') as file:
            #print("File: ", file)
            for row in file:
                print("row: ", row)
                print("")
                #Background-Klasse -> leere Datei
                if (row != "") and (row[k] != '\n'):
                    cat, x, y, w, h = row.split(" ")
                    if (cat == "1"):
                        return "waste"
                    else:
                        return ""
                else:
                    print("Background-Class")
                    return "nowaste"

def readFile(f, src, txt_path_old, img_path_old, dest, invalid):
    print("txt_path_old: ", txt_path_old)
    print("img_path_old: ", img_path_old)
    print("dest: ", dest)
    print("invalid: ", invalid)
    file = f
    k = 0
    res_list = []
    str_list = []
    str_counter = 0
    fn, fext = os.path.splitext(file)
    if (fext==".txt"):
        with open(os.path.join(src, file), 'r') as file:
            #print("File: ", file)
            for row in file:
                print("row: ", row)
                print("")
                #Background-Klasse -> leere Datei
                if (row != "") and (row[k] != '\n'):
                    cat, x, y, w, h = row.split(" ")
                    #h = h.rstrip("\n")
                    if (float(x) >= 0 and float(x) <= 1) and (float(y) >= 0 and float(y) <= 1) and (float(w) >= 0 and float(w) <= 1) and (float(h) >= 0 and float(h) <= 1):
                        if cat == "waste":
                            line = str(1) + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h)
                            str_list.append(line)
                            print("str_list: ", str_list)
                            res_list.append(str_list)
                        else:
                            print("Annotation correct")
                    else:
                        print("Invalid YOLO-Format! Move to invalid_yolo_format")
                        shutil.move(txt_path_old, invalid)
                else:
                    print("Background Label")
                    print()
                    with open(dest, 'w') as file:
                        file.writelines("")
                        file.close()
                        return res_list
                str_list = []
            print("res: ", res_list)
            with open(dest, 'w') as file:
                for row in res_list:
                    file.writelines(row)
            file.close()
            print("")
            return res_list

def main(src, dest, alone, invalid, trash, waste, nowaste):
    src = src
    #dest = dest
    print("src: ", src)
    #print("dest: ", dest)
    #convert_to_jpeg(src)
    #print("Rename file & convert it to .jpeg ...")
    for file in os.listdir(src):
        print(file)
        print("")
        fn, fext = os.path.splitext(file)
        if fext == ".txt":
            check_path_jpeg = Path(os.path.join(src, fn + ".jpeg"))
            check_path_jpg = Path(os.path.join(src, fn + ".jpg"))
            txt_path_old = os.path.join(src, fn + ".txt")
            txt_path_dest = os.path.join(dest, fn + ".txt")

            if check_path_jpeg.is_file():
                print("We have a match !")
                img_path_old = check_path_jpeg
                img_path_dest = os.path.join(dest, fn + ".jpeg")
                bbx_list = readFile(file, src, txt_path_old, img_path_old, txt_path_dest, invalid)
                if bbx_list == []:
                    print("NO WASTE")
                    print("Bbx-Liste: ", bbx_list)

            elif check_path_jpg.is_file():
                print("We have a match !")
                img_path_old = check_path_jpg
                img_path_dest = os.path.join(dest, fn + ".jpg")
                bbx_list = readFile(file, src, txt_path_old, img_path_old, txt_path_dest, invalid)
                if bbx_list == []:
                    print("NO WASTE")
                    print("Bbx-Liste: ", bbx_list)
            else:
                print("No matching image-file. Next File...")
                print("Alone: ", )
                path = Path(os.path.join(alone, fn + fext))
                b_exists = os.path.exists(path)
                print(b_exists)
                if not b_exists:
                    shutil.move(txt_path_old, alone)
                else:
                    shutil.move(txt_path_old, trash)

        elif fext == ".jpeg":
            check_path = Path(os.path.join(src, fn + ".txt"))
            img_path = os.path.join(src, fn + ".jpeg")
            if check_path_jpeg.is_file():
                print("We have a match !")
                shutil.copy(img_path, dest)
                #coord_list = convertYoloCoordinates(bbx_list, img_path)
                #saveBBxImage(coord_list, img_path, dest, fn)
            else:
                print("No matching txt-file. Next File...")
                print("Alone: ", os.path.join(alone, fn + fext))
                path = Path(os.path.join(alone, fn + fext))
                b_exists = os.path.exists(path)
                print(b_exists)
                if not b_exists:
                    shutil.move(img_path, alone)
                else:
                    shutil.move(img_path, trash)

        elif fext == ".jpg":
            check_path = Path(os.path.join(src, fn + ".txt"))
            img_path = os.path.join(src, fn + ".jpg")
            if check_path_jpeg.is_file():
                print("We have a match !")
                shutil.copy(img_path, dest)
                #coord_list = convertYoloCoordinates(bbx_list, img_path)
                #saveBBxImage(coord_list, img_path, dest, fn)
            else:
                print("No matching txt-file. Next File...")
                print("Alone: ", os.path.join(alone, fn + fext))
                path = Path(os.path.join(alone, fn + fext))
                b_exists = os.path.exists(path)
                print(b_exists)
                if not b_exists:
                    shutil.move(img_path, alone)
                else:
                    shutil.move(img_path, trash)

         else:
             print("Invalid File-Extension.. Move to trash")
             shutil.move(img_path, trash)

    print("Sorting images with each category into seperat folders..")
    str_cat = ""
    for file in os.listdir(dest):
        fn, fext = os.path.splitext(file)
        img_path = os.path.join(dest, fn + fext)
        print("img_path: ", img_path)
        if fext == ".txt":
            str_cat = check_category(file)
            print("str_cat: ", str_cat)
            if str_cat == "waste":
                shutil.copy(img_path, waste)
            elif str_cat == "nowaste":
                shutil.copy(img_path, nowaste)
            else
                shutil.copy(img_path, trash)
    print("Finished check_label & sorting into cat-folders!")
    print("Now you have to split Traindata into Train & val..")

if __name__ == "__main__":
    src = "/home/datafleet/21/YOLO-Darknet/darknet/data/preprocessing_20/input"
    dest = "/home/datafleet/21/YOLO-Darknet/darknet/data/preprocessing_20/output"
    alone = "/home/datafleet/21/YOLO-Darknet/darknet/data/preprocessing_20/alone"
    invalid = "/home/datafleet/21/YOLO-Darknet/darknet/data/preprocessing_20/yolo_format_invalid"
    trash = "/home/datafleet/21/YOLO-Darknet/darknet/data/preprocessing_20/trash"
    waste = "/home/datafleet/21/YOLO-Darknet/darknet/data/preprocessing_20/category-folder/waste"
    nowaste = "/home/datafleet/21/YOLO-Darknet/darknet/data/preprocessing_20/category-folder/nowaste"
    #cat_list = {"nowaste", "waste"}
    main(src, dest, alone, invalid, trash, waste, nowaste)

