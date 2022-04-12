import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from tqdm import tqdm

mylist = []
user = {'user-agent': 'Mozilla/5.0'}
for i in tqdm(range(1,2173)):#共有2172页需要爬取，设置url链接中page的参数，其中tqdm用于进度条
    url = 'https://src.sjtu.edu.cn/list/?page='+str(i)
    r = requests.get(url, headers=user)#请求页面
    r.encoding = r.apparent_encoding
    html = BeautifulSoup(r.text, 'html.parser')
    mytable=html.find('table')#找到页面中的表格
    mytr=mytable.find_all('tr')#找到表格中所有行
    mytr.pop(0)#去掉数据中表头那一行
    #对每一行各个单元格处理
    for m in mytr:
        tds=m('td')#将这一行所有单元格保存在tds中
        j=tds[1].a.string.split()[0]#第二个单元格（这一个单元格保存的数据为xx学校存在xx漏洞）包围在<a>标签中，将其中的字符串取出来，并去掉空格换行等
        jj=j.split('存在')#将改字符串通过存在分割
        #因为里面的数据有一点不是xx学校存在xx漏洞的形式，需要分别处理
        if(len(jj)==2):#如果有存在这个字符
            ty = jj.pop()#保存漏洞类型
            school = jj.pop()#保存学校
        else:#如果没有，将漏洞类型设为其它
            school=jj.pop()
            ty='其他漏洞'
        #将这一行所有内容存在mylist中
        mylist.append([tds[0].string.split('-')[0],school,ty,tds[2].string,tds[3].string])#第一个单元格通过-分割，只取年份
    time.sleep(2)#一方面降低爬取速度，一方面用于显示爬取进度条
my=pd.DataFrame(mylist,columns=['年份','学校','类型','程度','提交人'])
my.to_excel(r'C:\Users\Desktop\my.xlsx')