import requests
import sys
import re
import time
import random
reload(sys)
sys.setdefaultencoding('utf-8')
data = {'m':'saveRxKc', 'token':'8c590069142208a81565208971f13111', \
        'p_sort.p1': 'bkskyl','p_sort.asc1':'false','p_sort.asc2': 'true', \
        'p_xnxq': '2016-2017-2','tokenPriFlag':'rx','p_kkdwnm':'024',\
        'p_rx_id':'2016-2017-2;00740143;90;','goPageNumber':'1'}
url = 'https://sslvpn.tsinghua.edu.cn/,DanaInfo=zhjwxk.cic.tsinghua.edu.cn+xkBks.vxkBksXkbBs.do'
headers = {
           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',\
           'Accept-Encoding':'gzip, deflate',\
           'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',\
           'Cache-Control':'max-age=0',\
           'Connection':'keep-alive',\
           'Content-Length':'262',\
           'Content-Type':'application/x-www-form-urlencoded',\
           'Cookie':'DSSignInURL=/; DSID=c9d9a5f3a88c5630037df1de14f9c12f; DSFirstAccess=1481946270; DSLastAccess=1481949514',\
           'Host':'zhjwxk.cic.tsinghua.edu.cn',\
           'Origin':'http://zhjwxk.cic.tsinghua.edu.cn',\
           'Referer':'http://zhjwxk.cic.tsinghua.edu.cn/xkBks.vxkBksXkbBs.do',\
           'Upgrade-Insecure-Requests':'1',\
           'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
course = [{'name':'number theory','m':'saveXxKc','tokenPriFlag':'xx','p_xxl_id':'2016-2017-2;10430792;0;'},\
          {'name':'circuit design','m':'saveXxKc','tokenPriFlag':'xx','p_xxl_id':'2016-2017-2;30240353;0;'}]

ff = open('output.html', 'r').read()
n = re.search('<input type="hidden" name="token" value="(\w+)"', ff)
f = file('output.txt','w+')
if n:
     f.write(n.group(1))
f.close()
if n:
     data['token'] = n.group(1)
index = random.randint(0, len(course) - 1)

data['m'] = course[index]['m']
data['tokenPriFlag']= course[index]['tokenPriFlag']
data['p_xxl_id']= course[index]['p_xxl_id']
r = requests.post(url, data=data, headers=headers)
f = file('output.html','w')
f.write(r.text)
f.close()
f = file('output.txt','r+')
f.write(time.strftime("%Y-%m-%d %H:%M:%S \n",time.localtime(time.time())))
message = re.search('showMsg(.+$)', r.text)
if message:
     f.write(message(1))

if n:
     f.write(n.group(1))
f.close()
time.sleep(10)

