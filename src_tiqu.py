import requests
from lxml import etree

#yeshu=input("您想要搞多少页:")

def src_tiqu(yeshu):
    for i in range(1, int(yeshu+1)):
        url = 'https://src.sjtu.edu.cn/list/?page=' + str(i)
        print("提取->",str(i)+"页数")
        data = requests.get(url).content
        print(data.decode('utf-8'))
        soup = etree.HTML(data)
        result = soup.xpath('//td[@class=" "]/a/text()')
        results = '\n'.join(result)
        resultss = results.split()
        # print(resultss)
        # 将结果写入文件
        for edu in resultss:
            print(edu)
            with open(r'src_edu.txt', 'a+', encoding='utf-8') as f:
                f.write(edu + '\n')


if __name__ == '__main__':
    yeshu = input("您想要搞多少页:")
    src_tiqu(yeshu)