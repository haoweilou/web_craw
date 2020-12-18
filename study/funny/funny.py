import requests
import re
from datetime import datetime,timedelta
#下载图片
def download_image(url,i):
    image = requests.get(url=url).content
    with open(f"image/{i}.png","wb") as f:
        f.write(image)
#得到第N个page,返回HTML
def get_page(page):
    url = "https://www.qiushibaike.com/imgrank/page/"+str(page)+"/"
    header = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    page = requests.get(url=url,headers=header).text
    return page
#在html文件中获得图片的URL
def getImageUrl(page):
    res = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
    url = re.findall(res,page,re.S)
    return url

if __name__ == '__main__':
    image_num = 0
    now = datetime.now()
    for i in range(1,11):
        timetaken = datetime.now()-now
        print(f"开始请求第{i}页,{timetaken}")
        image = get_page(i)
        timetaken = datetime.now()-now
        print(f"第{i}页请求成功,{timetaken}")
        urls = getImageUrl(image)
        timetaken = datetime.now()-now
        print(f"开始下载图片,{timetaken}")
        #记录图片URL
        with open("image_url.txt","a",encoding="utf-8") as target:
            target.write(str(urls))
        for image_url in urls:
            temp = "https:"+image_url
            download_image(temp,image_num)
            image_num+=1
        timetaken = datetime.now()-now
        print(f"图片下载结束,{timetaken}")
