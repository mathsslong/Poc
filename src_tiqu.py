import requests
from lxml import etree

#yeshu=input("����Ҫ�����ҳ:")

def src_tiqu(yeshu):
    for i in range(1, int(yeshu+1)):
        url = 'https://src.sjtu.edu.cn/list/?page=' + str(i)
        print("��ȡ->",str(i)+"ҳ��")
        data = requests.get(url).content
        print(data.decode('utf-8'))
        soup = etree.HTML(data)
        result = soup.xpath('//td[@class=" "]/a/text()')
        results = '\n'.join(result)
        resultss = results.split()
        # print(resultss)
        # �����д���ļ�
        for edu in resultss:
            print(edu)
            with open(r'src_edu.txt', 'a+', encoding='utf-8') as f:
                f.write(edu + '\n')


if __name__ == '__main__':
    yeshu = input("����Ҫ�����ҳ:")
    src_tiqu(yeshu)