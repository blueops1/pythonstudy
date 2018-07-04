'''
Created on 2018年7月4日

@author: user
'''
import urllib.request,re

def UAcatch(testurl):
    opener = urllib.request.build_opener()
    UA = ("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36")
    opener.addheaders=[UA]
    urllib.request.install_opener(opener)    
    data = urllib.request.urlopen(testurl).read().decode("utf-8","ignore")
    x = len(data)
    #print(data)
    pat = "href=\"(htt(p|ps)://.*?)\""
    strlist = re.findall(pat,data,re.S)
    #print(strlist)
    for x in strlist:
        print(x[0])
        
    #urllib.reque

UAcatch("http://www.baidu.com")