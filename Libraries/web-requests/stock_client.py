import requests
from urllib.parse import urlencode
from requests import exceptions


class StockClient(): 
    BASE_URL = 'https://api.freeapi.app/api/v1/public'

    def __init__(self):
        print('One instance has been created of StockClient')
    
    def build_url(self, endpoint, parameters=None):
        if parameters:
            return f'{self.BASE_URL}/{endpoint}?{urlencode(parameters)}'
        else: 
            return f'{self.BASE_URL}/{endpoint}'
    

    def get_stocks(self, count, query, inc:list[str]):
        endpoint = 'stocks'

        parameters={
            'page': 1,
            'limit': count,
            'inc': 'Symbol,' + ','.join(inc),
            'query': query
        }

        url = self.build_url(endpoint, parameters)


        try: 
            response = requests.get(url,timeout=3000)
            response.raise_for_status()
        except requests.exceptions.Timeout as error: 
            print('Error: Time out error, Server did not send data in the specified time')
            print(error)
            return None

        if response.status_code != 200: 
            return None
        
        return response.json()


    def get_random_stock(self):
        endpoint = 'stocks/stock/random'
        try:
            response = requests.get(self.build_url(endpoint))
        except exceptions.Timout as error: 
            print('Error: Timeout error')
            print(error)
            return None
        
        if response.status_code != 200: 
            return None 
        
        return response.json()
            

    def display_stocks(self, data): 
        if not data:
            print('No data')
            return
        
        stocks = data['data']['data']

        if not len(stocks): 
            print('No stocks found of the specified compnany')
            return 

        for stock in stocks: 
            keys = stock.keys()

            for key in keys: 
                print(stock[key])

            print()
        
    def display_random_stock(self, stock):
        if not stock: 
            print('No data')
            return 
        
        stock_details = stock['data']
        keys = stock_details.keys()

        for key in keys: 
            print(key + ' = ' + stock_details[key])
        
        print()

def main():
    pass 


if __name__ == '__main__': 
    main()