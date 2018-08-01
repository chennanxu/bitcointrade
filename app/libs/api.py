from .helper import HTTP
from HuobiServices import *


class API:

    @staticmethod
    def get_trade():
        '''
        获取当前价格
        :return
              "tick": {
                "id": 消息id,
                "ts": 最新成交时间,
                "data": [
                  {
                    "id": 成交id,
                    "price": 成交价钱,
                    "amount": 成交量,
                    "direction": 主动成交方向,
                    "ts": 成交时间
                  }
                ]
              }
        '''
        return get_trade('btcusdt')

