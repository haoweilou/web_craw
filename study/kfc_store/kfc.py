import requests
import json
def print_list(table_list, destination):
    if(table_list == []):return

    with open("kfc_stores/"+destination+".txt","w",encoding="utf-8") as f:
        f.write("")
    f.close()
    with open("kfc_stores/"+destination+".txt","a",encoding="utf-8") as fd:
        for store in table_list:
            output = f"店名: {store['storeName']}, 地址: {store['addressDetail']}, 省市: {store['provinceName']}, {store['cityName']}\n"
            fd.write(output)
        fd.close()

        
def getCitiesList():
    f = open("city","r",encoding="utf-8")
    provinces = json.load(f)["provinces"]
    allcity = []
    for province in provinces:
        cities= province["citys"]
        for city in cities:
            allcity.append(city)
    return allcity
#crawler for collect location of all KFC store in China
if __name__ == '__main__':
    kfc_url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    header = {
        'user-agent':user_agent
    }
    keyword = input("Input your destination: ")
    sortByCity = int(input("Press 1 for city: "))
    kfc_url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op="

    if(not sortByCity):
        kfc_url += "keyword"
    else:
        kfc_url +="cname"

    keyword = keyword.split(' ')
    keyword = getCitiesList()
    print("开始收集信息")
    i = 0
    for key in keyword:
        key = key["citysName"]
        data = {
            "cname":"",
            "pid": "",
            "pageIndex":1,
            "pageSize":1,
        }
        if(sortByCity):data['cname'] = key
        else:data['keyword'] = key

        response = requests.post(url=kfc_url, headers=header, data=data)
        output = response.json()
        #get the number of store
        number_of_store = int(output['Table'][0]['rowcount'])
        data["pageSize"] = number_of_store
        #calculate the response
        response = requests.post(url=kfc_url, headers=header, data=data)
        output = response.json()
        print_list(output['Table1'],key)
        i+=1
        print(f"     {key} finished {i}/{len(keyword)}")
    print("信息收集完成")