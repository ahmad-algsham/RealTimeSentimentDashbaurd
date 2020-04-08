"""
here use for word cloud and the frequent
"""
import nltk
import pandas as pd
import codecs

from nltk import word_tokenize
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

import arabic_reshaper
from bidi.algorithm import get_display

from projectIT499 import regexarabic as ra
df = pd.read_csv(codecs.open('../projectIT499/marged.csv', 'rU', 'utf-16'), delimiter='\t')


# --------to collect all tweet--------                                                          change   name column

all_tweets = " ".join(ra.WordsFiltires(ra.remove(ra.harakat(ra.WordsFiltires(review)))) for review in df['Tweets_SA'])

# ---upload the figures----          change figure
mask_AE = np.array(Image.open('../Statistics/maps/om.png'))

# this code for the shape arabic word
data = arabic_reshaper.reshape(all_tweets)
data = get_display(data)  # add this line

# ------ato plot in cloud word format--------------------------------
wordcloud = WordCloud(font_path='arial', mask=mask_AE, background_color='white', mode='RGB',
                      width=2000, height=1000).generate(data)
plt.figure(figsize=(10, 10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
# --------------------------------------------------
# # plot the frecuancy
word_tokens = word_tokenize(data)
# print(word_tokens)

cts = nltk.FreqDist(word_tokens)
cts.plot(20)
