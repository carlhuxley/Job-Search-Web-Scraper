# Job-Search-Web-Scraper
This code allows the scraping of job details from the cwjobs.co.uk website and export the data to a CSV file.

It's a simple way to export a list of jobs you are interested in to Excel giving the following information:
* Job Keyword & Location
* Job Title 
* Salary
* Job detail page link
* Closing Date
* Hiring Organisation
* Hiring City & Region
* Job Description

You can easily customise your search by changing:
* The date the jobs were posted
* Combinations of Job title and job location

## Users Guide
If you want to see the latest postings leave the 'postedwithin' value to 1. If you want to see what's been posted over the last week change the value to 7 etc.
```Python
def get_job_list(keyword, location): 
       
    job_list = []     
      
    url ='https://www.cwjobs.co.uk/jobs/{}/in-{}?radius=30&postedwithin=1'.format(keyword,location)
```
By changing the list values here you can search on as many combinations of job title and job location as you like.
```Python
search_list = [['reports-developer', 'manchester'],['data-analyst', 'manchester'],
               ['bi-developer', 'bradford'],['reports-developer', 'bradford'],
               ['bi-developer', 'manchester'],['reports-developer', 'stoke-on-trent']]
```
Change the file path to where you want to save the exported csv file.
```Python
file_name = 'C:\Files\Carl\Career\Research\job_searches\{}_cwjobs.csv'.format(today)
print (file_name)
export_df = df.to_csv(file_name, sep = ',', index = False, encoding='utf-8-sig')
```
