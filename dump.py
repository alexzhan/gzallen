# -*- coding:utf-8 -*-
import sys
import time
import requests
import encodings

reload(sys)
sys.setdefaultencoding('utf8')

headers = {}
cookies = {}

for i in range(1, 119):
    url = 'http://fanfou.com/~RLhcIDBjZAM/p.%s' % i
    r = requests.get(url, headers = headers, cookies = cookies)
    print r.text

    f = open("%s.html" % i, "w")
    f.write(r.text)
    f.close()

    time.sleep(10)
