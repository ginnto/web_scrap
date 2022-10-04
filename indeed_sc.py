import requests
from bs4 import BeautifulSoup
website_url = "https://in.indeed.com/jobs?q=python%20developer&l=India&from=searchOnHP&vjk=ac9dbd5e904a8b60"

keyword = ['python','django']
res = requests.get(website_url)
output_file = open("injobs.txt","w")
soup = BeautifulSoup(res.text,'lxml')
job = soup.find_all("div",{"class":"mosaic-zone"})

for jobs in job:
    title_ele = jobs.find("a")
    title =title_ele.text
    link = title_ele["href"]
    company_name = jobs.find("h2",{"class":"jobTitle"}).text
    # last_date = jobs.find("div",{"class":"job-date"}).text
    if any(word.lower() in title.lower() for word in keyword):

        print(title,company_name,link)
        output_file.write(title +" "+ company_name +"\n"+ link +"\n\n")