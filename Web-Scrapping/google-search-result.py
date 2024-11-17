import requests
from bs4 import BeautifulSoup
import  sys


def main(): 
    url = 'https://www.google.com/search?q=pen&oq=pen&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTINCAEQABiRAhiABBiKBTINCAIQABiRAhiABBiKBTIMCAMQABhDGIAEGIoFMhAIBBAAGIMBGLEDGIAEGIoFMgYIBRBFGEEyBggGEEUYPDIGCAcQRRg80gEHNDAyajBqN6gCCLACAQ&sourceid=chrome&ie=UTF-8'

    html_doc = requests.get(url).text
    find_search_results(html_doc)


def find_search_results(html_doc):
    sourcecode = BeautifulSoup(html_doc, 'html.parser')
    print(sourcecode.prettify())
    # search_results =  sourcecode.select('div.N54PNb')
    # print(search_results)
    # if 'class="N54PNb"' in html_doc: 
    #     print(True)
    # else: 
    #     print(False)

    


def extract_all_links(html_doc): 
    soup = BeautifulSoup(html_doc, 'html.parser')

    links = soup.find_all('a')
    
    counter = 1
    for _, link in enumerate(links): 
        url = link.get('href', 'No link value specified')
        if url.startswith('/url'): 
            url  = url.split('?')[1]
            url = url.split('=')[1]

            if url.startswith('https://'): 
                print(f"{counter}: {url}")
                counter += 1


if __name__ == "__main__": 
    main()