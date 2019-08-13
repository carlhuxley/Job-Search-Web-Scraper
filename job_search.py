# -*- coding: utf-8 -*-
"""
Created on Fri May 17 10:24:32 2019

@author: Carl Huxley
"""
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('headless') 
options.add_argument('window-size=1366x662') 
from bs4 import BeautifulSoup
from datetime import date
import pandas as pd
import json
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from IPython.core.debugger import set_trace
ps = PorterStemmer()
jobs = []

class Job():
    
    def __init__(self):
       
        self.title = ""
        self.link = ""
        self.salary = ""
        self.json = ""
        self.date_posted = ""
        self.valid_through = ""
        self.hiring_organisation_name = ""
        self.hiring_city = ""
        self.hiring_region = ""
        self.description = ""
         
def get_job_list(keyword, location): 
       
    job_list = []     
      
    url ='https://www.cwjobs.co.uk/jobs/{}/in-{}?radius=30&postedwithin=1'.format(keyword,location)
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    
    #find total search results pages
    pages = soup.find('ul', class_ = 'pagination adjacent-to-drilldown')
    page_num = 1
    if pages is not None:
        page_num = len(pages.find_all('li'))-2
   
    for page in range(1, page_num + 1):
          
        # download html page 
        if page > 1:
            new_url = url + '&page={0}'.format(page)
            driver = webdriver.Chrome(options=options)
            driver.get(new_url)
         
        # create soup
        soup = BeautifulSoup(driver.page_source, 'lxml')
            
        div = soup.find('tbody')
            
        for div in soup.find_all('div', class_ = "job-title"):
            for a in div.find_all('a'):
                    new_job = Job()
                    new_job.title = a.text
                    new_job.link = a["href"]
                    job_list.append(new_job)
            
    driver.quit()
       
    return job_list 

def get_detail_for_all_jobs(job_list):
    driver = webdriver.Chrome(options=options)
    for j in job_list:
        url = j.link
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        json_text = soup.find('script',{'id':'jobPostingSchema'})
        j.salary = soup.find('li', class_='salary icon').find("div", recursive=False).text.strip()
        #j.salary = salary.replace("Â", "")
        j.json = json_text
        j.title = json.loads(j.json.text)['title']
        j.date_posted = json.loads(j.json.text)['datePosted']
        j.valid_through = json.loads(j.json.text)['validThrough']
        j.hiring_organisation_name = json.loads(j.json.text)['hiringOrganization']['name']
        j.hiring_city = json.loads(j.json.text)['jobLocation']['address']['addressLocality']
        j.hiring_region = json.loads(j.json.text)['jobLocation']['address']['addressRegion']
        j.description = json.loads(j.json.text)['description']
        
        job = {
        'Keyword':keyword,
        'Location':location,
        'Title':j.title, 
        'Salary':j.salary,
        'Link':j.link, 
        'Date Posted':j.date_posted, 
        'Valid Through':j.valid_through, 
        'Hiring Organisation':j.hiring_organisation_name, 
        'Hiring City':j.hiring_city, 
        'Hiring Region':j.hiring_region, 
        'Description':clean_description(j.description)
                }
        jobs.append(job)
        
    return jobs

def clean_description(description):
    letters_only = re.sub("[^a-zA-Z0-9]", " ", description)                   
                       
    query = letters_only
    #need to improve the way markup is removed from descriptions! eg text-align
    markup = ['strong','gt','lt','li','ul','br','div','span','amp','b','nbsp', 
              'text','align','justify','p','style','font','weight']
    querywords = query.split()

    resultwords  = [word for word in querywords if word.lower() not in markup]
    description = ' '.join(resultwords)
    
    #description = description.lower()
    
    #bag_of_words = description.split()
    
    #bag_of_words = [ps.stem(word) for word in bag_of_words if not word in set(stopwords.words('english'))]
    
    #description = ' '.join(bag_of_words)
    
    return description

def create_corpus(jobs):
    corpus = []
   
    for j in jobs:
        corpus.append(j['Description'])
        
    return corpus

#Search for jobs and create dataframe and output a csv using the criteria below 
#You need two lists, one locations and the other keywords. combine both lists

search_list = [['reports-developer', 'manchester'],['data-analyst', 'manchester'],
               ['bi-developer', 'bradford'],['reports-developer', 'bradford'],
               ['bi-developer', 'manchester'],['reports-developer', 'stoke-on-trent']]

for search_item in search_list:
    
    keyword = search_item[0]
    location = search_item[1]

    #Call the job detail function passing in the get job list function
    jobs = get_detail_for_all_jobs(get_job_list(keyword, location))
    
    corpus = create_corpus(jobs)
    
    df = pd.DataFrame(jobs, columns = ['Keyword', 'Location', 'Title', 'Salary',
                                       'Link', 'Date Posted', 'Valid Through',                                   
                                       'Hiring Organisation', 'Hiring City',
                                       'Hiring Region', 'Description'])
    
    #create bag of words model
    from sklearn.feature_extraction.text import CountVectorizer
    cv = CountVectorizer(ngram_range=(1, 3), min_df = 2 )
    X = cv.fit_transform(corpus).toarray()
    #Show the words in the bag
    words = cv.get_feature_names()
    print (words)
    
    #Export the dataframe as a csv file
    today = date.today()
    today = today.strftime('%Y%m%d')
  
file_name = 'C:\Files\Carl\Career\Research\job_searches\{}_cwjobs.csv'.format(today)
print (file_name)
export_df = df.to_csv(file_name, sep = ',', index = False, encoding='utf-8-sig')
