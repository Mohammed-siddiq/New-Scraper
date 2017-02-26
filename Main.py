import FileOps
import EstablishConnection
import Scraper
import BeautifulUsn


def semresult():
    url = "http://www.fastvturesults.com/check_new_results/"

    collegecode = raw_input("Enter the college\nex:\tRnsit:1rn\t")
    year = raw_input("Enter the year")
    branch = raw_input("Enter the branch code\n")
    fp = FileOps.createnew("Cse6sem.csv")

    BeautifulUsn.gencollege(collegecode, year, branch, url)
    for i in range(120):
        studenturl = BeautifulUsn.gennexturl()
        page = EstablishConnection.openwebpage(studenturl)

        soup = Scraper.page(page)

        resulturl, name = Scraper.semresultlink('6', soup)

        if resulturl != 'none':
            page = EstablishConnection.openwebpage(resulturl)

            soup = Scraper.page(page)

            result = Scraper.getresult(soup, name)

            print result

            
            FileOps.writestudentresult(fp, result)


# page-url

semresult()