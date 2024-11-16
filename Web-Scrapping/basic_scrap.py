import sys

from bs4 import BeautifulSoup

def main(): 
    html_doc = ''

    with open('index.html', 'r') as file: 
        html_doc = file.read() 
        
    soup = BeautifulSoup(html_doc, 'html.parser')
    # print(soup.prettify(formatter='html5'))

    # print(soup.title.string)
    # print(soup.title.text , soup.title.string)
    # print(soup.title.parent.string)


    # print(soup.head.meta) # give you the very first meta element
    # print(soup.head.select('meta')) # list of all meta element 
    # print(soup.head.string) # None

    # print(soup.h1['content']) # value of particular attribute 
    # print(soup.h1['class']) # return a list of class value 


    # # Extract all the urls found in the page 
    # links = soup.find_all('a')
    # for link in links: 
    #     print(link.get('abc', "doesn't exist"))
    
    # # Extracting all the text from a page 
    # page_text = soup.get_text(separator="\n\n", strip=True)
    # print(page_text)



    # print(soup.find(id="card-python-for-beginners").prettify())

    extract_course_info(html_doc)


def extract_course_info(html_doc): 
    sourcecode = BeautifulSoup(html_doc, 'html.parser')
    courses = sourcecode.find_all(class_="card")
    course_list = []

    for index, course in enumerate(courses): 
        field = course.select_one('div.card-header').string.strip()
        title = course.find(class_='card-title').string
        description = course.find(class_='card-text').string
        price = course.find(class_='btn-primary').string


        course_list.append({
                'title': title,
                'description': description,
                'price': price,
                'field': field
            }
        )

    return course_list



if __name__ == "__main__": 
    main()