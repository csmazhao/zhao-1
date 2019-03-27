import unittest
import requests

#####登录操作，获取token#######
url = 'https://erp-test-api.eatjoys.cn/login'
data1 = {'phone':'18444444444','password':'25d55ad283aa400af464c76d713c07ad'}
headers1 = {'Content-Type':'application/json;charset=UTF-8'}

response = requests.post(url,json=data1,headers=headers1)
# token = response.json()['data']['token']
headers = {'Content-Type':'application/json;charset=UTF-8','token':response.json()['data']['token']}
hosts='https://erp-test-api.eatjoys.cn'

#######业务接口测试##########
####get数据####
path = '/dict/list'
params = 'serviceName=goodsOrderService&dictCode=goodOrderState'

response = requests.get(hosts+path,params=params,headers=headers)
print(response.json())
status_code = response.status_code

####post数据####
path1 = '/goods/page'
body = {'endTime': "",'goodsOrderNo': "",'goodsOrderType': "",'intoOrgId': "",'outOrgId': "",'page': "1",'startTime': "",'state': ""}
response = requests.post(hosts+path1,json=body,headers=headers)
print(response.json())
status_code = response.status_code

####单元测试，字段校验####
class response(unittest.TestCase):

    def test_StatusCode(self):
        self.assertEqual(200,status_code)

if __name__ == '__main__':
    unittest.main()
