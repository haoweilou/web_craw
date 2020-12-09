import requests
import json
userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
class MakeUpPermission():
    def __init__(self):
        self.header = {
            "user-agent":userAgent
        }
    
    def print(self):
        print(self.response.text)

    def save(self):
        with open("page.html","w",encoding="utf-8") as fp:
            fp.write(self.response.text)
    
    def getData(self,page):
        requestUrl = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList"
        data = {
            "on": "true",
            "page": page,
            "pageSize": 15,
            "productName": "",
            "conditionType": 1,
            "applyname":  "",
            "applysn" : ""

        }
        output = requests.post(requestUrl,json= data,headers = self.header)
        return output.json()

    
    def getCompanyIds(self,page):
        data = self.getData(page)
        companies = data['list']
        ids = [company['ID'] for company in companies]
        return ids        

    def getInformations(self):
        base_url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById"
        i = 51
        ids = self.getCompanyIds(i)
        jsonoutput = {
            "companies" : []
        }
        while ids != []:
            for id in ids:
                data = {"id":id}
                response = requests.post(base_url,data=data,headers=self.header).json()
                infor = f"公司名字:{response['epsName']}, 法人:{response['businessPerson']}, 地址:{response['epsAddress']}\n"
                with open("detail.txt","a",encoding="utf-8") as f:
                    f.write(infor)
                    f.close()
                jsonoutput["companies"].append(response)
            i += 1
            ids = self.getCompanyIds(i)

        with open("company.json","w") as f:
            f.write(json.dumps(jsonoutput,indent=4))

if __name__ == "__main__":
    m = MakeUpPermission()
    print(m.getData(100))
    m.getInformations()
