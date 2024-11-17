
""" TO DO: Later Work
    Right now scrapping data from this website is out of scope 
    Content are being generated dynamically.

    I would do that later once i get some experience 
    with html parsing 
"""







# from bs4 import BeautifulSoup
# import requests 

# def main(): 
#     # print(get_html_page())
#     parse_html_doc(get_html_page())



# def get_html_page(url:str='https://www.naukri.com/html-jobs'): 
#     page = requests.get('https://www.naukri.com/html-jobs')

#     if page.status_code != 200: 
#         return None

#     return page.text

# def parse_html_doc(html_doc): 
#     soup = BeautifulSoup(html_doc, 'html.parser')

#     print(soup.prettify())
#     # jobs_list_container = soup.find_all(class_='srp-jobtuple-wrapper')
#     # print(jobs_list_container)



# if __name__ == "__main__": 
#     main()