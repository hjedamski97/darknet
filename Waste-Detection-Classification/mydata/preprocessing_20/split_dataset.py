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


src = "/home/stec102594/YOLO-Darknet/data/waste/"
test_dir = "/home/stec102594/YOLO-Darknet/data/val/"
print(test_dir)
train_dir = "/home/stec102594/YOLO-Darknet/data/train/"
print(train_dir)
name_list = []

for file in os.listdir(src):
    print(file)
    print("")
    fn, fext = os.path.splitext(file)
    if (fext == ".jpeg"):
        name_list.append(fn)

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
     shutil.move(src + image,
                 train_dir + image)
     shutil.move(src + txt,
                 train_dir + txt)

for file in test_names:
     image = file+'.jpeg'
     txt = file+'.txt'
     #print(os.path.join(destination_path, image))
     shutil.move(src + image,
                 test_dir + image)
     shutil.move(src + txt,
                 test_dir + txt)

print("Now all .jpg's ..")
name_list = []

for file in os.listdir(src):
    print(file)
    print("")
    fn, fext = os.path.splitext(file)
    if (fext == ".jpg"):
        name_list.append(fn)

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
     shutil.move(src + image,
                 train_dir + image)
     shutil.move(src + txt,
                 train_dir + txt)

for file in test_names:
     image = file+'.jpg'
     txt = file+'.txt'
     #print(os.path.join(destination_path, image))
     shutil.move(src + image,
                 test_dir + image)
     shutil.move(src + txt,
                 test_dir + txt)
