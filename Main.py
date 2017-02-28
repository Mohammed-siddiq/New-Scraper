import FileOps
import EstablishConnection
import Scraper
import BeautifulUsn


def semresult():
    url = "http://www.fastvturesults.com/check_new_results/"
    folderpath="College_results"
    FileOps.createdirectoryifnotexist(folderpath)


    # college name for the file
    collegename=raw_input("Enter College Name :\n")
    folderpath = folderpath + "//"+collegename
    FileOps.createdirectoryifnotexist(folderpath)
    collegecode = raw_input("Enter the college Code : \n")
    year = raw_input("Enter the year : \n")
    folderpath = folderpath + "//" + year
    FileOps.createdirectoryifnotexist(folderpath)
    branch = raw_input("Enter the branch code : \n")
    folderpath = folderpath + "//" + branch
    FileOps.createdirectoryifnotexist(folderpath)
    semester = raw_input("Enter the Semester : \n")
    attempt = raw_input("Enter the attempt :\n")
    #  -1 because in gennexturl() the value is incremented and then url is generated

    BeautifulUsn.start = int(raw_input(" Enter the starting usn \n"))-1
    BeautifulUsn.end = int(raw_input(" Enter the ending usn \n"))
    range_usn = BeautifulUsn.end - BeautifulUsn.start
    folderpath = folderpath + "//"

    # generating a generic file name
    filename = folderpath + collegename+"_"+year+"_"+branch+"_"+semester+"sem.csv"
    # create a file using the above filename
    fp = FileOps.createnew(filename)

    BeautifulUsn.gencollege(collegecode, year, branch, url)
    for i in range(range_usn):
        studenturl = BeautifulUsn.gennexturl()
        page = EstablishConnection.openwebpage(studenturl)

        soup = Scraper.page(page)
        # added semester
        resulturl, name = Scraper.semresultlink(semester, attempt, soup)

        if resulturl != 'none':
            page = EstablishConnection.openwebpage(resulturl)

            soup = Scraper.page(page)

            result = Scraper.getresult(soup, name)

            print result

            FileOps.writestudentresult(fp, result)


semresult()
