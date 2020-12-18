import requests
import json
from datetime import datetime, timedelta

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

class StockSubscriber():
    def __init__(self):
        self.sections = ["Materials","SS","Energy","DF","PBLS","HCES","RE","ME","Retailing","FBT","CG","CPS","THE","Utilities","TS"]
        self.sections += ["CS","Transportation","Banks","CDA","Insurance","AC","FSR","HPP","SSE","NA"]

    def gedPriceForSection(self,section):
        fd = open(f"codes/{section}.json","r")
        data = json.load(fd)
        lis = data['data']
        lis = sorted(lis,key=lambda i : i["code"])
        now = datetime.now()
        price = []
        for item in lis:
            code = item['code']
            print(f"Read price for {code}")
            priceData = self.getPrice(code)
            price.append(priceData)
        timetaken = (datetime.now()-now).seconds
        return timetaken, price

    def orderCodes(self):
        fd =  open("codes/ALL.json","w")
        codes = []

        for section in self.sections:
            with open(f"codes/{section}.json","r",encoding="utf-8") as f:
                data = json.load(f)
                code = data['data']
                codes += code
        codes = sorted(codes,key=lambda i:i['code'])
        output = {
            "data":codes
        }
        fd.write(json.dumps(output,indent=4))
        fd.close()

    def getPrice(self,code):
        price_url = "https://api.61financial.com.au/marketdata/latest/?code="+code
        try:
            return float(requests.get(url=price_url,headers=headers).json()[-1]['last'])
        except KeyError:
            return 0.0

    def getAllCodes(self):
        f = open("codes/ALL.json","r")
        data = json.load(f)
        output = []
        for code in data['data']:
            output.append(code['code'])
        return output

    def initialise(self):
        codes = self.getAllCodes()
        data = {}
        for code in codes:
            data[code] = []
        with open("database.json","w") as f:
            f.write(json.dumps(data,indent=4))

    def getCodeForSection(self,section):
        f = open(f"codes/{section}.json","r")
        data = json.load(f)
        output = []
        for code in data['data']:
            output.append(code['code'])
        return output

    def update(self,section):
        codes = self.getCodeForSection(section)
        timetaken, prices = self.gedPriceForSection(section)
        print(f"Get section {section} takes {timetaken}s" )

        database = json.load(open("database.json","r"))
        for code, price in zip(codes,prices):
            #data = {"time":datetime.now().strftime("%Y/%m/%d, %H:%M:%S"),"price":price}
            data = price
            database[code].append(data)
        
        with open("database.json","w") as f:
            f.write(json.dumps(database,indent=4))

if __name__ == '__main__':
    a = StockSubscriber()
    #output = a.gedPriceForSection("RE")
    a.initialise()
    a.update("ALL")