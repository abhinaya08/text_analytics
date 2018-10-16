# Analyzing Glassdoor reviews 

## Objective: 
1. Comparing employee reviews with company mission statements
2. Evaluating sentiment scores across Job Titles and Locations

## Process:
Following are the different pieces of analysis we did in order to evaluate how employees feel about their respective companies:

### 1. Wordcloud: 

Which are the most frequently occuring words when employees discuss the pros and cons of their respective companies?
[Code here](https://github.com/abhinaya08/text_analytics/blob/master/Project/1_wordcloud.ipynb)

### 2. Lift: 

Calculate lift scores by interacting "Pros and Cons Attributes" with "Company Categories"

#### Pros and Cons Attributes
* Pick the top frequent words adjective POS 
* Pros: great, good, happy, nice, decent, strong, flexible, new, friendly, positive, solid…etc.
* Cons: low, little, hard, difficult, poor, limited, bad, slow, terrible, conservative, less, bureaucratic…etc.

#### Five Categories
* Work life balance 
* Culture/ Value 
* Career Opportunity 
* Company Benefit 
* Senior Management 

#### Lift score calculation overview:
1. Tokenize each pros/cons review
2. Get POS, lemmentize and find pros_attibutes/ cons_attributes by getting adj POS
3. categorize reviews into 5 categories which match to glassdoor's rating categories and check their lift with pros and cons

[Code here](https://github.com/abhinaya08/text_analytics/blob/master/Project/2_Lift/)

### 3. Topic Modeling

We used LDA to do model for topics in unstructured review data. This helps us in identifying what employees percieve to be the positives and negatives of their respective companies
[Code here](https://github.com/abhinaya08/text_analytics/blob/master/Project/3_Topic%20Modeling.ipynb)

### 4. Cosine Similarity

Comparing company values to positive and negative reviews on Glassdoor. This enables us to classify the sentiment associated with company values. 
[Code here](https://github.com/abhinaya08/text_analytics/blob/master/Project/4_Sentiment%20and%20cosine%20similarity.ipynb)

### 5. Sentiment Analysis

How do employees across job titles and locations feel about the company?

We combine the positive and negative ratings to get a true assessment of employee sentiment
[Code here](https://github.com/abhinaya08/text_analytics/blob/master/Project/4_Sentiment%20and%20cosine%20similarity.ipynb)
