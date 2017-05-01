import csv
import os

def createnew(folderpath, name):
    filepath = os.path.join(folderpath, name)
    if not os.path.exists(folderpath):
        os.makedirs(folderpath)
    fp = open(filepath, 'a+')
    return fp


def writestudentresult(fp, result):
        writer = csv.writer(fp)
        writer.writerows(result)
        writer.writerow(['-----------------------------'])


def createdirectoryifnotexist(directoryname):
    if not os.path.exists(directoryname):
        os.makedirs(directoryname)

