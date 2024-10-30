import requests 
from urllib.parse import urlencode
import sys

class BookClient():
    __BASE_URL = 'https://api.freeapi.app/api/v1/public'

    def __build_url(self, endpoint, params=None):
        if params:
            query_strings = urlencode(params)
        else: 
            query_strings = ''
        
        url = f'{self.__BASE_URL}/{endpoint}?{query_strings}'

        return url

    def get_random_books(self, count:int, topic:str):
        endpoint = 'books'
        params = {
            'page': 1,
            'limit': count,
            'inc': 'kind, id, etag,volumeInfo',
            'query': topic,
        }
        url = self.__build_url(endpoint,params)
        # print(url)
        # sys.exit()

        # Handling api request errors
        try: 
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.HTTPError as httperror:
            print("HTTP Error: ", httperror)
            sys.exit()
        except requests.exceptions.ConnectionError as conerror:
            print("Unable to connect server ", conerror)
            sys.exit()
        except requests.exceptions.Timeout as tmoute:
            print('Timeout Error ', tmoute)
            sys.exit()
        except requests.exceptions.RequestException as reqexce:
            print('Something went wrong: ', reqexce)
            sys.exit()

        return response.json()
    
    def print_books(self, response):
        book_list = response['data']['data']

        if len(book_list) == 0:
            print('Stock has no book currently')
            return
        
        
    




    


def main(): 
    book_client = BookClient() 
    print(book_client.get_random_books(1, 'ai'))


if __name__ == "__main__": 
    main()
