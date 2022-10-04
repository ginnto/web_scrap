import requests
from bs4 import BeautifulSoup
# website_url = "https://infopark.in/companies/job-search"
website_url = "https://www.technopark.org/job-search"

keyword = ['django','fresher']
res = requests.get(website_url)
output_file = open("tecjobs.txt","w")
soup = BeautifulSoup(res.text,'lxml')
job = soup.find_all("tr",{"class":"companyList"})

for jobs in job:
    title_ele = jobs.find("a")
    title =title_ele.text
    # link = title_ele["onClick"]
    company_names = jobs.find("td")
    company_name = company_names.text

    last_dates = jobs.find("td")
    last_date = last_dates.text

    if any(word.lower() in title.lower() for word in keyword):

        print(title,company_name,last_date)
        output_file.write(title +" "+ company_name +" "+ last_date +"\n"+ "\n\n")