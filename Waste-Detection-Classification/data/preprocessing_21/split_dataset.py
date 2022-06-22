import os
from glob import glob
import shutil
from sklearn.model_selection import train_test_split
# do test train splitting

# find image names
#image_files = glob("/home/stec102594/YOLO-Darknet/data/20_traindata/*.jpeg")
# remove file extension
#image_names = [name.replace(".jpeg","") for name in image_files]
# Use scikit learn function for convenience
#print(image_names)



src = "/home/datafleet/21/YOLO-Darknet/darknet/data/preprocessing_21/category-folder/"
test_dir = "/home/datafleet/21/YOLO-Darknet/darknet/data/val/"
print(test_dir)
train_dir = "/home/datafleet/21/YOLO-Darknet/darknet/data/train/"
print(train_dir)
name_list = []
folder_count = 0

for folder in os.listdir(src):
    name_list = []
    test_names = []
    train_names = []
    print(str(folder))
    print("Splitting all .jpeg's")
    print("----------------------")
    path = src + str(folder) + "/"
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
                            train_dir + image)
                shutil.copy(path + txt,
                            train_dir + txt)

            for file in test_names:
                image = file+'.jpeg'
                txt = file+'.txt'
                #print(os.path.join(destination_path, image))
                shutil.copy(path + image,
                            test_dir + image)
                shutil.copy(path + txt,
                            test_dir + txt)
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
                            train_dir + image)
                shutil.copy(path + txt,
                            train_dir + txt)

            for file in test_names:
                image = file+'.jpeg'
                txt = file+'.txt'
                #print(os.path.join(destination_path, image))
                shutil.copy(path + image,
                            test_dir + image)
                shutil.copy(path + txt,
                            test_dir + txt)
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
                            train_dir + image)
                shutil.copy(path + txt,
                            train_dir + txt)

            for file in test_names:
                image = file+'.jpg'
                txt = file+'.txt'
                #print(os.path.join(destination_path, image))
                shutil.copy(path + image,
                            test_dir + image)
                shutil.copy(path + txt,
                            test_dir + txt)
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
                            train_dir + image)
                shutil.copy(path + txt,
                            train_dir + txt)

            for file in test_names:
                image = file+'.jpg'
                txt = file+'.txt'
                #print(os.path.join(destination_path, image))
                shutil.copy(path + image,
                            test_dir + image)
                shutil.copy(path + txt,
                            test_dir + txt)
        else:
            print("Name-List is empty!")
    except FileNotFoundError as e:
        print("Alle Dateien durchsucht.")
