import requests
from bs4 import BeautifulSoup

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

def getText(url):
    output = ""
    response = requests.get(url=url,headers=header).text
    soup = BeautifulSoup(response,features='lxml')
    texts = soup.select(".chapter_content > p")
    for text in texts:
        output+=text.text + "\n"
    return output

if __name__ == '__main__':
    url = "https://www.shicimingju.com/book/sanguoyanyi.html"
    response = requests.get(url=url,headers=header).text
    soup = BeautifulSoup(response,"lxml")
    titles = soup.select(".book-mulu > ul > li")

    for title in titles:
        titlename = title.text
        href = title.a['href']
        sub_url = "https://www.shicimingju.com"+href
        text = getText(sub_url)
        with open("threekindom.txt","a",encoding="utf-8") as f:
            f.write(titlename+"\n"+text)