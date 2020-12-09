import requests
import re
def download_image(url,i):
    image = requests.get(url=url).content
    with open(f"{i}.png","wb") as f:
        f.write(image)

def get_page():
    url = "https://www.qiushibaike.com/imgrank/"
    header = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    page = requests.get(url=url,headers=header).text
    return page

def getImageUrl(page):
    res = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
    url = re.findall(res,page,re.S)
    return url

if __name__ == '__main__':
    url = "https://pic.qiushibaike.com/system/pictures/12385/123854616/medium/0FQC6HEDF619T6HA.jpg"
    image = get_page()
    urls = getImageUrl(image)
    with open("image_url.txt","w",encoding="utf-8") as target:
        target.write(str(urls))
    i = 0
    for image_url in urls:
        temp = "https:"+image_url
        download_image(temp,i)
        i+=1
