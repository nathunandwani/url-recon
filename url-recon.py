import urllib2

def getrobots(url):
    arr = []
    try:
        domain = url.split("//")[-1]
        if not domain.endswith('/'):
            domain = domain + '/'
        domain = "http://" + domain + "robots.txt"
        response = urllib2.urlopen(domain)
        contents = response.read()
        for item in contents:
            if ("Disallow: " in item):
                link = item.split("Disallow: ")[1]
                if link != "/":
                    if checkifresponsive(domain + link):
                        print "-" + domain + link
                        arr.append(domain + link)
    except Exception as e:
        print e
    return arr

def checkifresponsive(url):
    if "http://" not in url:
        url = "http://" + url
    try:
        response = urllib2.urlopen(url)
        print "URL is responsive: " + url
        return True 
    except Exception as e:
        print "Error: " + str(e)
        if "www." not in url:
            print "Trying with 'www.'"
            url = url.replace("http://", "http://www.")
            print "Testing " + url
            return checkifresponsive(url)
        else:    
            return False

#checkifresponsive("jeugdinspecties.nl")
#getrobots("jeugdinspecties.nl\n")
#exit(0)
#counter = 0
responsive = ""
with open("file.txt", "r") as urls:
    for url in urls:
        url = url.rstrip()
        print "Testing " + url
        if checkifresponsive(url):
           responsive += url + "\n"
           otherlinks = getrobots(url)
           for link in otherlinks:
               responsive += link + "\n"
        #counter += 1
        #if counter == 10:
        #    break

file = open("responsive.txt", "w") 
file.write(responsive) 
file.close()
        
