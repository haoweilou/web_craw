import requests
from bs4 import BeautifulSoup
import json
import re
if __name__ == '__main__':
    url = "https://www.sydneytoday.com/job_information-ha0-na0-ex0-hy0-p"
    header = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    print("Start crawing:")
    response = requests.get(url=url+"1",headers=header)
    soup = BeautifulSoup(response.text,'lxml')


    count = 0
    names = soup.select(".yp-list-title")
    hrefs = soup.select('.yp-list > .yp-list-item > .row > .col-xs-12')
    output = []
    for p,h in zip(names,hrefs):
        temp_url = h.find("div",class_=None)
        temp_url = temp_url.select("div > a")[0]['href']
        temp_url = "https:"+temp_url
        specific_data = requests.get(temp_url,headers=header).text
        retext = '<div class="yp-contact-name">(.*)</div>'
        name = re.findall(retext,specific_data)

        sentenct = p.get_text() + "     " + name[0]
        output.append(sentenct)
        count+=1

    for i in range(2,11):
        response = requests.get(url=url+str(i),headers=header).json()
        posts = response['data']['rows']
        for post in posts:
            temp_url = f"https://www.sydneytoday.com/job_information/{post['_id']}"

            specific_data = requests.get(temp_url,headers=header).text
            retext = '<div class="yp-contact-name">(.*)</div>'
            name = re.findall(retext,specific_data)
            try:
                sentenct = post['title'] + "     " + name[0]
                output.append(sentenct)
            except IndexError:
                continue
            count+=1
    with open("today.txt","a",encoding="utf-8") as target:
        for item in output:
            target.write(item+"\n")
    print(f"End crawing: {count}")