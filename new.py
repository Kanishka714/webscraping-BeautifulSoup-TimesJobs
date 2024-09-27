import time

from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=python&txtLocation=').text
#print(html_text)
soup = BeautifulSoup(html_text, 'lxml')

jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

def find_job():
    print('Enter job title')
    title_name = input('>')
    print(f"filtering for {title_name.strip()}")

    for index, job in enumerate(jobs):

        title = job.header.h2.a.text
        date = job.find('span', class_='sim-posted').text
        if 'few' in date and title_name in title:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skill = job.find('span', class_='srp-skills').text.replace(' ', '')
            link = job.header.h2.a['href']
            with open(f'Posts/{index}.txt', 'w') as f:

                f.write(f"title: {title.strip()} \n")
                f.write(f"Date: {date.strip()} \n")
                f.write(f"Company Name: {company_name.strip()} \n")
                f.write(f"Skills required: {skill.strip()} \n")
                f.write(f"Link to post {link} \n")
            print(f'File Saved: {index}')



if __name__ == '__main__':
    while True:
        find_job()
        time_wait = 10
        print(f"Waiting {time_wait} minutes")
        time.sleep(time_wait * 60)