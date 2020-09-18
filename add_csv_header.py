import csv
from os import listdir
from os.path import isfile, join

row = ["COLUMN_HEADER_1","COLUMN_HEADER_2"]
mypath = 'DIRECTORY_FOR_FILES_TO_ADD_HEADER'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
onlyfiles.remove('.DS_Store')
i = 0
while i < len(onlyfiles):
    print(onlyfiles[i])
    file_name = mypath+onlyfiles[i]

    with open(file_name, 'r') as readFile:
        reader = csv.reader(readFile)
        lines = list(reader)
        print(row)
        str1 = ';'.join(row)
        print(str1)
        x = str1.split()
        print(str1.split())
        lines.insert(0, x)

    with open(file_name, 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)

    i+=1

    readFile.close()
    writeFile.close()