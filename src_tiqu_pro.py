import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from tqdm import tqdm

mylist = []
user = {'user-agent': 'Mozilla/5.0'}
for i in tqdm(range(1,2173)):#����2172ҳ��Ҫ��ȡ������url������page�Ĳ���������tqdm���ڽ�����
    url = 'https://src.sjtu.edu.cn/list/?page='+str(i)
    r = requests.get(url, headers=user)#����ҳ��
    r.encoding = r.apparent_encoding
    html = BeautifulSoup(r.text, 'html.parser')
    mytable=html.find('table')#�ҵ�ҳ���еı��
    mytr=mytable.find_all('tr')#�ҵ������������
    mytr.pop(0)#ȥ�������б�ͷ��һ��
    #��ÿһ�и�����Ԫ����
    for m in mytr:
        tds=m('td')#����һ�����е�Ԫ�񱣴���tds��
        j=tds[1].a.string.split()[0]#�ڶ�����Ԫ����һ����Ԫ�񱣴������ΪxxѧУ����xx©������Χ��<a>��ǩ�У������е��ַ���ȡ��������ȥ���ո��е�
        jj=j.split('����')#�����ַ���ͨ�����ڷָ�
        #��Ϊ�����������һ�㲻��xxѧУ����xx©������ʽ����Ҫ�ֱ���
        if(len(jj)==2):#����д�������ַ�
            ty = jj.pop()#����©������
            school = jj.pop()#����ѧУ
        else:#���û�У���©��������Ϊ����
            school=jj.pop()
            ty='����©��'
        #����һ���������ݴ���mylist��
        mylist.append([tds[0].string.split('-')[0],school,ty,tds[2].string,tds[3].string])#��һ����Ԫ��ͨ��-�ָֻȡ���
    time.sleep(2)#һ���潵����ȡ�ٶȣ�һ����������ʾ��ȡ������
my=pd.DataFrame(mylist,columns=['���','ѧУ','����','�̶�','�ύ��'])
my.to_excel(r'C:\Users\Desktop\my.xlsx')