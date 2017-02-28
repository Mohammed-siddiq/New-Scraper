import csv
import os

def createnew(name):
    fp = open(name, 'a+')
    return fp


def writestudentresult(fp, result):
        writer = csv.writer(fp)
        writer.writerows(result)
        writer.writerow(['-----------------------------'])


def createdirectoryifnotexist(directoryname):
    if not os.path.exists(directoryname):
        os.mkdir(directoryname)

