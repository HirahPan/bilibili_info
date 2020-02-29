import requests
import re
import pandas as pd
url = 'http://www.bilibili.com/video/av85951067?p={}'
headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
time_list=[]
res = requests.get(url.format(1),headers=headers).content.decode()
timelength_pattern = re.compile('"timelength":(.*?),"accept_format"')
title_pattern =re.compile('"part":"(.*?)"')
title =title_pattern.findall(res)
for i in range(1,len(title)+1):
    get_time = requests.get(url.format(i),headers=headers).content.decode()
    timelength_pattern = re.compile('"timelength":(.*?),"accept_format"')
    time_list.append(eval(timelength_pattern.findall(get_time)[0])/60/1000)
t1 = pd.Series(time_list)
t2 = pd.Series(title)
d = {
    "章节名称":t2,
    "时长(单位：min）":t1,
}
data = pd.DataFrame(d)
data.to_excel('pmp_info.xlsx',encoding='utf-8',index=None)

