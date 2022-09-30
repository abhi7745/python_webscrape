from calendar import c
import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.technopark.org/job-search')
keyword = ['django']
output_file = open('technopark_webscarpe/jobs.txt', 'w')
soup = BeautifulSoup(response.text, 'lxml')
# print(soup)

job_row = soup.find_all('tr', {'class' : 'companyList'})

count = 0
for jobs in job_row:
    job_title = jobs.find('a', {'class':'jobTitleLink'}).text

    if any(word.lower() in job_title.lower() for word in keyword):
        count += 1
        print(job_title)
        output_file.write(job_title + '\n\n')


print(count, 'Jobs found')
output_file.write(str(count) + ' Jobs found' + '\n\n')



