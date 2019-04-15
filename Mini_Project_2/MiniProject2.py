# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 16:52:11 2018

@author: TempAdmin1
"""

import pandas as pd
import requests
import datetime
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt 



# A program that fetches valid World Indices from Yahoo Finance and reads them 
#into a dataframe.

url = "https://in.finance.yahoo.com/world-indices/"
response = requests.get(url)

try:
    df = pd.read_html(response.content)[0]
except ConnectionError as e:
    assert df.dropna(how='any').isnull == 0, "try again"
else:
    print(df)


print(df.dropna(how='any'))
print('\n -For example(enter CSV without qoute marks or paste)/'
        '"df.Symbol.sample(n=5).tolist()" in the input for random indices-\n')

print(df.Symbol.sample(n=5).tolist())

# The 35 valid World Indices are then randomly selected converted into a list
if __name__ == '__main__':
    def main():
        try:
            indices = input("Enter few indices from https://in.finance.yahoo.com/world-indices in CSV format:")
            index = indices.strip().split()
        except AttributeError as e:
            assert index, "invalid entry"
        else:
            index = df.Symbol.sample(n=5).tolist()
            return index
#Download data for the last 10 years for each of the Indices. 
#Date automated to 10 years from today

startDate = datetime.date.today() -datetime.timedelta(weeks=520)
endDate = datetime.date.today()

# download Panel
data = pdr.get_data_yahoo(main(), start= startDate, end = endDate)['Adj Close']


#clean the data with dropna
clean_data = data.dropna(how='any')
 
# Calculate the array of daily returns 
ret = clean_data.shift(1) / clean_data - 1 

# Pearson's correlation coefficients

corr= ret.corr()

  
print('\n --- Correlational Interdependence -- \n', corr)


#Show color map of correlation interdependence
print('\n --- Correlation Coefficients -- \n')
plt.imshow(corr, cmap='jet', interpolation='none') 
plt.colorbar() 
plt.xticks(range(len(corr)), corr.columns) 
plt.yticks(range(len(corr)), corr.columns) 
plt.show()

# Print the details of the Variability or Trend Relationships 

print('\n --- Trend Variability -- \n')

print(corr**2)    
print('\n --- Variability (R-squared) -- \n')
plt.imshow(corr**2, cmap='jet', interpolation='none') 
plt.colorbar() 
plt.xticks(range(len(corr)), corr.columns) 
plt.yticks(range(len(corr)), corr.columns) 
plt.show()


