# -*- coding: utf-8 -*-
"""
Created on Fri May 17 10:24:32 2019

@author: Carl Huxley
"""
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('headless') 
options.add_argument('window-size=1366x662') 
from datetime import date
import job_func.get_jobs
import job_func.process_description
import pandas as pd

keyword=""
location = ""
radius = ""
postedwithin = ""

#Import a search list csv file into a dataframe
df = pd.read_csv('search_list.csv')
#Iterate over the dataframe for each row in it updating search variables
for index, search in df.iterrows():
    keyword = search['keyword']
    location = search['location']
    radius = search['radius']
    postedwithin = search['postedwithin']
    
    #Call the job detail function passing in the get job list function
    jobs = job_func.get_jobs.get_detail_for_all_jobs(job_func.get_jobs.get_job_list(keyword, location, radius, postedwithin))
    
    corpus = job_func.process_description.create_corpus(jobs)
    
    df = pd.DataFrame(jobs, columns = ['Search Keyword', 'Search Location', 
                                       'Search Radius', 'Title', 'Salary',
                                       'Link', 'Date Posted', 'Valid Through',                                   
                                       'Hiring Organisation', 'Hiring City',
                                       'Hiring Region', 'Description'])
 
#Export the dataframe as a csv file
    
today = date.today()
today = today.strftime('%Y%m%d')
  
file_name = 'C:\Files\Carl\Career\Research\job_searches\{}_cwjobs.csv'.format(today)
print (file_name)
export_df = df.to_csv(file_name, sep = ',', index = False, encoding='utf-8-sig')
