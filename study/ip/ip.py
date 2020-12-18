import requests
def baidu():
    headers = {
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    }
    #url = "http://www.baidu.com/s?wd=ip"
    url = "http://ip.293.net/"
    response = requests.get(url=url,headers=headers,proxies={"http":"http://114.239.42.137:9999"}).text
    with open("baidu.html","w",encoding="utf-8") as target:
        target.write(response)

def ws():
    url = 'https://w3schools.com/python/demopage.php'

    #find a free proxy address and send your request via that proxy:
    x = requests.get(url)

    #'demopage.php' will print the ip address of the proxy instead of your ip:
    print(x.text)
baidu()
