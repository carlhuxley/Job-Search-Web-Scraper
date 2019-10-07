# -*- coding: utf-8 -*-
"""
Created on Fri May 17 10:24:32 2019

@author: Carl Huxley

This code web scrapes job details from cwjobs.co.uk. and exports a csv file.
"""
from selenium import webdriver
from datetime import date
import get_jobs
import process_description
import pandas as pd
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1366x662')
keyword = ""
location = ""
radius = ""
posted = ""


# Import a search list csv file into a dataframe


def job_search(keyword, location, radius, posted):

    # Call the job detail function passing in the get job list function
    jobs = get_jobs.get_detail_for_all_jobs(get_jobs.get_job_list(keyword, location, radius, posted))

    df = pd.DataFrame(jobs, columns=['Search Keyword', 'Search Location',
      'Search Radius', 'Title', 'Salary', 'Job Type', 'Link', 'Date Posted',
      'Valid Through', 'Hiring Organisation', 'Hiring City', 'Hiring Region',
      'Hiring Contact', 'Job Reference', 'Job ID', 'Description'])

    # Export the dataframe as a csv file

    today = date.today()
    today = today.strftime('%Y%m%d')

    file_name = f'C:\Files\Carl\Career\Research\job_searches\{today}_cwjobs.csv'
    print(file_name)
    df.to_csv(file_name, sep=',', index=False, encoding='utf-8-sig')
    return jobs
