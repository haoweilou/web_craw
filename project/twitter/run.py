import requests
from lxml import etree

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

if __name__ == '__main__':
    url = "https://twitter.com/search?q=%23BBL10&src=trend_click&vertical=trends"
    response = requests.get(url=url,headers=headers)
    etre = etree.HTML(response.text)
    etr = etre.xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/section/div/div/div[1]/div/div/article/div')
    print(etr)
    for div in etr:
        print(div)