import requests
from bs4 import BeautifulSoup
website_url = "https://infopark.in/companies/job-search"

keyword = ['django','fresher']
res = requests.get(website_url)
output_file = open("jobs.txt","w")
soup = BeautifulSoup(res.text,'lxml')
job = soup.find_all("div",{"class":"row company-list joblist"})

for jobs in job:
    title_ele = jobs.find("a")
    title =title_ele.text
    link = title_ele["href"]
    company_name = jobs.find("div",{"class":"jobs-comp-name"}).text
    last_date = jobs.find("div",{"class":"job-date"}).text
    if any(word.lower() in title.lower() for word in keyword):

        print(title,company_name,last_date,link)
        output_file.write(title +" "+ company_name +" "+ last_date +"\n"+ link +"\n\n")