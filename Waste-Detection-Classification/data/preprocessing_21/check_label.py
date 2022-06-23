import os
import cv2
import os.path
from os.path import join
from os.path import exists
from pathlib import Path
from PIL import Image
import re
import shutil
import statistics

def readNames(path):
    k = 0
    res_list = []
    counter = 0
    with open(path, 'r') as file:
        #print("File: ", file)
        for row in file:
            print("row: ", row)
            print("")
            #Background-Klasse -> leere Datei
            if (row != "") and (row[k] != '\n'):
                name = row.split(" ")
            res_list.append({"idx": str(counter), "cat": name, "num_labels": 0, "num_images": 0})
            counter = counter + 1
    return res_list

def countImages(dest, cat_list):
    print("ToDO")
    k = 0
    num_list = []
    elektronik_img = 0
    for element in cat_list:
       
    for file in os.listdir(dest):
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
                        if cat == "0":
                            elektronik_img  = elektronik_img + 1
                            break
                    else:
                        print("Background-Class")
                        break
    return num_list


# Ineffizient, aber automatisierbar
def count_annotations(dest, name_list):
    k = 0
    res_list = name_list
    for elem in res_list:
        b_add_image = False
        idx = str(elem['idx'])
        cat = str(elem['cat'])
        num_labels = int(elem['num_labels'])
        num_images = int(elem['num_images'])
        for file in os.listdir(dest):
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
                            if cat == idx:
                                num_labels = num_labels + 1
                                b_add_image = True

                if b_add_image == True:
                    num_images = num_images + 1
                file.close()
                b_add_image = False
        elem['idx'] = idx
        elem['cat'] = cat
        elem['num_labels'] = num_labels
        elem['num_images'] = num_images
    return res_list

def sort_list(num_list):
    res = sorted(num_list, key=lambda k: k['num'], reverse=False)
    #print("Sortierte Liste: ", res)
    return res

def images_elektronik(dest):
    k = 0
    elektronik_img = 0
    for file in os.listdir(dest):
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
                        if cat == "0":
                            elektronik_img  = elektronik_img + 1
                            break
                    else:
                        print("Background-Class")
                        break
    return elektronik_img

def images_glas(dest):
    k = 0
    glas_img = 0
    for file in os.listdir(dest):
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
                        if cat == "1":
                            glas_img  = glas_img + 1
                            break
                    else:
                        print("Background-Class")
                        break
    return glas_img

def images_holz(dest):
    k = 0
    holz_img = 0
    for file in os.listdir(dest):
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
                        if cat == "2":
                            holz_img  = holz_img + 1
                            break
                    else:
                        print("Background-Class")
                        break
    return holz_img

def images_moebel(dest):
    k = 0
    moebel_img = 0
    for file in os.listdir(dest):
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
                        if cat == "3":
                            moebel_img  = moebel_img + 1
                            break
                    else:
                        print("Background-Class")
                        break
    return moebel_img

def images_pappe(dest):
    k = 0
    pappe_img = 0
    for file in os.listdir(dest):
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
                        if cat == "4":
                            pappe_img  = pappe_img + 1
                            break
                    else:
                        print("Background-Class")
                        break
    return pappe_img

def images_plastik(dest):
    k = 0
    plastik_img = 0
    for file in os.listdir(dest):
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
                        if cat == "5":
                            plastik_img  = plastik_img + 1
                            break
                    else:
                        print("Background-Class")
                        break
    return plastik_img

def images_sanitaer(dest):
    k = 0
    sanitaer_img = 0
    for file in os.listdir(dest):
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
                        if cat == "6":
                            sanitaer_img  = sanitaer_img + 1
                            break
                    else:
                        print("Background-Class")
                        break
    return sanitaer_img


def images_sonderabfaelle(dest):
    k = 0
    sonderabfaelle_img = 0
    for file in os.listdir(dest):
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
                        if cat == "7":
                            sonderabfaelle_img  = sonderabfaelle_img + 1
                            break
                    else:
                        print("Background-Class")
                        break
    return sonderabfaelle_img


def images_stoffe(dest):
    k = 0
    stoffe_img = 0
    for file in os.listdir(dest):
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
                        if cat == "8":
                            stoffe_img  = stoffe_img + 1
                            break
                    else:
                        print("Background-Class")
                        break
    return stoffe_img

def check_category(file, prio_idx):
    k = 0
    fn, fext = os.path.splitext(file)
    b_res = False
    if (fext==".txt"):
        with open(os.path.join(src, file), 'r') as file:
            #print("File: ", file)
            for row in file:
                print("row: ", row)
                print("")
                #Background-Klasse -> leere Datei
                if (row != "") and (row[k] != '\n'):
                    cat, x, y, w, h = row.split(" ")
                    if (cat == prio_idx):
                        b_res = True
    return b_res

