import requests
import time


def get_kline(period="1min", size=2000, symbol="btcusdt"):
    url = "https://api.huobipro.com/market/history/kline?period=1min&size=2000&symbol=btcusdt"
    r = requests.get(url.format(period, size, symbol))
    if r.status_code == 200:
        return r.json()
    else:
        return {}


if __name__ == '__main__':
    kline = get_kline()
    if kline is not None:
        with open('huobikline.txt', 'a') as f:
            f.write("时间,成交量,成交笔数,开盘价,收盘价,最低价,最高价,成交额\r\n")
            data = kline['data']
            for e in data:
                ts = e['id']
                tl = time.localtime(ts)
                format_time = time.strftime("%Y-%m-%d %H:%M:%S", tl)
                line = "{},{},{},{},{},{},{},{}\r\n".format(format_time, e['amount'], e['count'],
                                                            e['open'], e['close'], e['low'], e['high'], e['vol'])
                f.write(line)
