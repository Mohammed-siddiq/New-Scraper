import FileOps
import EstablishConnection
import Scraper
import BeautifulUsn


def semresult():
    url = "http://www.fastvturesults.com/check_new_results/"

    # college name for the file
    collegename=raw_input("Enter College Name\n")
    collegecode = raw_input("Enter the college Code\n")
    year = raw_input("Enter the year\n")
    branch = raw_input("Enter the branch code\n")
    semester = raw_input("Enter the Semester\n")

    # generating a generic file name

    filename = collegename+"_"+year+"_"+branch+"_"+semester+"sem.csv"
    # create a file using the above filename
    fp = FileOps.createnew(filename)

    BeautifulUsn.gencollege(collegecode, year, branch, url)
    for i in range(120):
        studenturl = BeautifulUsn.gennexturl()
        page = EstablishConnection.openwebpage(studenturl)

        soup = Scraper.page(page)
        # added semester
        resulturl, name = Scraper.semresultlink(semester, soup)

        if resulturl != 'none':
            page = EstablishConnection.openwebpage(resulturl)

            soup = Scraper.page(page)

            result = Scraper.getresult(soup, name)

            print result

            FileOps.writestudentresult(fp, result)

semresult()
