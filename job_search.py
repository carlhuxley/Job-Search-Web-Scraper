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
from get_jobs import get_job_list
from get_jobs import get_detail_for_all_jobs
from process_description import create_corpus
import pandas as pd

#Search for jobs and create dataframe and output a csv using the criteria below 
#You need two lists, one locations and the other keywords. combine both lists

search_list = [['reports-developer', 'manchester'],['data-analyst', 'manchester'],
               ['bi-developer', 'bradford'],['reports-developer', 'bradford'],
               ['bi-developer', 'manchester'],['reports-developer', 'stoke-on-trent']]

for search_item in search_list:
    
    keyword = search_item[0]
    location = search_item[1]

    #Call the job detail function passing in the get job list function
    jobs = get_detail_for_all_jobs(get_job_list(keyword, location, 1))
    
    corpus = create_corpus(jobs)
    
    df = pd.DataFrame(jobs, columns = ['Search Keyword', 'Search Location', 'Title', 'Salary',
                                       'Link', 'Date Posted', 'Valid Through',                                   
                                       'Hiring Organisation', 'Hiring City',
                                       'Hiring Region', 'Description'])
 
    #Export the dataframe as a csv file
    today = date.today()
    today = today.strftime('%Y%m%d')
  
file_name = 'C:\Files\Carl\Career\Research\job_searches\{}_cwjobs.csv'.format(today)
print (file_name)
export_df = df.to_csv(file_name, sep = ',', index = False, encoding='utf-8-sig')
