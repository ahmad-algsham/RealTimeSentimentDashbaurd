# BUILDING A REAL-TIME TWITTER SENTIMENT DASHBOARD USING PYTHON AND TABLEAU
 
## Getting Started:

You will need to create a free acount on twitter developer acount. After that you need to create an application and recieve the key's. Then copy that access token key's to the python
file inside this project by the name of kays_twitter to grant your access to the twitter for collecting tweets.

## Requirements:

There are some libraries which are needed and you have to install them before you run the code, otherwise you face to problem.

1. gensim == 3.8.1
2. nltk == 3.4.5
3. pandas == 1.0.3
4. tweepy == 3.8.0
5. textblob-ar-mk == 0.0.2

6. wordcloud == 1.6.0
7. arabic-reshaper == 2.0.15
8. python-bidi == 0.4.2

To install these libraries samply you have to opent the file by the name of "requirements" and run it using cmd or pycharm it will
install all those requirements.

```
pip install -r requirements
```

## Usage:
Open the folder uisng Pycharm, then go to main_streamer.py and run this file in case if there are all libraries available it must work fine. After runing of the file is finished you see there are many CSV files some of them by the name of data_sa refers to the tweets with sentiment analysis. Furthermore there ary many other CSV files by the name of Trends_SA which refers to the top trends in each country.
Note: The last two litters after underscore refers to the name of each country.

## Tableau Dashboard:
There is a file by the name of Dash.twbx which is desiged to visualize the result. To use this file you need to install Tableau software in your system or using online tableau.





## Results at Tablea 
* SciKit-Learn ML algorithms 
    * https://www.kaggle.com/mksaad/sentiment-analysis-in-arabic-tweets-using-sklearn

* NLTK Naive Bayes 
    * https://www.kaggle.com/mksaad/arabic-sentiment-analysis-in-tweets-nb-bow

    * https://www.kaggle.com/mksaad/arabic-sentiment-analysis-in-tweets-nb-bigrams
