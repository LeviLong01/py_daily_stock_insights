import requests


class Info:
    def __init__(self):
        return

    def get_summary(self, symbol, stock_url):
        try:
            # Get latest summary of latest article
            response = requests.get(stock_url + symbol + '/news/last/1')
            json = response.json()
            return json[0]['summary']
        except Exception as e:
            # Print thrown error
            print(str(e))

    def get_articles(self, symbol, stock_url):
        try:
            # Get latest article
            response = requests.get(stock_url + symbol + '/news/last/1')
            json = response.json()
            return json[0]['url']
        except Exception as e:
            # Print thrown error
            print(str(e))

    def get_company_name(self, symbol, stock_url):
        try:
            # Get company name
            response = requests.get(stock_url + symbol + '/company')
            json = response.json()
            return json['companyName']
        except Exception as e:
            # Print thrown error
            print(str(e))

    def get_exchange(self, symbol, stock_url):
        try:
            # Get exchange the stock belongs to
            response = requests.get(stock_url + symbol + '/company')
            json = response.json()
            return json['exchange']
        except Exception as e:
            # Print thrown error
            print(str(e))
