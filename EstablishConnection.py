import urllib2


'''
Openwebpage: establishes the connection and opens the web page using urlib2. Return the wb page to the caller

'''


def openwebpage(url):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]

    try:
        page = opener.open(url)
    except urllib2.HTTPError, e:
        print e.fp.read()

    return page
