#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import requests
import json


#创建任务ID
task_new_url='http://127.0.0.1:8775/task/new'
resp=requests.get(task_new_url)
task_id=resp.json()['taskid']
#print(resp.content.decode('utf-8'))
#print(resp.json()['taskid'])


#设置任务ID的配置信息(扫描信息)
data={
    'url':'http://127.0.0.1/sqli-labs-master/Less-2/?id=1'
}
headers={
    'Content-Type':'application/json'
}


task_set_url='http://127.0.0.1:8775/option/'+task_id+'/set'
task_set_resp=requests.post(task_set_url,data=json.dumps(data),headers=headers)
#print(task_set_resp.content.decode('utf-8'))


#启动对应ID的扫描任务
task_start_url='http://127.0.0.1:8775/scan/'+task_id+'/start'
task_start_resp=requests.post(task_start_url,data=json.dumps(data),headers=headers)
#print(task_start_resp.content.decode('utf-8'))


#获取对应ID的扫描状态
task_status_url='http://127.0.0.1:8775/scan/'+task_id+'/status'
task_status_resp=requests.get(task_status_url)
print(task_status_resp.content.decode('utf-8'))