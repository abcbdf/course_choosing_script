import requests
data = {'m':'kylSearch', 'page':'-1', 'token':'ea85abd23423476ff2a81bb8c714906df0c2a', 'p_sort.asc1': 'true', 'p_sort.asc2': 'true', 'p_xnxq': '2016-2017-2', 'p_skjc': '1', 'goPageNumber': '1'}
url = 'http://zhjwxk.cic.tsinghua.edu.cn/xkBks.vxkBksJxjhBs.do'
headers = {'cookie': 'JSESSIONID=cef7bXjgX52I0exWh9fKv; thuwebcookie=990146470.20480.0000'}
r = requests.post(url, data=data, headers=headers)
print(r.text)
