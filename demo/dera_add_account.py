import requests
import json
from com.api.demo.timestamp import get_current_time
import sys

token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXBhcnRtZW50IjoiIiwiZW1haWwiOiJoZXppaGFvQGpveXkuY29tIiwiZXhwIjoxNjU1Nzc2OTQxLCJqb2Jjb2RlIjoiUFEwMDgxIiwibmlja25hbWUiOiIiLCJwYXNzcG9ydCI6ImR3X2hlemloYW8iLCJyZWFsbmFtZSI6IuS9leaik-ixqiIsInl5dWlkIjoiNzMzNzgifQ.TB5vlXNm3kGg2V4NyTTtL7yLDGicl1enejVHguNoXsSXcbfTCXy2ny-9Kpii6vfUlT1d0l5LjccpPtgIh3UJ8oAZSS17ZvgXRxTq5jq79ruC76XfOzUqY75EjZW_k9al2KJYREEqKVi5aH-SOsbyaW5tLLazQ-OZXMFFlWpiYM5ncIy4c7Z7Jdyiza9b-JuNxPeGD-vQydpnSDCWt45gMUXTVE-Ec-R4_XS5NJI4LLl0sGaGuaRdg8aCbTl6QwlYBpXiJhpjQ_biKswJrJqm0fJf_RDffHdobfpysvHoRn0xI3rho70353ck-Kc7o8SVCchnGC4ysq0z---wGxXFhA'

def input_moblie(start_mobile,add_num):
  # start_mobile = input("请输入需要添加账号的手机号(开始账号)：")
  # start_mobile = int(start_mobile)
  # #
  # add_num = input("请输入需要添加账号的个数：")

  mobiles_list = []

  i = 0
  while i< int(add_num):
    mobiles_list.append(start_mobile)
    # print(start_mobile)
    start_mobile += 1
    i += 1

  return mobiles_list




def add_account():
  mobiles_list = input_moblie(start_mobile,add_num)
  # print(mobiles_list)

  new_uid_list =[]
  old_uid_list =[]
  all_uid_list =[]

  for mobile in mobiles_list:
      url = "https://i-test.ihago.net/service/genMobileUid"
      # 注册 hago
      # payload = f"appId=ikxd&mobile={mobile}&rawCountry=VN"
      # 注册 dera
      payload = f"appId=dera&mobile={mobile}&rawCountry=VN"
      headers = {
        'Content-Type': 'text/plain'
      }

      response = requests.request("POST", url, headers=headers, data=payload)
      res = json.loads(response.text)
      print('手机号：', res['mobile'], '是否是新账号：', res['new'], 'uid：', res['uid'])
      all_uid_list.append(res['uid'])
      # print(type(res['new']))

##--------------判断新添加是账号是否是新账号------------------------
      if res['new'] == bool(1):
        new_uid_list.append(res['uid'])
      else:
        old_uid_list.append(res['uid'])

  print('新增账号 uid：',json.dumps(new_uid_list,indent=4,ensure_ascii=False))
  print('已有账号 uid：',json.dumps(old_uid_list,indent=4,ensure_ascii=False))
  print('总账号 uid：',json.dumps(all_uid_list,indent=4,ensure_ascii=False))
  return all_uid_list


##------------------添加登录白名单---------------------
def add_login_whitelist():
    ## ------------------ 获取 13 位时间戳 ------------------
    current_time = get_current_time()
    print("时间戳",current_time)

    uid_list = add_account()
    print('添加登录白名单账号uid:',uid_list)

    for uid in uid_list:
        url = "https://boss-proxy-test.ihago.cn/boss_proxy/ymicro/api?group_id=863&method=Add"

        cookies = {'username': 'dw_hezihao', 'yyuid': '73378',
                   'jwt': token}
        # payload = "{\"uid\":107112776,\"token\":\"username=dw_hezihao; yyuid=73378; jwt=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXBhcnRtZW50IjoiIiwiZW1haWwiOiJoZXppaGFvQGpveXkuY29tIiwiZXhwIjoxNjUzNjE1NzI4LCJqb2Jjb2RlIjoiUFEwMDgxIiwibmlja25hbWUiOiIiLCJwYXNzcG9ydCI6ImR3X2hlemloYW8iLCJyZWFsbmFtZSI6IuS9leaik-ixqiIsInl5dWlkIjoiNzMzNzgifQ.KCX9V67zLH2BNZnFAJT7_EKNYN6VOxGMcbAdBE4JZ7YIbwZUG2Cvxe8kZsFkOd2RUKWRG5g3_-_3FFEstwQBuFbTiw-3K97hYCbJctr7KSOsn9faTQx4YrBu2iGIe8_azl60ZoQSC0BbIQ21RzqrSkKBoOlTXtbwqCi2_OhuLjHMCQ0XwAOVUgKYX1rtdEZUDX9o5CYKZbOtN0N19WoEmeaER6_-26jO-BvOn8z6ZVjYjPokHA-VHcIxpppG_ZCV0HykHmTANDmB62sSH3AicV7J_JUBcbsHsdgSk8FNhDPn68Sdxo9JiJXkO6y3wplFqrkYk2s4pdT7jbU7EbezPw\",\"sequence\":1653049835270}"
        payload = {"uid": uid,
                   "token": "username=dw_hezihao; yyuid=73378; jwt=" + token,
                   "sequence": current_time}

        headers = {
            'content-type': 'application/json',
            # 'cookie': 'username=dw_hezihao; yyuid=73378; jwt=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXBhcnRtZW50IjoiIiwiZW1haWwiOiJoZXppaGFvQGpveXkuY29tIiwiZXhwIjoxNjUzNjE1NzI4LCJqb2Jjb2RlIjoiUFEwMDgxIiwibmlja25hbWUiOiIiLCJwYXNzcG9ydCI6ImR3X2hlemloYW8iLCJyZWFsbmFtZSI6IuS9leaik-ixqiIsInl5dWlkIjoiNzMzNzgifQ.KCX9V67zLH2BNZnFAJT7_EKNYN6VOxGMcbAdBE4JZ7YIbwZUG2Cvxe8kZsFkOd2RUKWRG5g3_-_3FFEstwQBuFbTiw-3K97hYCbJctr7KSOsn9faTQx4YrBu2iGIe8_azl60ZoQSC0BbIQ21RzqrSkKBoOlTXtbwqCi2_OhuLjHMCQ0XwAOVUgKYX1rtdEZUDX9o5CYKZbOtN0N19WoEmeaER6_-26jO-BvOn8z6ZVjYjPokHA-VHcIxpppG_ZCV0HykHmTANDmB62sSH3AicV7J_JUBcbsHsdgSk8FNhDPn68Sdxo9JiJXkO6y3wplFqrkYk2s4pdT7jbU7EbezPw',
            'x-ymicro-api-method-name': 'Token.Add',
            'x-ymicro-api-service-name': 'net.ihago.testenv.srv.token'
        }

        response = requests.request("POST", url, headers=headers, json=payload, cookies=cookies)

        print('添加白名单结果:',response.text)






if __name__ == '__main__':
    # mobile = '86911843700'
    start_mobile = input("请输入需要添加账号的手机号(开始账号)：")
    # str_start_mobile = sys.argv[1]
    # start_mobile = int(str_start_mobile)
    print(start_mobile)
    start_mobile = int(start_mobile)
    #
    add_num = input("请输入需要添加账号的个数：")
    # str_add_num = sys.argv[2]
    # add_num = int(str_add_num)
    print(add_num)

    # input_moblie(start_mobile,add_num)
    # add_account()
    add_login_whitelist()
