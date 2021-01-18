# -*- coding: UTF-8 -*
import hmac
import json
import requests
import time
global dns

# https://www.dibaqu.com/iQbE
dns = 'https://testapi.fameex.com'


def getHeader(method, request_path, body):
    # crayzhangpeng@163.com
    # Access_Key = '2c96296c-575b-19e9-661c-cbb120bd3e2b'
    # Secret_Key = '290e184d-e0e3-0dc4-ff31-1711260f91f6'

    # 1877383144@qq.com
    Access_Key = '7ae03b61-b2a5-8e80-4c4d-e25ce3db50cb'
    Secret_Key = 'e0a05f54-676b-7b79-90b7-2945178d357b'

    timestamp = str(time.time())[0:10]
    message = str(timestamp) + str.upper(method) + request_path + str(body)
    mac = hmac.new(bytes(Secret_Key, encoding='utf8'), bytes(
        message, encoding='utf-8'), digestmod='sha256').digest()

    hex_data = bytes(mac).hex()
    headers = {
        'AccessKey': Access_Key,
        'SignatureMethod': 'HmacSHA256',
        'SignatureVersion': 'v1.0',
        'Timestamp': timestamp,
        'Signature': hex_data
    }
    return headers


def getNewprice():
    '''
    获取最新价格
    '''
    method = 'GET'
    path = '/v1/market/history/kline24h?pairName=ADA_USDT'
    url = dns + path
    body = ''
    headers = getHeader(method, path, body)
    res = requests.get(url=url, headers=headers).json()

    return res['data']['last']


def buy():
    '''
    购买接口111
    '''
    method = 'POST'

    path = '/v1/api/spot/orders'
    url = dns + path
    newPrice = getNewprice()
    body = '{"base":"ADA","quote":"USDT","buyType":0,"price":"' + \
        str(newPrice)+'","count":"1"}'

    headers = getHeader(method, path, body)
    res = requests.post(url=url, data=body, headers=headers).json()
    if res["code"] != 200:
        cancel()
    else:
        print(res)


def sell():
    '''
    卖出接口
    '''

    method = 'POST'
    path = '/v1/api/spot/orders'
    url = dns + path
    newPrice = getNewprice()
    body = '{"base":"ADA","quote":"USDT","buyType":1,"price":"' + \
        str(newPrice)+'","count":"1"}'

    headers = getHeader(method, path, body)
    res = requests.post(url=url, data=body, headers=headers).json()

    print(res)


def cancel():
    '''
    撤单接口
    '''

    method = 'POST'
    path = '/v1/api/spot/cancel_orders_all'
    url = dns + path
    newPrice = getNewprice()
    body = '{"buyType":-1,"base":"BTC","quote":"USDT","startTime":0,"endTime":0}'
    headers = getHeader(method, path, body)
    res = requests.post(url=url, data=body, headers=headers).json()
    print(res)


if __name__ == '__main__':

    # # getNewprice()
    # for i in range(0,100):
    # 	buy()
    # 	print("第%s次交易"% str(i))
    # 	time.sleep(10)
    # 	sell()
    # 	time.sleep(10)
    # # cancel()
    buy()
    time.sleep(5)
    sell()
