# Job-Search-Web-Scraper

This project was born because it was so difficult for me to research of all of the jobs listed daily on recruitment websites.
It's too time-consuming cutting and pasting all of the information into an Excel spreadsheet for further analysis.

This code allows the scraping of job details from the cwjobs.co.uk website. 
You can search for a given keyword, location, over a specific time period and export the data to a CSV file.

It's easy to customise your search criteria by altering the search_list.csv file. 

Using the following data row in the search_list.csv file:
keyword = data-analyst, location = london, radius = 20, postedwithin = 7 
Returns => data analyst jobs within a 20mile radius of London posted in the last week.

If you want to do multiple searches just add more rows to the file.

Change the file path to where you want to save the exported csv file.
```Python
file_name = 'C:\Files\Carl\Career\Research\job_searches\{}_cwjobs.csv'.format(today)
print (file_name)
export_df = df.to_csv(file_name, sep = ',', index = False, encoding='utf-8-sig')
```
## Other Features
Its a work in progress but I've created a corpus of all the job descriptions in the dataset.
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