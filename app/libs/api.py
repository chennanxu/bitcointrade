from .helper import HTTP

class API:

    @staticmethod
    def get_ticker():
        '''
        获取当前价格
        :return
            date: 返回数据时服务器时间
            buy: 买一价
            high: 最高价
            last: 最新成交价
            low: 最低价
            sell: 卖一价
            vol: 成交量(最近的24小时):
        '''
        url = "https://www.okcoin.com/api/v1/ticker.do?symbol=btc_usd"
        res = HTTP.get(url)
        return res

    @staticmethod
    def get_depth():
        '''
        获取市场深度
        :return:
                asks :卖方深度
                bids :买方深度
        '''
        url = "https://www.okcoin.com/api/v1/depth.do?symbol=btc_usd"