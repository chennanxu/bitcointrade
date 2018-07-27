import requests


class HTTP:

    @staticmethod
    def get(url):
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
        else:
            return {'code': r.status_code}