from __future__ import print_function
from bs4 import BeautifulSoup


def page(p):
    s = BeautifulSoup(p, "html.parser")
    return s


def semresultlink(sem, attempt, soup):
    try:
        resulttab = soup.find(id="scell")
        trs = resulttab.find_all("tr")
    except Exception,e:
        return 'none', 'none'
    flag = False
    resulturl = 'none'
    name = soup.find('div', class_="col-xs-12 box-red-round lead text-center").text.strip()
    for tr in trs:
        try:
            tds = tr.find_all('td')
            sem_td = tds[0]
            attempt_td=tds[1]
            if sem_td.text.strip() == sem and attempt_td.text.strip() == attempt :
                links = tr.find_all('a', string='Result')
                for a in links:
                    resulturl = a['href']
                    flag = True
                    break
            if flag:
                break
        except Exception,e:
            continue

    return resulturl, name


def getresult(soup,n):
    resulttab = soup.find(id="scell")
    trs = resulttab.find_all("tr", {'class': ["success","danger"]})
    details = soup.find_all('p', style='font-size:16px;')

    name = []
    name.append(str(n))
    result =[]
    result.append(name)
    for d in details:
        res =[]
        res.append(str(d.text.strip()))
        result.append(res)

    for tr in trs:
        sub = []
        tds = tr.find_all('td')
        for i in range(6):
            sub.append(str(tds[i].text.strip()))
        result.append(sub)
    return result

