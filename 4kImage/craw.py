import requests
from lxml import etree
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

def downLoadPage(number):
    print(f"开始爬取第{number}页")
    if(number == 1):
        url = "http://pic.netbian.com/4kmeinv"
    else:
        url = f"http://pic.netbian.com/4kmeinv/index_{number}.html"
    response = requests.get(url=url,headers=header)
    #print(response.encoding)
    response = response.text
    tree = etree.HTML(response)
    hrefs = tree.xpath('//div[@class="slist"]/ul/li/a/img/@src')
    names =  tree.xpath('//div[@class="slist"]/ul/li/a/img/@alt')

    for h,n in zip(hrefs,names):
        n = "image/"+n+".jpg"
        image_url = "http://pic.netbian.com"+h
        image = requests.get(url=image_url,headers=header).content
        n = n.encode('iso-8859-1').decode("gbk")
        with open(n,"wb") as target:
            target.write(image)
        print("     "+n+"完成")

if __name__ == '__main__':
    i = 0
    for i in range(1,14):
        downLoadPage(i)
        i+=1
    print(f"一共爬取{i}张照片")