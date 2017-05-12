from __future__ import print_function
from bs4 import BeautifulSoup
import FileOps
import EstablishConnection
import Scraper
import BeautifulUsn
import os


def Scrapepage(p):

    s = BeautifulSoup(p, "html.parser")
    tables = s.find_all('table')
    trs = tables[0].find_all('tr')
    usn=''

    tds = trs[0].find_all('td')
    usn = str(tds[1].text.strip()[1:])
    tds = trs[1].find_all('td')
    name = str(tds[1].text.strip()[1:])+'(' + usn + ')'
    namel = []
    namel.append(name)
    trs = tables[2].find_all('tr')
    tds = trs[0].find_all('td')
    totalmarks = "Total Marks  " + str(tds[1].text.strip())

    percent = (int(tds[1].text.strip()[1:]) / 900.0)*100

    total = []
    total.append(totalmarks)
    result = []
    result.append(namel)
    result.append(total)
    tds = trs[1].find_all('td')
    cclass = "Class " + str(tds[1].text.strip())

    classl = []

    classl.append(cclass)
    result.append(classl)
    percentl = []
    Percentage = "Percentage : " + str(percent) + "%"
    percentl.append(Percentage)
    result.append(percentl)
    trs = tables[1].find_all('tr')
    for tr in trs:
        res=[]
        tds = tr.find_all('td')
        c = 0
        for td in tds :
            if c == 0:
                code = str(td.text.strip())
            elif c==1:
                sub = str(td.text.strip())
            elif c == 2 :
                res.append(sub)
                res.append(code)
                res.append(str(td.text.strip()))

            else:
                res.append(str(td.text.strip()))

            c+=1
        if(c!=0):
            result.append(res)

    print (result)
    return result




def scrape():
    url = "http://results.vtu.ac.in/results/result_page.php?usn="
    folderpath = "College_results"
    FileOps.createdirectoryifnotexist(folderpath)

    # college name for the file
    collegename = raw_input("Enter College Name :\n")
    folderpath = os.path.join(folderpath, collegename)
    # FileOps.createdirectoryifnotexist(folderpath)
    collegecode = raw_input("Enter the college Code : \n")
    year = raw_input("Enter the year : \n")
    folderpath = os.path.join(folderpath, year)
    # FileOps.createdirectoryifnotexist(folderpath)
    branch = raw_input("Enter the branch code : \n")
    folderpath = os.path.join(folderpath, branch)
    # FileOps.createdirectoryifnotexist(folderpath)
    semester = raw_input("Enter the Semester : \n")
   # attempt = raw_input("Enter the attempt :\n")
    #  -1 because in gennexturl() the value is incremented and then url is generated

    BeautifulUsn.start = int(raw_input(" Enter the starting usn \n")) - 1
    BeautifulUsn.end = int(raw_input(" Enter the ending usn \n"))
    range_usn = BeautifulUsn.end - BeautifulUsn.start

    # generating a generic file name

    filename = collegename + "_" + year + "_" + branch + "_" + semester + "sem.csv"

    # create a file using the above filename
    fp = FileOps.createnew(folderpath, filename)

    BeautifulUsn.gencollege(collegecode, year, branch, url)
    for i in range(range_usn):
        studenturl = BeautifulUsn.gennexturl()
        p = EstablishConnection.openwebpage(studenturl)

        try:
            result = Scrapepage(p)
        except Exception,e:
            continue
        # added semester
        FileOps.writestudentresult(fp,result)


scrape()
