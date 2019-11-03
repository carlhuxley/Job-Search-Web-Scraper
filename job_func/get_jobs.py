# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 10:19:21 2019

@author: Carl Huxley

This module gets job summaries and details from the cwjobs.co.uk website.
"""
import json
from selenium import webdriver
from bs4 import BeautifulSoup
import job_func.process_description

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1366x662')

jobs = []


class Job():
    """
    This class initialises the job object.
    """

    def __init__(self):
        self.keyword = ""
        self.location = ""
        self.title = ""
        self.radius = ""
        self.link = ""
        self.salary = ""
        self.job_type = ""
        self.json = ""
        self.date_posted = ""
        self.valid_through = ""
        self.hiring_organisation_name = ""
        self.hiring_city = ""
        self.hiring_region = ""
        self.hiring_contact = ""
        self.hiring_reference = ""
        self.job_id = ""
        self.description = ""


def get_job_list(keyword, location, radius, posted):
    """
    This function takes keyword, location, radius and postedwithin as arguments.
    It returns a list of job detail urls from cwjobs.co.uk.
    """
    job_list = []

    url = 'https://www.cwjobs.co.uk/jobs/{}/in-{}?radius={}&postedwithin={}'.format(keyword, location, radius, posted)
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'lxml')

    # find total search results pages
    pages = soup.find('ul', class_='pagination adjacent-to-drilldown')
    page_num = 1
    if pages is not None:
        page_num = len(pages.find_all('li')) - 2

    for page in range(1, page_num + 1):

        # download html page
        if page > 1:
            new_url = url + '&page={0}'.format(page)
            driver = webdriver.Chrome(options=options)
            driver.get(new_url)

        # create soup
        soup = BeautifulSoup(driver.page_source, 'lxml')

        div = soup.find('tbody')

        for div in soup.find_all('div', class_="job-title"):
            for a in div.find_all('a'):
                    new_job = Job()
                    new_job.keyword = keyword
                    new_job.location = location
                    new_job.radius = radius
                    new_job.title = a.text
                    new_job.link = a["href"]
                    job_list.append(new_job)

    driver.quit()

    return job_list


def get_detail_for_all_jobs(job_list):
    """
    This functions takes a list of job urls and returns a list of job objects.
    """

    driver = webdriver.Chrome(options=options)
    for j in job_list:
        url = j.link
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        json_text = soup.find(
            'script', {'id': 'jobPostingSchema'}
        )
        j.salary = soup.find(
            'li', class_='salary icon').find("div", recursive=False).text.strip()

        try:
            j.job_type = soup.find(
                'li', class_='job-type icon').find("div", recursive=False).text.strip()

        except:
            j.job_type = "_"

        j.json = json_text
        j.title = json.loads(j.json.text)['title']
        j.date_posted = json.loads(j.json.text)['datePosted']
        j.valid_through = json.loads(j.json.text)['validThrough']
        j.date_added = None
        j.date_applied = None
        j.hiring_organisation_name = json.loads(j.json.text)['hiringOrganization']['name']
        j.hiring_city = json.loads(j.json.text)['jobLocation']['address']['addressLocality']
        j.hiring_region = json.loads(j.json.text)['jobLocation']['address']['addressRegion']
        contact_reference = soup.find('ul', class_='contact-reference hidden-xs').findAll('li')

        try:
            j.hiring_contact = (contact_reference[0].text.strip().split(":"))[1]
        except TypeError:
            j.hiring_contact = "-"

        j.hiring_reference = contact_reference[1].text.strip().split(":")[1]
        j.job_id = contact_reference[2].text.strip().split(":")[1]
        j.description = str(soup.find('div', class_='job-description'))

        job = {
        'search_keyword': j.keyword,
        'search_location': j.location,
        'search_radius': j.radius,
        'title': j.title,
        'salary': j.salary,
        'job_type': j.job_type,
        'link': j.link,
        'date_added': j.date_added,
        'date_posted': j.date_posted,
        'valid_through': j.valid_through,
        'date_applied': j.date_applied,
        'hiring_organisation': j.hiring_organisation_name,
        'hiring_city': j.hiring_city,
        'hiring_region': j.hiring_region,
        'hiring_contact': j.hiring_contact,
        'hiring_reference': j.hiring_reference,
        'job_id': j.job_id,
        'description':j.description}
        jobs.append(job)

    return jobs
