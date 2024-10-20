import requests
from urllib.parse import urlencode
import sys


if len(sys.argv) != 3: 
    sys.exit('Enter 2 arguments books count and topic')

base_url = 'https://api.freeapi.app/api/v1/public'
end_point = 'books'


def main():

    parameters = {
        'page': '1',
        'limit': str(sys.argv[1]),
        'inc': ','.join(['kind', 'id', 'etag', 'volumeInfo']),
        'query': str(sys.argv[2]),
    }
    url = build_url(end_point, parameters)

    # Make web request

    # response = requests.request('get', url)
    response = requests.get(url)

    if response.status_code != 200:
        print("Don't get response")
        sys.exit(); 


    # res_header = response.headers 
    data = response.json()

    # print(data)
    # print(res_header)
    # print(response.status_code)

    # Extract the useful information from the response

    books_list = data['data']['data']; 

    if not len(books_list): 
        sys.exit('No books found of the topic')

    for book in books_list: 
        book_details = book['volumeInfo']

        # Find which key is present
        required_keys = [('title', 'Title'), ('subtitle', 'Sub Title'), ('authors', 'Authors'), ('publisher', 'Publisher'), ('publishedDate', 'Published Date'), ('pageCount', 'Page Count')]

        available_keys = []

        # Finding the available keys 
        for rkey, _ in required_keys: 
            if rkey in book_details:
                available_keys.append(True)
                continue 
            available_keys.append(False)

        # Print the info of the books 
        for i in range(len(available_keys)):
            if available_keys[i]:
                print(f'{required_keys[i][1]} = {book_details[required_keys[i][0]]}')
            else:
                print(f'{required_keys[i][1]} = data not available')
        print()


# print('Book Details')
# print(f'Title = {book_details['title']}')
# print(f'Subtitle = {book_details['subtitle']}')
# print(f'Author = {book_details['authors']}')
# print(f'Publisher = {book_details['publisher']}')
# print(f'Published Date = {book_details['publishedDate']}')
# print(f'Pages Count = {book_details['pageCount']}')


    # Which keys are availables
    # for i in range(len(required_keys)): 
    #     if not available_keys[i]:
    #         print(f'{required_keys[i]} data is not avialable')
    #         continue

    #     print(f'{required_keys[i]} data is available')



# Print some response information
# print(response.status_code)
# print(response.reason)
# print(response.url)

# Build Urls for different endpoints
def build_url(endpoints, params=None):
    if params: 
        query_strings = urlencode(params)
    else:
        query_strings = ''

    
    url=f'{base_url}/{endpoints}?{query_strings}'

    return url


def get_random_booklist(url):
    pass


if __name__ == '__main__': 
    main() 

