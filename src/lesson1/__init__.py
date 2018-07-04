print('This is lesson 1')
print('egit is successful!1')
print('retry the key')
print('this line is type at home_pc!')
dictofpeople = [['necho','12345678910'],['alise','98765432101']]
for people in dictofpeople:
    for name in people:
        print(name)
import urllib.request
data = urllib.request.urlopen("http://www.baidu.com").read().decode("utf-8","ignore")
x = len(data)
import re
pat = "<title>(.*?)</title>"
rst = re.findall(pat,data,re.S)
print(rst)      
urllib.request.urlretrieve("https://www.jd.com/", filename="d:/test.html") 

url = "https://www.qiushibaike.com"

opener = urllib.request.build_opener()

UA = ("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36")
#Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36
#涓浗中国
opener.addheaders=[UA]
urllib.request.install_opener(opener)
data = urllib.request.urlopen(url).read().decode("utf-8","ignore")
#print(data)
urllib.request.urlretrieve("http://www.jd.com", filename="d:/test.html")

