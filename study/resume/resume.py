import requests
from lxml import etree
headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}
def downLoadFile(url,name):
    full = "https:"+url
    response = requests.get(url=full,headers=headers).text
    et = etree.HTML(response)
    path = '/html//div[@id="down"]/div[@class="clearfix mt20 downlist"]/ul/li/a/@href'
    hrefs = et.xpath(path)[0]
    response = requests.get(url=hrefs,headers=headers).content
    with open("format/"+name+".rar","wb") as target:
        target.write(response)

if __name__ == '__main__':
    for i in range(1,4):
        if i == 1:
            url = "https://sc.chinaz.com/jianli/free.html"
        else:
            url = f"https://sc.chinaz.com/jianli/free_{i}.html"
        html = requests.get(url,headers=headers).text
        etr = etree.HTML(html)

        hrefs = etr.xpath('/html/body/div[@class="bggray clearfix pt20"]/div[@class="sc_warp  mt20"]/div[@id="main"]/div/div/a/@href')
        names = etr.xpath('/html/body/div[@class="bggray clearfix pt20"]/div[@class="sc_warp  mt20"]/div[@id="main"]/div/div/a/img/@alt')
        for item,name in zip(hrefs,names):
            name = name.encode('iso-8859-1').decode("utf-8")
            print(item,name)
            downLoadFile(item,name)