#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import requests
import json


#��������ID
task_new_url='http://127.0.0.1:8775/task/new'
resp=requests.get(task_new_url)
task_id=resp.json()['taskid']
#print(resp.content.decode('utf-8'))
#print(resp.json()['taskid'])


#��������ID��������Ϣ(ɨ����Ϣ)
data={
    'url':'http://127.0.0.1/sqli-labs-master/Less-2/?id=1'
}
headers={
    'Content-Type':'application/json'
}


task_set_url='http://127.0.0.1:8775/option/'+task_id+'/set'
task_set_resp=requests.post(task_set_url,data=json.dumps(data),headers=headers)
#print(task_set_resp.content.decode('utf-8'))


#������ӦID��ɨ������
task_start_url='http://127.0.0.1:8775/scan/'+task_id+'/start'
task_start_resp=requests.post(task_start_url,data=json.dumps(data),headers=headers)
#print(task_start_resp.content.decode('utf-8'))


#��ȡ��ӦID��ɨ��״̬
task_status_url='http://127.0.0.1:8775/scan/'+task_id+'/status'
task_status_resp=requests.get(task_status_url)
print(task_status_resp.content.decode('utf-8'))