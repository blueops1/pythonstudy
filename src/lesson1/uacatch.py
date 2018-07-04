'''
Created on 2018年7月4日

@author: user
'''
import unittest,urllib.request,re


class Test(unittest.TestCase):
    testurl = "http://www.baidu.com"
    
    def testUA(self):
        pass
    def UAcatch(self,testurl):
        data = urllib.request.urlopen(testurl)
        pat = "://(.*?)/"
        strlist = re.findall(pat, data, re.S)
        for x in strlist:
            print(x)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testUA']
    unittest.main()