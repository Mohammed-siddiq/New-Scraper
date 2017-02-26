import csv


def createnew(name):
    fp = open(name, 'a+')
    return fp


def writestudentresult(fp, result):
        writer = csv.writer(fp)
        writer.writerows(result)
        writer.writerow(['-----------------------------'])

