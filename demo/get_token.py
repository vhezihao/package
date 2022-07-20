import requests
import json
from com.api.demo.timestamp import get_current_time
from com.api.demo.get_uid import func

## ------------------ 获取 13 位时间戳 ------------------
current_time = get_current_time()
# print(current_time)


cookie = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXBhcnRtZW50IjoiIiwiZW1haWwiOiJoZXppaGFvQGpveXkuY29tIiwiZXhwIjoxNjU3NTA1Mzg5LCJqb2Jjb2RlIjoiUFEwMDgxIiwibmlja25hbWUiOiIiLCJwYXNzcG9ydCI6ImR3X2hlemloYW8iLCJyZWFsbmFtZSI6IuS9leaik-ixqiIsInl5dWlkIjoiNzMzNzgifQ.xXj6xtEU1zih0tuYPyLC7s_cbaOLEPhr8x0UL9H0DDy1z5phRBhkV9TvRGG81mzNXTd3Qa_z2RqjRxV4mwjSxqTgSdDhIU75cRC2JFmPv-HkITwatwL3n8pV0cLj8-0ELI3wwDyI6_W_6Cz3TCIx0e1wiv5Jlh3fsdODn4ZNcdBfrH80str-qbQPI-gLr6czq_ZQrzxR9Z_TKGiKtEpc4k1dfE_6_vaBCJrw300GrYlsb3JBxPccYXvo4ZLyu8vk8-yZ2jOLkR3wc9agpPp6n2pdiDWFwbul8mJ1viGxKHpFEtFIkDa2WK0NF0MtuDZBpXyUD80zvimDlU-K5b_vTA'
# uid = 106859946
# uid_list = [2295032954568500,2295032954568560,2295032954568570,2295032954568580,2295032954568590]
uid_list = func()

token_list = []

def get_token():
    for uid in uid_list:
      url = "https://boss-proxy-test.ihago.cn/boss_proxy/ymicro/api?group_id=863&method=CreateToken"
      # url = "https://boss-proxy-test.ihago.cn/boss_proxy/ymicro/api?group_id=863&method=CreateToken"

      payload = json.dumps({
        "uid": uid,
        "env": 1,
        "sequence": current_time
      })

      headers = {
        'cookie': 'username=dw_hezihao; yyuid=73378; jwt=' + cookie,
        'x-ymicro-api-method-name': 'Token.CreateToken',
        'x-ymicro-api-service-name': 'net.ihago.testenv.srv.token',
        'content-type': 'application/json'
      }

      response = requests.request("POST", url, headers=headers, data=payload)
      res = json.loads(response.text)
      # print(res)

      token = res['token']
      # print(res['token'])
      token_list.append(token)

    # print(token_list)
    # print('',json.dumps(token_list,indent=4,ensure_ascii=False))

    return token_list,uid_list


if __name__ == '__main__':
    get_token()