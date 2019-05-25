# -*- coding: UTF-8 -*-
# import requests
#
# session = requests.session()
# session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
# session.headers['Content-type'] = 'application/x-www-form-urlencoded'
# # print(res.text)
# # session.headers['x-udid'] = 'ACCha1aUqA6PTsEjcylWGx8HHM3feFPytFg=|1544611343'
# res = session.post('https://www.zhihu.com/udid', data=None)
# print(res.text)
# res = session.get('http://www.zhihu.com/api/v3/oauth/captcha?lang=en')
# print(res.text)
# session.headers['x-zse-83'] = '3_1.1'
# # print(session.cookies)
# # print(session.headers)
#
#
# res = session.post('https://www.zhihu.com/api/v3/oauth/sign_in',
#                    data='ToOk0KPwMtBtNXtzltBlMKpxBduq0PQzppOk0KPwMtBtNX0x1hBlMK6z0p9a01AzwLAlMK-pNsauCle2hdQwQGohEobaMc8k-9uxA-dyUXeuD6dpisaxMxP2NlfuKx8k1OQz82LkQcraOs8k1cbkKG5xU6v4NsqxsdAzMLP1PxNa058lw2bl6P_kToQvKkuxwpQw80_l0xQvTobl-cNw6dKk0xbbRoQwmkepNKpxMtvr6TQxolBlMK6w02RdP6uypDBjHxPwclbf0lA1kXQ1QGohSwr_Ogrkj18lOOolLo9a0_vzwpR10ptyOxNa0oA1u2R1N6d1clbf0-v3lXd2I601BxNa0_8k1-8lLCoxLcQb00rwigemAD_lScbuQwNwmwux8DKwclbf90QvlTuxDtPw')
# print(res.text)
# res = session.get('https://www.zhihu.com/logout',data=None)
# # print(res.text)

# from suds.client import Client
# from suds.xsd.doctor import ImportDoctor, Import
# import time
# imp = Import('http://www.w3.org/2001/XMLSchema', location='http://www.w3.org/2001/XMLSchema.xsd')
# imp.filter.add('http://WebXml.com.cn/')
# doctor = ImportDoctor(imp)
# 
# client = Client('http://www.webxml.com.cn/WebServices/WeatherWebService.asmx?wsdl',doctor=doctor)
# res = client.service.getWeatherbyCityName('长沙')
# print(res)
# time.sleep(1)
# res = client.service.getWeatherbyCityName('北京')
# print(res)
# time.sleep(1)
# res = client.service.getWeatherbyCityName('深圳')
# print(res)

# from suds.client import Client
# from suds.xsd.doctor import ImportDoctor, Import
# import time,inspect,json


# 使用suds.client创建一个客户端，用来请求webservice服务器
# imp = Import('http://www.w3.org/2001/XMLSchema', location='http://www.w3.org/2001/XMLSchema.xsd')
# imp.filter.add('http://soap.testingedu.com/')
# doctor = ImportDoctor(imp)

# client = Client('http://112.74.191.10:8081/inter/SOAP?wsdl',headers={'token':'6659095a1a3a4f24afbcb4b5853ddbf9'})
# p = []
# res = client.service.__getattr__('auth')(*p)
# r = json.loads(res)
# print(r)
# p = ['will','123456']
# res = client.service.__getattr__('login')(*p)
# r = json.loads(res)
# print(r)
# p = []
# res = client.service.__getattr__('logout')(*p)
# r = json.loads(res)
# print(r)

import requests,json


session = requests.session()
result = session.post("http://112.74.191.10:8081/inter/REST/auth")
token = json.loads(result.text)['token']
session.headers['token'] = token
result = session.post("http://112.74.191.10:8081/inter/REST/user/register?%7B%22username%22%3A%22I_wanting%22%2C%22pwd%22%3A%22111111%22%2C%22nickname%22%3A%22111111%22%2C%22describe%22%3A%22111111%22%7D")
print(result.text)