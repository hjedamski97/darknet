import os
import cv2
from datetime import date
import os.path
from glob import glob
from os.path import join
from os.path import exists
from pathlib import Path
from PIL import Image
import re
import shutil
import statistics
from sklearn.model_selection import train_test_split

def split_dataset(cat_dir, train_dir, test_dir):
    src = cat_dir
    name_list = []
    folder_count = 0

    for folder in os.listdir(src):
         print("FOLDER: ", str(folder))
         name_list = []
         test_names = []
         train_names = []
         #print(str(folder))
         print("Splitting all .jpeg's")
         print("----------------------")
         path = os.path.join(src, str(folder)) + "/"
         print("PFAD: ", path)
         try:
             for file in os.listdir(path):
                 print(file)
                 print("")
                 fn, fext = os.path.splitext(file)
                 if (fext == ".jpeg"):
                      name_list.append(fn)

             if len(name_list) > 0 and len(name_list) >= 10:
                 test_names, train_names = train_test_split(name_list, test_size=0.8)
                 print("train-names: ", len(train_names))
                 print("------------------------------------------------")
                 print("test-names: ", len(test_names))

                 for file in train_names:
                     image = file + '.jpeg'
                     #print("i: ",image)
                     txt = file+'.txt'
                     #print(os.path.join(destination_path, image))
                     #print(os.path.cwd)
                     shutil.copy(path + image,
                                 train_dir + "/" + image)
                     shutil.copy(path + txt,
                                 train_dir + "/" + txt)

                 for file in test_names:
                     image = file+'.jpeg'
                     txt = file+'.txt'
                     #print(os.path.join(destination_path, image))
                     shutil.copy(path + image,
                                 test_dir + "/" + image)
                     shutil.copy(path + txt,
                                 test_dir + "/" + txt)

             elif len(name_list) > 0 and len(name_list) < 10:
                 test_names, train_names = train_test_split(name_list, test_size=0.5)
                 print("train-names: ", len(train_names))
                 print("------------------------------------------------")
                 print("test-names: ", len(test_names))

                 for file in train_names:
                     image = file + '.jpeg'
                     #print("i: ",image)
                     txt = file+'.txt'
                     #print(os.path.join(destination_path, image))
                     #print(os.path.cwd)
                     shutil.copy(path + image,
                                 train_dir + "/" + image)
                     shutil.copy(path + txt,
                                 train_dir + "/" + txt)

                 for file in test_names:
                     image = file+'.jpeg'
                     txt = file+'.txt'
                     #print(os.path.join(destination_path, image))
                     shutil.copy(path + image,
                                 test_dir + "/" + image)
                     shutil.copy(path + txt,
                                 test_dir + "/" + txt)
             else:
                 print("Name-List is empty!")

             print("Now all .jpg's ..")
             print("----------------------")
             name_list = []

             for file in os.listdir(src):
                 print(file)
                 print("")
                 fn, fext = os.path.splitext(file)
                 if (fext == ".jpg"):
                     name_list.append(fn)

             if len(name_list) > 0 and len(name_list) >= 10:
                 test_names, train_names = train_test_split(name_list, test_size=0.8)
                 print("train-names: ", len(train_names))
                 print("------------------------------------------------")
                 print("test-names: ", len(test_names))

                 for file in train_names:
                     image = file + '.jpg'
                     #print("i: ",image)
                     txt = file+'.txt'
                     #print(os.path.join(destination_path, image))
                     #print(os.path.cwd)
                     shutil.copy(path + image,
                                 train_dir + "/" + image)
                     shutil.copy(path + txt,
                                 train_dir + "/" + txt)

                 for file in test_names:
                     image = file+'.jpg'
                     txt = file+'.txt'
                     #print(os.path.join(destination_path, image))
                     shutil.copy(path + image,
                                 test_dir + "/" + image)
                     shutil.copy(path + txt,
                                 test_dir + "/" + txt)
             elif len(name_list) > 0 and len(name_list) < 10:
                 test_names, train_names = train_test_split(name_list, test_size=0.5)

                 print("train-names: ", len(train_names))
                 print("------------------------------------------------")
                 print("test-names: ", len(test_names))

                 for file in train_names:
                     image = file + '.jpg'
                     #print("i: ",image)
                     txt = file+'.txt'
                     #print(os.path.join(destination_path, image))
                     #print(os.path.cwd)
                     shutil.copy(path + image,
                                 train_dir + "/" + image)
                     shutil.copy(path + txt,
                                 train_dir + "/" + txt)

                 for file in test_names:
                     image = file+'.jpg'
                     txt = file+'.txt'
                     #print(os.path.join(destination_path, image))
                     shutil.copy(path + image,
                                 test_dir + "/" + image)
                     shutil.copy(path + txt,
                                 test_dir + "/" + txt)
             else:
                 print("Name-List is empty!")

         except FileNotFoundError as e:
             print("Alle Dateien durchsucht.")

