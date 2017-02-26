

url = ''
counter = 0


def gencollege(collegename, branch, year, genericurl):

    global url
    url = genericurl + collegename + branch+year


def gennexturl():
    global counter
    counter = counter+1

    return url + str(counter).zfill(3)


