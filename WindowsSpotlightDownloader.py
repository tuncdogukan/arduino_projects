# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 22:11:10 2019

@author: DT
"""

import http.client
from html.parser import HTMLParser
import urllib
import sys

startingPageNumber = 1
pageCount = -1              #-1 for all pages till the end

downloadFolder = "G:/WindowsSpotlightv2/"
downloadLogPath = downloadFolder + 'WindowsSpotlightDownloadLog.txt'
pageRoot = 'windows10spotlight.com'
pageSuffix = '/page/'
totalBytes = 0
totalImages = 0



def getPageHtml(url):
    
    if '://' in url:
        url = url[url.find('://')+3:]

    urlRoot = url
    urlSuffix = '/'
    
    if '/' in url:
        urlRoot = url[:url.find('/')]
        urlSuffix = url[url.find('/'):]
        
    conn = http.client.HTTPSConnection(urlRoot,443)
    conn.request('GET',urlSuffix)
    r= conn.getresponse()
    output = r.read()
    conn.close()
    return output


def getAttributeIfExists(attrb,key):
    for name, value in attrb:
        if name == key:
            return value
        
    return ''


class ImageURLClass:
    def __init__(self,ID,title,url,size):
        self.ID = ID
        self.title = title
        self.url = url
        self.size = size
    
    def logImage(self):
        with open(downloadLogPath, 'a') as f:
            line = str(self.size/1024) + '\t' + self.ID + '\t' + self.url + ' \t' + self.title + '\n'
            f.write(line)
            f.flush()
            f.close()
            
        
    

class ImageLinkScraper(HTMLParser):
    parenttag = ''
    parentattr = []
    link = ''
    imgid = ''
    title = ''
    
    def handle_starttag(self, tag, attrs):        
        if tag == 'a' and  self.parenttag == 'h2':
            
            self.link = getAttributeIfExists(attrs,'href')
            self.imgid = getAttributeIfExists(attrs, 'title')
            #print("Got image page | Link:" + self.link + ' | ID:' + self.imgid)
                    
        self.parenttag = tag
        self.parentattr = attrs
        

    def handle_endtag(self, tag):
        #print("Encountered an end tag :", tag)
        pass

    def handle_data(self, data):
        #print('DATA - parenttag: ' + str(self.parenttag) + ' - parentattr:' + str(self.parentattr))
        try:
            if self.parenttag == 'span' and getAttributeIfExists(self.parentattr,'class') == 'entry-title hidden':
                self.title = data
                #print('Got title:',data)
        except Exception as a:
            print(a)
        
    def returnData(self):
        return self.link,self.imgid,self.title


class ImageScraper(HTMLParser):
    link = ''
    def handle_starttag(self, tag, attrs):
        if tag == 'a' and  getAttributeIfExists(self.parentattr,'class') == 'wp-caption aligncenter':
            self.link = getAttributeIfExists(attrs,'href')
            #print("Got DL link:" + self.link)
                    
        self.parenttag = tag
        self.parentattr = attrs
    
    def handle_endtag(self, tag):
        pass
    
    def handle_data(self, data):
        pass
        
    def returnData(self):
        return self.link






rootHtml = getPageHtml(pageRoot)

pageNumberDividerPhrase = "next page-numbers"

pageNumberSplit = str(rootHtml).split(pageNumberDividerPhrase)
pageNumberStr = pageNumberSplit[0]
pgNoIndex = pageNumberStr.rfind("</a>")
pgNoIndexEnd = pgNoIndex
pgNoIndexStart = pageNumberStr.rfind('">')
pgNoIndexStart = pgNoIndexStart + 2
pageNumber = pageNumberStr[pgNoIndexStart:pgNoIndexEnd]

print("There are ",pageNumber," pages in total.")

maxPages = 0
try:
    maxPages = int(pageNumber)
except TypeError:
    print('Max page number parse error')
    sys.exit(1)
    

start = startingPageNumber

if start <= 0 or start > maxPages or start + pageCount > maxPages + 1:
    print('Page number error')
    sys.exit(1)

if pageCount != -1:
    end = start + pageCount
else:
    end = maxPages + 1

for p in range(start,end):
    print("\n---Page: ",p,"---\n\n")
    
    pageHtml = getPageHtml(pageRoot + pageSuffix + str(p))
    pageSplit = str(pageHtml).split('</article>')
    a = 1
    
    for l in pageSplit[0:]:
        if '<article' in l:
            imgLinkScraper = ImageLinkScraper()
            imgLinkScraper.feed(l)
            link, ID, name = imgLinkScraper.returnData()
            imgLinkScraper.close()
            
            if link != '':
                totalImages = totalImages + 1
                print("Downloading: ",totalImages)
                
                imagePageHtml = getPageHtml(link)
                
                
                imgScraper = ImageScraper()
                imgScraper.feed(str(imagePageHtml))
                imgDlLink = imgScraper.returnData()
                image = getPageHtml(imgDlLink)
                dlBytes = len(image)
                
                imgObj = ImageURLClass(ID, name, imgDlLink, dlBytes)
                imgObj.logImage()
                
                totalBytes = totalBytes + dlBytes
                
                imageSrc = ID + ".jpg"
                with open(downloadFolder + imageSrc, 'wb') as f:
                    f.write(image)
                    f.flush()
                    f.close()
                
                
                    
                
                
print(str(totalBytes/1024/1024)," MB downloaded.")
        
        