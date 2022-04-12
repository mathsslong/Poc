#!/usr/bin/python3
# -*- coding: UTF-8 -*-


import socket,os,time,sys,whois
      #ip��ѯ
      def ip_check(url):
          ip=socket.gethostbyname(url)
          print(ip)
          print('------------------------------------++++++-------------------------------------------')
      #whois��ѯ
      def whois_check(url):
          data = whois.whois(url)
          print(data)
          print('------------------------------------++++++-------------------------------------------')

      #CDN�ж�-���÷���IP���������ж�
      def cdn_check(url):
          ns="nslookup "+url
          #data=os.system(ns)
          #print(data) #����޷���ȡ����
          data=os.popen(ns,"r").read()
          if data.count(".")>8:
              print("����CDN")
          else:
              print("������CDN")
          print('------------------------------------++++++-------------------------------------------')
      #��������ѯ-
      #1.�����ֵ���ر��ƽ��в�ѯ
      #2.���õ������ӿڽ��в�ѯ
      def zym_list_check(url):
          url=url.replace("www.","")
          for zym_list in open("../../plug-in/dic.txt"):
              zym_list=zym_list.replace("\n","")
              zym_list_url=zym_list+"."+url
              try:
                  ip=socket.gethostbyname(zym_list_url)
                  print(zym_list_url+"->"+ip)
                  time.sleep(0.1)
              except Exception as e:
                  time.sleep(0.1)
          print('------------------------------------++++++-------------------------------------------')

      def zym_api_check(url):
          url=url.replace("www.", "")


      #�˿�ɨ��
      def port_check(url):
          ip = socket.gethostbyname(url)
          #ip="192.168.76.155"
          #ports={'21','22','135','443','445','80','1433','3306',"3389",'1521','8000','7002','7001','8080',"9090",'8089',"4848}
          server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
          #for port in ports:
          try:
              data=server.connect_ex((ip, 80))
              if data==0:
                  print(ip+":"+str(80)+"|open")
              else:
                  print(ip+":"+str(80)+"|close")
                  pass
          except Exception as err:
                  print("error")
          print('------------------------------------++++++-------------------------------------------')

      #ϵͳ�ж�-
      #1.����TTLֵ�����ж�
      #2.���ڵ������ű������ж�
      def os_check(url):
          data = os.popen("nmap\\nmap -O "+url, "r").read()
          print(data)
          print('------------------------------------++++++-------------------------------------------')

      if __name__ == '__main__':
          print("Test��python test.py www.dudu.com all")
          url = sys.argv[1]
          check = sys.argv[2]
          #print(url +"\n"+ check)
          if check=="all":
              ip_check(url)
              whois_check(url)
              port_check(url)
              cdn_check(url)
              os_check(url)
              zym_list_check(url)