from os import listdir
from os.path import isfile, join

mypath = 'INSERT_DIRECTORY'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
file_name = 'INSERT_FULL_FILE_PATH'


i = 0
while i < 1:
    print(onlyfiles[i])
    with open(file_name,mode = 'r') as fobj:
        for line in fobj:
            print(sum(1 for line in fobj))
            i+=1