import requests
from lxml import etree
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

if __name__ == '__main__':
    url = "https://www.bjcpez.net/"
    response = requests.get(url=url,headers=header).text
    etr = etree.HTML(response)
    titles = etr.xpath('/html/head/meta[@name="description"]/@content')
    for title in titles: 
        print(title)