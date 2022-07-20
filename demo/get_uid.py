import requests
import json


mobiles = [
            # "86913000810",
            # "86913000811",
            # "86913000812",
            # "86913000813",
            # "86913000814",
            # "86913000815",
            # "86913000816",
            # "86913000817",
            # "86913000818",
            # "86913000819",
            # "86913000810",
            # "86913000811",
            # "86913000812",
            # "86913000813",
            # "86913000814",
            # "86913000815",
            # "86913000816"
            '86913087610',
            '86913087611',
            '86913087612',
            '86913087613',
            '86913087614',
            '86913087615',
            '86913087616',
            '86913087617',
            '86913087618',
            '86913087619'
           ]

uid_list = []

def func():
    for mobile in mobiles:
        ## 印尼测试（hago）
        # url = "https://i-test.ihago.net/service/batchQuery"
        # payload = f"appId=ikxd&with_oa=1&type=2&vals={mobile}"

        ## dera 中东正式
        url = "https://i-uaasbe-console.ihago.net/service/batchQuery"
        payload = f"appId=dera&with_oa=1&type=2&vals={mobile}"

        headers = {'Content-Type': 'text/plain'}

        response = requests.request("POST", url, headers=headers, data=payload)
        res = json.loads(response.text)
        # print(res)

        uid = res["info"][0]["uuid"]
        # print(uid)
        uid_list.append(uid)

    # print(uid_list)
    # print('', json.dumps(uid_list, indent=4, ensure_ascii=False))
    return uid_list

#     #
#     # cid = res['data']["my_own_chan_list"][1]['cid']
#     # print(cid)

if __name__ == '__main__':
    func()
