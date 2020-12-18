import requests
from json import dumps
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

def getCodes(section):
    url = "https://api.61financial.com.au/industries/?industry="+section
    response = requests.get(url=url,headers=headers)
    data = response.json()
    i = 0
    stock_list = data["stockmarketdata"]
    output = {
       "data":[] 
    }
    for stock in stock_list:
        code = stock['code']
        price = stock['last']
        data = {
            "code":code
        }
        output["data"].append(data)
    
    with open("codes/"+section+".json","w",encoding="utf-8") as target:
        target.write(dumps(output))
        
if __name__ == '__main__':
    sections = ["Materials","SS","Energy","DF","PBLS","HCES","RE","ME","Retailing","FBT","CG","CPS","THE","Utilities","TS"]
    sections += ["CS","Transportation","Banks","CDA","Insurance","AC","FSR","HPP","SSE","NA"]
    for section in sections:
        print(section)
        getCodes(section=section)