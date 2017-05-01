

url = ''
start = 0
end = 0

def gencollege(collegename, branch, year, genericurl):

    global url
    url = genericurl + collegename + branch+year


def gennexturl():
    global start
    global end
    if start <= end:
        start = start + 1

    return url + str(start).zfill(3)


