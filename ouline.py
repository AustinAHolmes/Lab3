#import beautifulsoup and request here
from bs4 import BeautifulSoup
import requests
import json
#function to get job list from url 'https://www.talent.com/jobs?k={role}&l={location}'
def getJobList(role,location):
    url = 'https://www.talent.com/jobs?k={role}&l={location}'
    # Complete the missing part of this function here
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    jobDetails = soup.find_all('div',class_='card card__job')
    jobs = []
    for job in jobDetails:
            jobTitle = job.find('h2',class_= 'card__job-title').text.strip()
            company = job.find('div',class_= 'card__job-empname-label').text.strip()
            description = job.find('p',class_='card__job-snippet').text.replace ('\n', '').replace("'","").strip()
            jobDetailsJson = {
                "Title": jobTitle,
                "Company": company,
                "Description": description
            }
            jobs.append(jobDetailsJson)
            print(*jobs, sep = "\n")    
    return jobs
#save data in JSON file
def saveDataInJSON(jobDetails):
    #Complete the missing part of this function here
    print("Saving data to JSON")

#main function
def main():
    # Write a code here to get job location and role from user e.g. role = input()
    print("Enter role you want to search")
    role = input()

    # Complete the missing part of this function here
    print("Enter location")
    location = input()
    getJobList(role,location)
    
if __name__ == '__main__':
    main()
