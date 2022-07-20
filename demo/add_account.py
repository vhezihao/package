import requests
import json
from com.api.demo.timestamp import get_current_time
import sys

token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXBhcnRtZW50IjoiIiwiZW1haWwiOiJoZXppaGFvQGpveXkuY29tIiwiZXhwIjoxNjU3MjcyNTE5LCJqb2Jjb2RlIjoiUFEwMDgxIiwibmlja25hbWUiOiIiLCJwYXNzcG9ydCI6ImR3X2hlemloYW8iLCJyZWFsbmFtZSI6IuS9leaik-ixqiIsInl5dWlkIjoiNzMzNzgifQ.xbyjfk_VKmlPFIbB8Kmskb9ACAq1D-lReefWDA1peJ_Z36UviwxFxXyOElHZd7BGGxk__iDPQC-rrzEkbkURsX1Kr5xuT22GGx6MdfWXcVk9ia8e1N1bwwyOmNoQMsoGuJmJCupYPeuJV0_W-b-0w2GP-dR7DV-8S9Th-RJVnMe7x7nUydBaoOGaIk_n3q5OHCnBClpCtxu5Eht5WmiqlRi1WFG5LtHyTdzR6YqvGzqwETGgC-ASF9FIYqEHA5pEiWuT7PtCzuWbYrXehw2ihxcVUZ58VzYS33MQIFkciRmAYiKtfE7jYqNiKAOqtcn6kRdX5UrSP47-Sw-5BKjVIQ'

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

      if app_name == 'hago':
          # 注册 hago
          payload = f"appId=ikxd&mobile={mobile}&rawCountry=VN"
      elif app_name == 'dera':
          # 注册 dera
          payload = f"appId=dera&mobile={mobile}&rawCountry=VN"
      else:
          print('填写app_name错误')

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
  return mobiles_list,new_uid_list,old_uid_list,all_uid_list


##------------------添加登录白名单---------------------
def add_login_whitelist():
    ## ------------------ 获取 13 位时间戳 ------------------
    current_time = get_current_time()
    print("时间戳",current_time)

    mobiles_list,n_uid_list,o_uid_list,uid_list = add_account()
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
        add_result = response.text
        # print('添加白名单结果:',response.text)
        return mobiles_list,n_uid_list,o_uid_list,uid_list,add_result



##------------------飞书机器人--------------------
def robot():
    mobiles_list,n_uid_list,o_uid_list,uid_list,add_result = add_login_whitelist()
    # now_time = add_login_whitelist[1]
    # key_word = "当前时间："

    # 删除手机号 86 区号
    remove_mobiles_list = []
    for mobile in mobiles_list:
        # mobiles = str(mobiles_list[i])[2:]
        mobiles = str(mobile)[2:]
        remove_mobiles_list.append(int(mobiles))
    # print(remove_mobiles_list)

    # 你复制的webhook地址
    url = "https://open.feishu.cn/open-apis/bot/v2/hook/8942cfa9-b5c7-421d-99c5-9075577dc7eb"
    payload_message = {
        "msg_type": "text",
        "content": {
            "text": app_name + ':\n新增账号:'+ str(remove_mobiles_list) + '\n\n新增账号 uid:'+ str(n_uid_list) + '\n\n已有账号 uid:' + str(o_uid_list) + '\n\n总账号 uid:' + str(uid_list) + '\n\n添加白名单结果:' + str(add_result)
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=json.dumps(payload_message))
    print(response.text)



if __name__ == '__main__':
    # 选择添加 app
    app_name = sys.argv[1]
    print(app_name)

    # mobile = '86911843700'
    # start_mobile = input("请输入需要添加账号的手机号(开始账号)：")
    str_start_mobile = sys.argv[2]
    start_mobile = int(str_start_mobile)
    print(start_mobile)
    # start_mobile = int(start_mobile)
    #
    # add_num = input("请输入需要添加账号的个数：")
    str_add_num = sys.argv[3]
    add_num = int(str_add_num)
    print(add_num)

    # input_moblie(start_mobile,add_num)
    # add_account()
    # add_login_whitelist()
    robot()