# BUILDING A REAL-TIME TWITTER SENTIMENT DASHBOARD USING PYTHON AND TABLEAU
 


## Getting Started:

You will need to create a free acount on twitter developer acount. After that you need to create an application and recieve the key's. Then copy that access token key's to the python file inside this project by the name of `kays_twitter` to grant your access to the twitter for collecting tweets.

## Usage:

Open the folder projectIT499, then to main_streamer.py run this file in case if there are all libraries available it must work fine. After runing of the file is finished you see there are many CSV files some of them by the name of data_SA refers to the tweets with sentiment analysis. Furthermore there ary many other CSV files by the name of Trends_SA which refers to the top five trends in each country.
Note: The last two litters after underscore refers to the name of each country.


## Tableau Dashboard: 
There is a file by the name of Dash.twbx which is desiged to visualize the result. To use this file you need to install Tableau software in your system or using [online tableau.](https://eu-west-1a.online.tableau.com/#/site/shams456778/workbooks/320661?:origin=card_share_link)

![image25](https://user-images.githubusercontent.com/52973147/78813443-ac10d280-79d5-11ea-8bad-7a8f323518d7.png)

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

The `requirements` file should list all Python libraries that project
depend on, and they will be installed using:

```
pip install -r requirements
```

