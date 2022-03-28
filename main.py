import requests
import csv
from bs4 import BeautifulSoup

# code
html_text = requests.get(f'https://clutch.co/directory/mobile-application-developers').text
soup = BeautifulSoup(html_text, 'html.parser')
company = soup.find_all("h3", {"class": "company_info"})  # company name
company_list = [x.text.strip() for x in company]

rating = soup.find_all("span", {"class": "rating"})  # rating of the company
rating_list = [x.text.strip() for x in rating]

review = soup.find_all("a", {"data-link_text": "Reviews Count"})
review_list = [x.text.strip().split(' ')[0] for x in review]

project_size = soup.find_all("div", {"data-content": "<i>Min. project size</i>"})
project_size_list = [x.span.text for x in project_size]

hour_rate = soup.find_all("div", {"data-content": "<i>Avg. hourly rate</i>"})
hour_rate_list = [x.span.text for x in hour_rate]

employee = soup.find_all("div", {"data-content": "<i>Employees</i>"})
employee_list = [x.span.text for x in employee]

location = soup.find_all("div", {"data-content": "<i>Location</i>"})
location_list = [x.span.text for x in location]

website = soup.find_all("a", {"class": "website-link__item"})
website_list = [x['href'] for x in website]
final_list = []
for i in range(len(company_list)):
    final_list.append(
        [company_list[i], rating_list[i], review_list[i], project_size_list[i], hour_rate_list[i], employee_list[i],
         location_list[i], website_list[i]])

headers = ['Company Name', 'Rating', 'Reviews', 'Project Size', 'Hourly Rate', 'Employee Count', 'Location', 'Website']
with open('file.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(headers)

    # write multiple rows
    writer.writerows(final_list)