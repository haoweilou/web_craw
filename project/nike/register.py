import requests
from lxml import etree
import json
url = "https://unite.nike.com/access/users/v1?appVersion=857&experienceVersion=857&uxid=com.nike.commerce.nikedotcom.web&locale=en_AU&backendEnvironment=identity&browser=Google%20Inc.&os=undefined&mobile=false&native=false&visit=8&visitor=6a0c385b-e2a3-4285-84fd-f12e9865417b&language=en-GB&uxId=com.nike.commerce.nikedotcom.web"
url = "https://unite.nike.com/access/users/v1?appVersion=857&experienceVersion=857&uxid=com.nike.commerce.nikedotcom.web&locale=en_AU&backendEnvironment=identity&browser=Google%20Inc.&os=undefined&mobile=false&native=false&visit=1&visitor=afc8c1ac-30e8-4faf-9056-34d1c919c66d&language=en-GB&uxId=com.nike.commerce.nikedotcom.web"
headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
}
def register():
    email = "helloworld@nmsl.com"
    firstname = "h"
    lastname = "h"
    dob = "2010-12-13"
    password = "Ky12345678"
    with open("register.json","r") as target:
        data = json.load(target)
    data['firstName'] = firstname
    data['lastName'] = lastname
    data['password'] = password
    data['emailAddress'] = email
    data['username'] = email
    data['account']['email'] = email
    data['account']['passwordSettings']['password'] = password
    data['account']['passwordSettings']['passwordConfirm'] = password
    data['dateOfBirth'] = dob
    print(json.dumps(data,indent=4))
    output = requests.post(url=url,json = data,headers = headers).text
    print(output)
    #return response
if __name__ == '__main__':
    output = register()
    print(output)