import requests
import json

#  107112776,107112786,107112796
uid_list = list(input("uid:").split(','))
for i in range(len(uid_list)):
    uid_list[i] = int(uid_list[i])
print(uid_list)

amount = input("数量:")

currencyType = input("钻石/水晶:")
if currencyType == "钻石":
    currencyType = '1805'
elif currencyType == "水晶":
    currencyType = '1826'
else:
    print("输入充值类型错误")



# url = "http://turnover-bg-test.duowan.com/addCurrency?uid=107112776&amount=10000&description=test&currencyType=1805&appid=1802&countryCode=id"
for uid in uid_list:
    url = f"http://turnover-bg-test.duowan.com/addCurrency?uid={uid}&amount={amount}&description=test&currencyType={currencyType}&appid=1802&countryCode=id"
    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    res = json.loads(response.text)

    print( 'uid：', uid,'状态：', res['msg'], '总数量：', res['allAmount'])