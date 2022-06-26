from os import listdir
from os.path import isfile, join
customPath = '/home/datafleet/darknet/data/preprocessing_21/val/'
#for f in listdir(customPath):
    #test=join(customPath,f)
    #print("Path:",test)

onlyfiles = [f for f in listdir(customPath) if isfile(join(customPath,f))]


trainFile = customPath + "val.txt"
file = open(trainFile, 'w')

counter = 0
customPath = '/home/datafleet/darknet/data/preprocessing_21/val/'
for eachFile in onlyfiles:
    #print(eachFile)
    if "jpeg" in eachFile:
        counter+=1
        file.write(customPath + eachFile + "\n")
    if "jpg" in eachFile:
        counter+=1
        file.write(customPath + eachFile + "\n")
print(counter)
