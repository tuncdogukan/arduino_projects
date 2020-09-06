# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 22:11:10 2019

@author: DT
"""

import http.client



def getPageHtml(urlroot,urlsuffix="/"):
    #print("Getting URL: ",urlroot,urlsuffix)
    conn = http.client.HTTPSConnection(urlroot,443)
    conn.request('GET',urlsuffix)
    r= conn.getresponse()
    output = r.read()
    conn.close()
    return output


downloadFolder = "C:/Users/dtunc/Pictures/WindowsSpotlight/"
pageRoot = 'spotlight.it-notes.ru'
pageSuffix = '/page/'
totalBytes = 0
currentPageNumber = 1
maxPageNumber = -1


rootHtml = getPageHtml(pageRoot)

pageNumberDividerPhrase = "next page-numbers"

pageNumberSplit = str(rootHtml).split(pageNumberDividerPhrase)
pageNumberStr = pageNumberSplit[0]
pgNoIndex = pageNumberStr.rfind("page")
pgNoIndexStart = pgNoIndex + 5
pgNoIndexEnd = pageNumberStr.rfind("\\'>")
pageNumber = pageNumberStr[pgNoIndexStart:pgNoIndexEnd]

print("There are ",pageNumber," pages in total.")

maxPageNumber = int(pageNumber)
maxPageNumber = 5


for p in range(1,maxPageNumber+1):    
    print("\n---Page: ",currentPageNumber,"---\n\n")
    currentPageNumber = currentPageNumber + 1
    pageHtml = getPageHtml(pageRoot,pageSuffix + str(p))    
    pageSplit = str(pageHtml).split("\"more-link\"")
    a = 1
    for l in pageSplit[1:]:
        imagelink = l[7:l.find("title")-2]
        imageID = imagelink[imagelink.rfind("/")+1:]
        imageSrc = imageID + ".jpg"
        print("\n\n",str(a),"------------------\n\n",imagelink,"- ID : ",imageID,"\n")
        a = a + 1
        
        imageLinkHtml = str(getPageHtml(pageRoot,imagelink[imagelink.find("images")-1:]))
          
        
        imageDlLink = imageLinkHtml[imageLinkHtml.find("wp-content/uploads"):imageLinkHtml.find(imageSrc)+len(imageSrc)]
        
        
        print("Downloading image: ",imageDlLink)
        
        image = getPageHtml(pageRoot,"/" + imageDlLink)
        
        with open(downloadFolder + imageSrc, 'wb') as f:
            f.write(image)
            f.flush()
            f.close()
            totalBytes = totalBytes + len(image)
            print(totalBytes/1024/1024," MB downloaded.")