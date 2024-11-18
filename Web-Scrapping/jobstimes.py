import requests 
from bs4 import BeautifulSoup
import re
import csv

def main(): 
    technology = input("Technology: ")

    url = f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=Python%2CPython&txtKeywords={technology}%2C&txtLocation='

    job_posts = parse_html_content(get_html_page(url))

    write_in_csv_job_file('job_list.csv', job_posts)

def write_in_csv_job_file(filename, job_posts): 
    with open(filename, 'w') as file: 
        writer = csv.DictWriter(file, fieldnames=['job_title', 'company', 'date_posted', 'job_short_des', 'skills', 'location', 'salary', 'experience']) 
        writer.writeheader()

        writer.writerows(job_posts)

def parse_html_content(html_doc): 
    soup = BeautifulSoup(html_doc, 'html.parser')

    if job_boxes := soup.select('li.job-bx'): 
        job_posts = []
        for job_box in job_boxes:
            job_posts.append(get_job_details(job_box))

    return job_posts

def get_job_details(job_box): 

    if job_title := job_box.select_one('h2.heading-trun a'): 
        job_title = job_title.text.strip()
    else: 
        job_title = ''

    if comp_name := job_box.select_one('h3.joblist-comp-name'): 
        comp_name = comp_name.string.strip()
    else:
        comp_name = ''
    
    if date_posted := job_box.select_one('span.sim-posted span'): 
        date_posted = date_posted.text.strip()
    else: 
        date_posted = ''
    
    if job_short_description := job_box.select_one('li.job-description__'): 
        job_short_description = re.sub(r'\s\s+', ' ', job_short_description.text.strip())
    else: 
        job_short_description = ''
    
    if tags := job_box.select('div.more-skills-sections span'): 
        skills = []
        for tag in tags: 
            skills.append(tag.text.strip())
    else: 
        skills = []
    
    locexpsal = job_box.select_one('ul:has(li.srp-zindex.location-tru)')

    if locexpsal: 
            locexpsal = locexpsal.find_all('li')

            # Assume there is exactly three li items and corresponding locexpsal information are stored 
            # in the order in which they have been accesed and assigned 
            location = locexpsal[0].text.strip()
            experience = locexpsal[1].text.strip()
            salary = locexpsal[2].text.strip()
            salary = re.sub(r'\s+', '', salary)
    else: 
        location, experience, salary = '', '', ''

    return {
        "job_title": job_title,
        "company": comp_name,
        "job_short_des": job_short_description,
        "skills": skills,
        "location": location,
        "experience": experience,
        "salary": salary,
        "date_posted": date_posted,
    }

def get_html_page(url): 
    response = requests.get(url)

    if response.status_code == 200: 
        return response.text

    return None

def save_html_content(html_doc, filename): 
    with open(filename, 'w') as file: 
        written_char = file.write(html_doc)

    return written_char

def print_headers(headers): 
    for key in headers: 
        print(f'{key}: {headers[key]}')

if __name__ == "__main__": 
    main()