import requests
from lxml import etree
from requests import Session
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

def downloadVideo(id):
    url = "https://www.pearvideo.com/"+id
    session = Session()
    session.get(url=url,headers=headers)
    each = f"https://www.pearvideo.com/videoStatus.jsp?contId=1712055&mrd=0.9764294721577391"
    a = session.get(url=each,headers=headers).json()

    #ert = etree.HTML(response)
    #url = ert.xpath('//*[@id="JprismPlayer"]/video/@src')
    print(a)
if __name__ == '__main__':
    url = "https://www.pearvideo.com/category_5"
    response = requests.get(url=url,headers=headers).text
    et = etree.HTML(response)
    lis = et.xpath('//*[@id="categoryList"]/li/div/a/@href')
    for id in lis:
        downloadVideo(id)
        break
