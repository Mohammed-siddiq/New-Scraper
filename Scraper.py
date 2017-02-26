from __future__ import print_function
from bs4 import BeautifulSoup


def page(p):
    s = BeautifulSoup(p, "html.parser")
    return s


def semresultlink(sem, soup):
    try:
        resulttab = soup.find(id="scell")
        trs = resulttab.find_all("tr")
    except Exception,e:
        return 'none', 'none'
    flag = False
    resulturl = 'none'
    name = soup.find('div', class_="col-xs-12 box-red-round lead text-center").text.strip()
    for tr in trs:
        tds = tr.find_all('td')
        for td in tds:
            if td.text.strip() == sem:
                links = tr.find_all('a', string='Result')
                for a in links:
                    resulturl = a['href']
                    flag = True
                    break
            if flag:
                break
        if flag:
            break

    return resulturl, name


def getresult(soup,n):
    resulttab = soup.find(id="scell")
    trs = resulttab.find_all("tr", class_="success")
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

