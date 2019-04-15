# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 08:41:13 2018

@author: TempAdmin1
"""
import quandl  #pip install quandl
import datetime
import pandas as pd
import numpy as np 
import scipy.interpolate
import pylab
from scipy import optimize
import matplotlib.pyplot as plt

##############################################################################

"""
1. Write a python program that prompts the user to enter /
 any valid stock symbol available in Yahoo! Finance for NYSE & NASDAQ.
 Ensure proper error handling for wrong user inputs.
 """

# Due to challenges in getting free APIs to download symbols/
#listing.csv files for NYSE, NASDAQ listings were downloaded from /
#www.nasdaq.com/screening/company-list.aspx to create allow for 
#the lookup query to be used in error handling.

print('1a. The lists below shows the stock names and symbols for NYSE & NASDAQ');

NASDAQ= pd.read_csv('nasdaq_listings.csv', index_col=1, skiprows=1);

print(NASDAQ)

NYSE= pd.read_csv('nyse_listings.csv', index_col=1, skiprows=1);

print(NYSE)

#User is prompted to enter valid

print('From the lists above please choose the stock to be evaluated')


print("###################################################################");

############################################################################
# pip install Quandl was used to install the Quandl module. It is then 
# imported into  the code. Some of the Quandl WIKI stock codes are different
# from the Yahoo Finance symbols or tickers, which results in a ValueError. 
# Exception
quandl.ApiConfig.api_key = 'MgUeDFrhs9JjaA4gKzEx'
 
def quandl_stocks(symbol, start_date=(2017, 12, 20), end_date=None):
    """
    symbol is a string representing a stock symbol, e.g. 'AAPL'
 
    start_date and end_date are tuples of integers representing the year, month,
    and day
 
    end_date defaults to the current date when None
    """
 
    query_list = ['WIKI' + '/' + symbol + '.' + str(k) for k in range(1, 13)]
 
    start_date = datetime.date(*start_date)
 
    if end_date:
        end_date = datetime.date(*end_date)
    else:
        end_date = datetime.date.today()
 
    return quandl.get(query_list, 
            returns='pandas', 
            start_date=start_date,
            end_date=end_date,
            collapse='daily',
            order='asc'
            )
 
if __name__ == '__main__':
   try:
    sym_data= quandl_stocks(input("Enter stock to be evaluated: "))
   except ValueError:
    print("Oops! That was no valid Quandl Stock Symbol for NYSE" ,
          "or NASDAQ.  Try again...")
   finally:
       
       sym_data= quandl_stocks("AAPL")
       
print(sym_data)

print('#####################################################################')       


print("""2. Download data for last 1 month for user entered ticker 
from Quandl WIKI website.""")

#Using the AAPL stock data the quotes were ndarrayed and transposed to
#closing and adjusted closing is used as the value of x in the interpolation

quotes = np.array(sym_data) 

symACl = quotes.T[10] 

symCl = quotes.T[3]

print(symCl)

print("""
##############################################################################

""")

"""3. Using Interpolation techniques, fit a quadratic line'/
      "through the data points and plot the same"""

import numpy as np
import scipy.interpolate
import pylab

def createBaseData (n):
    """ Given an integer n, returns n data points
    x and values y as a numpy.array."""
    xmax = 5.
    x = np. linspace (0, xmax , n)
    y =  x**2
    #make x -data somewhat irregular
    y += 1.5 * np. random.normal (size=len(x))
    return x, y


if __name__ == '__main__':
    n = 10
    x, y = createBaseData (n)
    # Develop a regular mesh for plot
    xfine = np.linspace(0.1 , 4.9, n * 100)
    # interpolate with piecewise linear func (p=1)
    y1 = scipy.interpolate.interp1d (x, y, kind='linear')
    # interpolate with quadratic fit(p=2)
    y2 = scipy.interpolate.interp1d (x, y, kind='quadratic')
    #Dynamic interpolation with splines of varying order
    y0 = scipy.interpolate.interp1d (x, y, kind='nearest')
    pylab.plot(x, y, 'o', color='yellow', label='ActualData Values')
    pylab.plot(xfine , y0(xfine), label='Nearest Fit')
    pylab.plot(xfine , y1(xfine), label='Linear Fit')
    pylab.plot(xfine , y2(xfine), label='Quadratic Fit')
    pylab.errorbar(x, y)
    pylab.legend ()
    pylab.xlabel ('x values')
    pylab.show ()


print("####################################################################")

"""4. Choose a quadratic equation of your choice /
      "and using SciPy leastsq() optimization method /
      "calculate the best fit line with respect to the downloaded data /"""
 
def f(x):
    return x**2 + 10*np.sin(x)

ret = np.log(symCl / symCl.shift(1))

x = np.arange(ret)
plt.plot(x, f(x))
plt.show()
############################################################
# Now find the minimum with a few methods
# The default (Nelder Mead)
print(optimize.minimize(f, x0=0))

print(optimize.minimize(f, x0=0, method="L-BFGS-B"))

############################################################