def readFile(f, src, txt_path_old, img_path_old, dest, invalid, num_cat):
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
                        if cat == str(0) or cat == str(1) or cat == str(2) or cat == str(3) or cat == str(4) or cat == str(5) or cat == str(6) or cat == str(7) or cat == str(8):
                            line = str(cat) + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h)
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

def main(cat_dir, path_names, src, dest, alone, invalid, trash):
    src = src
    print("src: ", src)
    print("names: ", path_names)
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
                bbx_list = readFile(file, src, txt_path_old, img_path_old, txt_path_dest, invalid, num_cat)
                if bbx_list == []:
                    print("Fehler")
                    print("Bbx-Liste: ", bbx_list)

            elif check_path_jpg.is_file():
                print("We have a match !")
                img_path_old = check_path_jpg
                img_path_dest = os.path.join(dest, fn + ".jpg")
                bbx_list = readFile(file, src, txt_path_old, img_path_old, txt_path_dest, invalid, num_cat)
                if bbx_list == []:
                    print("Fehler")
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
            #path = Path(check_path_jpeg)
            if check_path.is_file():
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
            if check_path.is_file():
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
    print("")
    print("1.read category..")
    print("-------------------")
    name_list = []
    name_list = readNames(path_names)
    print("idx/category: ", name_list)
    num_images = []
    b_cat = False
    print("2.counting annotations..")
    print("------------------- ")
    num_annotations = []
    num_annotations = count_annotations(dest, name_list)

    print("3.Counting the number of images per class..")
    num_elektronik = images_elektronik(dest)
    num_glas = images_glas(dest)
    num_holz = images_holz(dest)
    num_moebel = images_moebel(dest)
    num_pappe = images_pappe(dest)
    num_plastik = images_plastik(dest)
    num_sanitaer = images_sanitaer(dest)
    num_sonderabfaelle = images_sonderabfaelle(dest)
    num_stoffe = images_stoffe(dest)

    num_images.append({"idx": "0", "num": num_elektronik})
    num_images.append({"idx": "1", "num": num_glas})
    num_images.append({"idx": "2", "num": num_holz})
    num_images.append({"idx": "3", "num": num_moebel})
    num_images.append({"idx": "4", "num": num_pappe})
    num_images.append({"idx": "5", "num": num_plastik})
    num_images.append({"idx": "6", "num": num_sanitaer})
    num_images.append({"idx": "7", "num": num_sonderabfaelle})
    num_images.append({"idx": "8", "num": num_stoffe})
    print("Num Images: ", num_images)
    sorted_list = sort_list(num_images)
    print("Sortierte Liste: ", sorted_list)

    print("Building Dataset with similar distrubution.")
    for element in sorted_list:
        temp_idx = str(element['idx'])
        print("INDEX: ", temp_idx)
        for file in os.listdir(dest):
            fn, fext = os.path.splitext(file)
            path_jpeg = Path(os.path.join(dest, fn + ".jpeg"))
            path_jpg = Path(os.path.join(dest, fn + ".jpg"))
            #print("img_path: ", img_path)
            print("----------------------------------")
            if fext == ".txt":
                path_txt = os.path.join(dest, fn + fext)
                b_cat = check_category(file, temp_idx)
                print("b_cat: ", b_cat)
                if b_cat == True:
                    # Directory
                    temp_dir = temp_idx
                    # Path
                    dest_path = os.path.join(cat_dir, temp_dir)
                    try:
                        os.makedirs(dest_path, exist_ok = True)
                        shutil.move(path_txt, dest_path)
                        if path_jpg.is_file():
                            img_jpg = os.path.join(dest, fn + ".jpg")
                            shutil.move(img_jpg, dest_path)
                        if path_jpeg.is_file():
                            img_jpeg = os.path.join(dest, fn + ".jpeg")
                            shutil.move(img_jpeg, dest_path)
                    except OSError as error:
                        print("Error: ", error)
        print("Next prio-level-category")

    print("Counting number of images in train & val folder..")
    
    print("Finished check_label & sorting into cat-folders!")
    print("Now you have to split Traindata into Train & val..")

if __name__ == "__main__":
    path_names = "/home/datafleet/21/YOLO-Darknet/darknet/data/preprocessing_21/names.txt"
    cat_dir = "/home/datafleet/21/YOLO-Darknet/darknet/data/preprocessing_21/category-folder"
    src = "/home/datafleet/21/YOLO-Darknet/darknet/data/preprocessing_21/input"
    dest = "/home/datafleet/21/YOLO-Darknet/darknet/data/preprocessing_21/output"
    alone = "/home/datafleet/21/YOLO-Darknet/darknet/data/preprocessing_21/alone"
    invalid = "/home/datafleet/21/YOLO-Darknet/darknet/data/preprocessing_21/yolo_format_invalid"
    trash = "/home/datafleet/21/YOLO-Darknet/darknet/data/preprocessing_21/trash"
    main(cat_dir, path_names, src, dest, alone, invalid, trash)

