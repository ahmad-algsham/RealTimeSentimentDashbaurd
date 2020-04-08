"""
this code to calculate the percentage polarity
"""

import pandas as pd
import codecs

# read data that want to calculate
df = pd.read_csv(codecs.open('../data/data_SA.csv', 'rU', 'utf-16'), delimiter='\t')


pos_correct = 0
neg_correct = 0
nat_correct = 0

total = 0

for row in df['sentiment']:
    # print(row)
    data = row

    if data == 'positive':
        # print(data)
        pos_correct += 1

    elif data == 'negative':
        # print(data)
        neg_correct += 1
    elif data == 'neutral':
        # print(data)
        nat_correct += 1
    else:
        print('decrease')
        total -= 1
    total += 1

print("Positive accuracy = {:.2f}% via {} samples".format(float(pos_correct / total * 100.0), total))
print("Negative accuracy = {:.2f}% via {} samples".format(float(neg_correct / total * 100.0), total))
print("Natural  accuracy = {:.2f}% via {} samples".format(float(nat_correct / total * 100.0), total))
print("Number of spam = {}".format(2000 - total))


# -------------=-------------------=--------------------=-------------------=-----------------=--------------------=--

