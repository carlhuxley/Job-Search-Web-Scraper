# Job-Search-Web-Scraper

This project was born because it was so difficult for me to keep track of the amount of data jobs on recruitment websites.
Its too time consuming cutting and pasting all of this imformation into an Excel spreadsheet for further analysis.

This code allows the scraping of job details from the cwjobs.co.uk website.  You can search for a given job title and location over a specific time period and export the data to a CSV file.

It's a simple way to export a list of jobs you are interested in to Excel giving the following information:
* Job Keyword & Location
* Job Title 
* Salary
* Job Detail Page Link
* Closing Date
* Hiring Organisation
* Hiring City & Region
* Job Description

You can easily customise your search by changing:
* The date the jobs were posted
* Combinations of Job title and job location

## User Guide
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
## Other Features
I've created a corpus of all the job descriptions in the dataset.
```Python
def create_corpus(jobs):
    corpus = []
   
    for j in jobs:
        corpus.append(j['Description'])
        
    return corpus
```
I've used the NLTK library to remove stopwords and turn the remaining keywords into stem words giving me a bag of words model.
```Python
 from sklearn.feature_extraction.text import CountVectorizer
    cv = CountVectorizer(ngram_range=(1, 3), min_df = 2 )
    X = cv.fit_transform(corpus).toarray()
    #Show the words in the bag
    words = cv.get_feature_names()
 ```
 From here I intend to do some analysis & visualisations on the job descriptions.
 For instance I'm interested in finding out what are the most frequently used words in job descriptions for each job search keyword.
 This could help me to learn which skills/techologies are the most popular. I can then see if there is anything I need to learn/brush up on. I can also decide where to concentrate my time and energy.
 
 ## Future Improvements
 The code needs refactoring if I want to expand it's functionality. It at least needs splitting into data extraction, cleaning and language processing modules. I want to convert functions into object methods.
 
 I'm thinking of using machine learning for analysis of the job descriptions and to automatically edit my CV to suit them. 
 At this point it would be possible, using the job detail hyperlink, to automate sending customised online job applications. I could even automate adding the recruiter contact information from the 'thank you' page to my original spreadsheet for follow-up purposes.
