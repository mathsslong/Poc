# Title: wechat push CVE-2020
# Date: 2020-5-9
# Exploit Author: weixiao9188
# Version: 4.0
# Tested on: Linux,windows
# coding:UTF-8
import requests
import json
import time
import os
import pandas as pd
time_sleep = 20 #ÿ��20����ȡһ��
while(True):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400"}
    #�ж��ļ��Ƿ����
    datas = []
    response1=None
    response2=None
    if os.path.exists("olddata.csv"):
        #����ļ�������ÿ����ȡ10��
        df = pd.read_csv("olddata.csv", header=None)
        datas = df.where(df.notnull(),None).values.tolist()#����ȡ�����������е�nanת��ΪNone
        response1 = requests.get(url="https://api.github.com/search/repositories?q=CVE-2020&sort=updated&per_page=10",
                                 headers=headers)
        response2 = requests.get(url="https://api.github.com/search/repositories?q=RCE&ssort=updated&per_page=10",
                                 headers=headers)

    else:
        #��������ȡȫ��
        datas = []
        response1 = requests.get(url="https://api.github.com/search/repositories?q=CVE-2020&sort=updated&order=desc",headers=headers)
        response2 = requests.get(url="https://api.github.com/search/repositories?q=RCE&ssort=updated&order=desc",headers=headers)

    data1 = json.loads(response1.text)
    data2 = json.loads(response2.text)
    for j in [data1["items"],data2["items"]]:
        for i in j:
            s = {"name":i['name'],"html":i['html_url'],"description":i['description']}
            s1 =[i['name'],i['html_url'],i['description']]
            if s1 not in datas:
                #print(s1)
                #print(datas)
                params = {
                     "title":s["name"],
                    "desp":" ����:"+str(s["html"])+"\n���"+str(s["description"])
                }
                print("��ǰ����Ϊ"+str(s)+"\n")
                print(params)
                requests.get("https://sctapi.ftqq.com/SCT142424TxKKLyofXmKcUhn0ys3yZ48f6.send",params=params,timeout=10)
                #time.sleep(1)#�Է�����̫��
                print("�������!")
                datas.append(s1)
            else:
                pass
                #print("�����Ѵ���!")
    pd.DataFrame(datas).to_csv("olddata.csv",header=None,index=None)
    time.sleep(time_sleep)