#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import requests
import json
import time

def sqlmapapi(url):
    data = {
        #'url': 'http://127.0.0.1/sqli-labs-master/Less-2/?id=1'
        'url':url
    }
    headers = {
        'Content-Type': 'application/json'
    }

    #创建新任务记录任务ID
    task_new_url = 'http://127.0.0.1:8775/task/new'
    resp = requests.get(task_new_url)
    task_id = resp.json()['taskid']
    # print(resp.content.decode('utf-8'))
    if 'success' in resp.content.decode('utf-8'):
        print('sqlmapapi task create success!')
        #设置任务ID扫描信息
        task_set_url = 'http://127.0.0.1:8775/option/' + task_id + '/set'
        task_set_resp = requests.post(task_set_url, data=json.dumps(data), headers=headers)
        # print(task_set_resp.content.decode('utf-8'))

        if 'success' in task_set_resp.content.decode('utf-8'):
            print('sqlmapapi task set success!')
            #开始扫描对应ID任务
            task_start_url = 'http://127.0.0.1:8775/scan/' + task_id + '/start'
            task_start_resp = requests.post(task_start_url, data=json.dumps(data), headers=headers)
            # print(task_start_resp.content.decode('utf-8'))

            if 'success' in task_start_resp.content.decode('utf-8'):
                print('sqlmapapi task start success!')
                #一直循环查看对应ID的扫描状态！！！
                while 1:
                    task_status_url = 'http://127.0.0.1:8775/scan/' + task_id + '/status'
                    task_status_resp = requests.get(task_status_url)
                    #print(task_status_resp.content.decode('utf-8'))
                    time.sleep(1)
                    if 'running' in task_status_resp.content.decode('utf-8'):
                        print(url+'->sqlmapapi taskid scan running')
                        pass
                    else:
                        print('sqlmapapi scan end')
                        #查看扫描结果并将其写入到文件中
                        task_data_url = 'http://127.0.0.1:8775/scan/' + task_id + '/data'
                        task_data_resp = requests.get(task_data_url).content.decode('utf-8')
                        #print(task_data_resp.content.decode('utf-8'))
                        with open(r'scan_result.txt','a+') as f:
                            f.write(url+'\n')
                            f.write(task_data_resp+'\n'+'\n')
                            f.write('=========python sqlmapapi by shanlong========='+'\n'+'\n')
                        #如果结束删除ID
                        task_delete_url='http://127.0.0.1:8775/task/' + task_id + '/delete'
                        task_delete_resp=requests.get(task_delete_url)
                        if 'success' in task_delete_resp.content.decode('utf-8'):
                            print('sqlmapapi task delete success!')
                        break



if __name__ == '__main__':
    print('scanurl checking OK ......')
    for url in open('url.txt'):
        url=url.replace('\n','')
        sqlmapapi(url)