def init(dir):
    path = dir
    k = 0
    res_list = []
    counter = 0
    #with open(os.path.join(src, file), 'r') as file:
    with open(os.path.join(path, "names.txt"), 'r') as file:
        #print("File: ", file)
        for row in file:
            #print("row: ", row)
            #print("")
            #Background-Klasse -> leere Datei
            if (row != "") and (row[k] != '\n'):
                name = row.strip('\n')
                #print(name)
            res_list.append({"idx": str(counter), "cat": name, "num_labels": 0, "num_images": 0})
            counter = counter + 1
    return res_list

# Ineffizient, aber automatisierbar
def category_info(dest_dir, init):
    dest = dest_dir
    k = 0
    idx = "0"
    cat = ""
    num_labels = 0
    num_images = 0
    res_list = init
    for elem in res_list:
        b_add_image = False
        idx = str(elem['idx'])
        cat = str(elem['cat'])
        print(cat)
        num_labels = int(elem['num_labels'])
        num_images = int(elem['num_images'])
        for file in os.listdir(dest):
            fn, fext = os.path.splitext(file)
            if (fext==".txt"):
                with open(os.path.join(dest, file), 'r') as file:
                    #print("File: ", file)
                    for row in file:
                        #print("row: ", row)
                        #print("")
                        #Background-Klasse -> leere Datei
                        if (row != "") and (row[k] != '\n'):
                            cat, x, y, w, h = row.split(" ")
                            if cat == idx:
                                num_labels = num_labels + 1
                                b_add_image = True

                if b_add_image == True:
                    num_images = num_images + 1
                #file.close()
                b_add_image = False
        elem['idx'] = idx
        #elem['cat'] = cat
        elem['num_labels'] = num_labels
        elem['num_images'] = num_images
    return res_list

def sort_list(info_list):
    res = sorted(info_list, key=lambda k: k['num_images'], reverse=False)
    #print("Sortierte Liste: ", res)
    return res

def fair_dataset(dest, cat_dir, l):
    sorted_list = l
    for element in sorted_list:
        temp_idx = str(element['idx'])
        print("INDEX: ", temp_idx)
        for file in os.listdir(dest):
            fn, fext = os.path.splitext(file)
            path_jpeg = Path(os.path.join(dest, fn + ".jpeg"))
            path_jpg = Path(os.path.join(dest, fn + ".jpg"))
            #print("img_path: ", img_path)
            #print("----------------------------------")
            if fext == ".txt":
                path_txt = os.path.join(dest, fn + fext)
                b_cat = check_category(path_txt, file, temp_idx)
                #print("b_cat: ", b_cat)
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

def check_category(path_txt, file, prio_idx):
    k = 0
    fn, fext = os.path.splitext(file)
    b_res = False
    if (fext==".txt"):
        with open(path_txt, 'r') as file:
            #print("File: ", file)
            for row in file:
                #print("row: ", row)
                #print("")
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
                #print("row: ", row)
                #print("")
                #Background-Klasse -> leere Datei
                if (row != "") and (row[k] != '\n'):
                    cat, x, y, w, h = row.split(" ")
                    #h = h.rstrip("\n")
                    if (float(x) >= 0 and float(x) <= 1) and (float(y) >= 0 and float(y) <= 1) and (float(w) >= 0 and float(w) <= 1) and (float(h) >= 0 and float(h) <= 1):
                        #print("Anzahl Kategorien: ", num_cat - 1)
                        if (int(cat) >= 0) and (int(cat) <= (num_cat-1)):
                            #if cat == "0":
                                #cat_new = "5"
                                #line = cat_new + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h)
                            #if cat == "1":
                                #cat_new = "0"
                                #line = cat_new + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h)
                            #if cat == "2":
                                #cat_new = "1"
                                #line = cat_new + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h)
                            #if cat == "3":
                                #cat_new = "2"
                                #line = cat_new + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h)
                            #if cat == "4":
                                #cat_new = "3"
                                #line = cat_new + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h)
                            #if cat == "5":
                                #cat_new = "4"
                                #line = cat_new + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h)
                            #if cat == "6":
                                #cat_new = "5"
                                #line = cat_new + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h)
                            #if cat == "7":
                                #cat_new = "6"
                                #line = cat_new + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h)
                            line = str(cat) + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h)
                            str_list.append(line)
                            #print("str_list: ", str_list)
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
            #print("res: ", res_list)
            with open(dest, 'w') as file:
                for row in res_list:
                    file.writelines(row)
            file.close()
            print("")
            return res_list

