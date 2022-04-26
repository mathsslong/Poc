# Title: wechat push CVE-2020
 
# Date: 2020-5-9
 
# Exploit Author: weixiao9188
 
# Version: 4.0
 
# Tested on: Linux,windows
 
# cd /root/sh/git/ && nohup python3 /root/sh/git/git.py &
 
# coding:UTF-8
 
import requests
 
import json
 
import time
 
import os
 
import pandas as pd
 
time_sleep = 60 #每隔 20 秒爬取一次
 
while(True):
 
headers1 = {
 
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)
Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400"}
 
#判断文件是否存在
 
datas = []
 
response1=None
 
response2=None
 
if os.path.exists("olddata.csv"):
 
#如果文件存在则每次爬取 10 个
 
df = pd.read_csv("olddata.csv", header=None)
 
datas = df.where(df.notnull(),None).values.tolist()#将提取出来的数据中的 nan 转化为 None
 
requests.packages.urllib3.disable_warnings()
 
response1 = requests.get(url="https://api.github.com/search/repositories?q=CVE2020&sort=updated&per_page=10",headers=headers1,verify=False)
 
response2 =
 
requests.get(url="https://api.github.com/search/repositories?q=RCE&ssort=updated&per_page=10",hea
 
ders=headers1,verify=False)
 
else:
 
#不存在爬取全部
 
datas = []
 
requests.packages.urllib3.disable_warnings()
 
response1 = requests.get(url="https://api.github.com/search/repositories?q=CVE2020&sort=updated&order=desc",headers=headers1,verify=False)
 
response2 =
 
requests.get(url="https://api.github.com/search/repositories?q=RCE&ssort=updated&order=desc",heade
 
rs=headers1,verify=False)
 
data1 = json.loads(response1.text)
 
data2 = json.loads(response2.text)
 
for j in [data1["items"],data2["items"]]:
 
for i in j:
 
s = {"name":i['name'],"html":i['html_url'],"description":i['description']}
 
s1 =[i['name'],i['html_url'],i['description']]
 
if s1 not in datas:
 
#print(s1)