import requests
from bs4 import BeautifulSoup

res = requests.get('https://infopark.in/companies/job-search')
soup = BeautifulSoup(res.text, 'lxml')
# print(res.text)

keywords = ['python', 'django']
output_file = open('jobs.txt', 'w')

jobs = soup.find_all('div', {'class' : 'row company-list joblist'})
# print(jobs)


for job in jobs:
    title_element = job.find('a')

    title = title_element.text
    link = title_element['href']

    company_name = job.find('div', {'class':'jobs-comp-name'}).text
    last_date = job.find('div', {'class':'job-date'}).text
    # print(title, link)

    if any( word.lower() in title.lower() for word in keywords):
        # print(title, company_name, last_date)
        output_file.write(title + ' | ' + company_name + ' | ' + last_date + '\n' + link + '\n\n')


