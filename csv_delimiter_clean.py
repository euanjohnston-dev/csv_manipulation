from os import listdir
from os.path import isfile, join
import re

copy_from_path = 'ORIGINAL_FILE_DIRECTORY'
copy_to_path = 'PASTE_TO_FILE_DIRECTORY'

onlyfiles = [f for f in listdir(copy_from_path) if isfile(join(copy_from_path, f))]

i = 0
while i < len(onlyfiles):
    print(onlyfiles[i])

    file_name = copy_from_path+onlyfiles[i]
    newfile = open(copy_to_path+onlyfiles[i], "w")

    with open(file_name,mode = 'r') as fobj:
        newrow = []
        for line in fobj:
                line_data = re.split(';',line)
                str1 = ';'.join(line_data)
                z = re.split('/', str1)
                str2 = ';'.join(z)
                newrow.append(str2)
        newfile.write(''.join(newrow) + '\n')
        newfile.close()
    print(i)

    i+=1