def save_stats(dest, full_list, train_list, val_list):
    str_date = str(date.today())
    len_full = len(full_list)
    len_train = len(train_list)
    len_val = len(val_list)
    print("len-full: ", len_full)
    print("len-train: ", len_train)
    print("len_val: ", len_val)
    i = 0
    j = 0
    k = 0
    with open(dest, "a") as file:
        file.writelines(str_date + "\n")
        file.writelines("")
        file.writelines("Full-Data-Stats: \n")
        for i in range(0, len_full-1):
            file.writelines(str(full_list[i]['cat']) + "\n" + "Num Annotations: " + str(full_list[i]['num_labels']) + "\n" + "Num Images: " + str(full_list[i]['num_images']) + "\n" )
        file.writelines("\n")
        file.writelines("")
        file.writelines("Train-Data-Stats: \n")
        for j in range(0, len_train-1):
            file.writelines(str(train_list[j]['cat']) + "\n" + "Num Annotations: " + str(train_list[j]['num_labels']) + "\n" + "Num Images: " + str(train_list[j]['num_images']) + "\n" )
        file.writelines("\n")
        file.writelines("")
        file.writelines("Val-Data-Stats: \n")
        for k in range(0, len_val-1):
            file.writelines(str(val_list[k]['cat']) + "\n" + "Num Annotations: " + str(val_list[k]['num_labels']) + "\n" + "Num Images: " + str(val_list[k]['num_images']) + "\n" )
        file.writelines("\n")
        file.writelines("")
        #file.writelines(str(val_list['cat']) + str(val_list['num_labels'] + str(val_list['num_images'])) )
    file.close()

def main(cat_dir, path_names, stats_path, src, dest, alone, invalid, trash, train, val):
    src = src
    print("src: ", src)
    print("names: ", path_names)
    print("1.Read category..")
    print("-------------------")
    init_list = []
    init_list = init(path_names)
    print("idx/category: ", init_list)
    num_cat = len(init_list)
    print("Number of Categories: ", num_cat)

    print("2.Check-Label..")
    print("-------------------")
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

    print("Label-Check over.")
    print("Init-List: ", init_list)
    print("Sorting images with each category into seperat folders..")
    print("")

    print("3.Get category-information..")
    print("------------------- ")
    info_list = []
    info_list = category_info(dest, init_list)
    print("Category-Info: ", info_list)
    print("4.Sort Prio-List..")
    print("------------------- ")
    sorted_list = sort_list(info_list)
    print("Sortierte Liste: ", sorted_list)

    print("5.Building Dataset with fair distribution..")
    print("------------------- ")
    fair_dataset(dest, cat_dir, sorted_list)

    print("6.Split Data into Train & val..")
    print("------------------- ")
    split_dataset(cat_dir, train, val)
    print("7.Counting number of images in train & val folder..")
    print("------------------- ")

    train_list = []
    val_list = []
    train_init = init(path_names)
    val_init = init(path_names)
    print("train-init:", train_init)
    print("-------------------------------")
    print("val-init:", val_init)

    print("Train-Path: ", train)
    train_list = category_info(train, train_init)
    print("Val-Path: ", val)
    val_list = category_info(val, val_init)
    print("Info-Init: ", init_list)
    print("")
    print("Info-Train: ", train_list)
    print("")
    print("Info-Validation: ", val_list)
    print("")
    file_path = data_path + "/" + "stats.txt"
    save_stats(file_path, init_list, train_list, val_list)
    print("Finished.")

if __name__ == "__main__":
    stats_path = "/home/datafleet/darknet/data/preprocessing_21"
    path_names = "/home/datafleet/darknet/data/preprocessing_21"
    cat_dir = "/home/datafleet/darknet/data/preprocessing_21/category-folder"
    src = "/home/datafleet/darknet/data/preprocessing_21/input"
    dest = "/home/datafleet/darknet/data/preprocessing_21/output"
    alone = "/home/datafleet/darknet/data/preprocessing_21/alone"
    invalid = "/home/datafleet/darknet/data/preprocessing_21/yolo_format_invalid"
    trash = "/home/datafleet/darknet/preprocessing_21/trash"
    train = "/home/datafleet/darknet/preprocessing_21/train"
    val = "/home/datafleet/darknet/data/preprocessing_21/val"
    main(cat_dir, path_names, stats_path, src, dest, alone, invalid, trash, train, val)

