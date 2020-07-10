import logging
import time
from broker.client import BrokerClient

BASE_URL = "https://api.hanbitco.global/openapi/"
API_KEY = "lVVf7I1lZNuA7oIDhEZvB1LtPTX69JRZvAePCeqGMFuJi1h3WGkoc8Bj2ADqiDpt"
SECRET = "jG65PxK8cmSkfMeR4b89tNiUVyrWTHyE47tFqxbhGktsR4Tojo6u08iuBb85CwBY"

if __name__ == '__main__':
    from broker import broker_log

    broker_log.setLevel(logging.DEBUG)
    broker_log.addHandler(logging.StreamHandler())

    proxies = {
        "http": "",
        "https": "",
    }

    entry_point = BASE_URL  # like: https://api.xxx.yyy/openapi/ where xxx.yyy is your base domain
    b = BrokerClient(entry_point, api_key=API_KEY, secret=SECRET, proxies=proxies)

    # print(b.time())

    # print(int(time.time() * 1000))

    # print(b.broker_info())

    # print(b.depth('BTCUSDT'))

    # print(b.trades('BTCUSDT'))

    # print(b.klines('BTCUSDT'))

    # print(b.ticker_24hr('BTCUSDT'))
    from pyprnt import prnt
    result = b.order_new(symbol='BTCUSDT', side='BUY', type='LIMIT', quantity='10', price='0.1', timeInForce='GTC')

    prnt(result)

    # order_id = result['orderId'] # Problem here

    # print(order_id)

    # print(b.order_get(order_id=order_id))

    # print(b.order_cancel(order_id=order_id))

    # print(b.open_orders())

    # print(b.history_orders())

    # print(b.account())

    # print(b.my_trades())

    # listen_key = b.stream_get_listen_key()

    # print(listen_key)

    # print(b.stream_keepalive(listen_key.get('listenKey')))

    # print(b.stream_close(listen_key.get('listenKey')))

    # print(b.deposit_orders())

