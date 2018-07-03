print('This is lesson 1')
print('egit is successful!')
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