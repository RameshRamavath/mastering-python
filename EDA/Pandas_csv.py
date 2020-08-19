"""
Pandas - Useful for data manipulation and Analysis

Analysis on load data - /Users/313248/PycharmProjects/mastering-python/Resources/Loan_data.csv

Columns -



"""

import pandas as pd

data = pd.read_csv("/Users/313248/PycharmProjects/mastering-python/Resources/character-predictions.csv")
#print(data.head())
#print(data.describe())

data2 = data[:2]
print (data2.head())