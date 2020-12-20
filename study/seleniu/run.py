from selenium import webdriver
from lxml import etree
import requests
bro = webdriver.Chrome(executable_path="chromedriver.exe")
main_page = "https://www.pearvideo.com/category_5"
url = "https://www.pearvideo.com/video_1712055"
#let chrome send request for given url
bro.get(url)
#get current source code for current page
page_text = bro.page_source

video_url = etree.HTML(page_text)
url = video_url.xpath('//*[@id="JprismPlayer"]/video/@src')[0]

video = requests.get(url).content
with open("video/视频.mp4","wb") as target:
    target.write(video)