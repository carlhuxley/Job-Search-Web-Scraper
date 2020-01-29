# Job-Search-Web-Scraper
I started this python coding project because it was so difficult for me to research all of the jobs listed daily on recruitment websites. It's also too time-consuming copying and pasting all of the information into an Excel spreadsheet for further analysis. Using Python Flask, sqlalchemy, Beautiful Soup, Pandas and Selenium I’ve developed a custom job research tool. Job search criteria entered into a web form is processed by a web scraper that returns a date stamped CSV file and also adds the results to the SQLite database.

The next stage is adding job application functionality. I will be able to choose the jobs from the list I want to apply for, and which version of my CV I want to use. When I click the apply button the tool will apply for all the jobs on the list. Now this is working with cwjobs.co.uk I can extend this to researching and applying for jobs on multiple job boards. Looking to change the Selenium/Beautiful Soup based scraper to one using the Scrapy Framework so it's easier to manage scraping from multiple sites.


Entering the following into the job search form:
keyword = data-analyst, location = london, radius = 20, postedwithin = 7
Returns => data analyst jobs within a 20 mile radius of London posted in the last week.

You can change the file path to where you want to save the exported csv file. Change the path in job_search.py line 41
```Python
file_name = 'C:\Files\Carl\Career\Research\job_searches\{}_cwjobs.csv'.format(today)
print (file_name)
export_df = df.to_csv(file_name, sep = ',', index = False, encoding='utf-8-sig')
```
## Other Features
It's a work in progress but I've created a corpus of all the job descriptions in the dataset.
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
I'm thinking of using machine learning for analysis of the job descriptions and to automatically edit my CV to suit them.
At this point it would be possible, using the job detail hyperlink, to automate sending customised online job applications.