# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 07:55:23 2018
Mini Project: 1
@author: Tawanda Vera
"""

# The statsmodels.api is used for the 2 variable regression calculation
# Pandas are used for data analysis
# scipy is used to calulate the annualized stock volatility

import statsmodels.api as sm
import pandas as pd
import scipy as sp


#############################################################################
# Problem 1: Descriptive Statistics In Python
#############################################################################

# Download data for the JP Morgan stock historical prices Yahoo Finance:

""" 1. Download data for the JPM.csv file from:"""

# https://finance.yahoo.com/quote/JPM/history?p=JPM

# Then Use Pandas to read the JPM.csv file saved in the Project directory:
"""
The data is checked and the Adj Closing Prices are in Column 5, so we\
import only column 5 into the pandas.
The dataframe.sort_index() is used to ensure that the adj. closing prices\
are in ascending order
"""
jpm = (pd.read_csv('JPM.csv', usecols=[5])).sort_index()

# 1. Calculate the Average Stock Price:

print("1. Average Stock value :", jpm.mean())

# Calculate the Simple Daily Returns using (P0 - P1)/P1
"""
The dropna() suffix is used for Filtering Out Missing Data
"""
j_ret = (jpm.pct_change()).dropna()

print("3. Daily Returns:", j_ret.mean)

# Calculate the Volatility of JPM stock

print("2. Volatility:", sp.sqrt(252)*(j_ret.std()))


#############################################################################
# Problem 3: Descriptive Statistics In Python
#############################################################################
# Download data for the JP Morgan stock historical prices Yahoo Finance:

""" 4. Download data for the ^GSPC.csv file from:"""

# https://finance.yahoo.com/quote/^GSPC/history?p=^GSPC

# Then Use Pandas to read the ^GSPC.csv file saved in the Project directory:
sp500 = pd.read_csv('^GSPC.csv', usecols=[5]).sort_index()

# Calculate the Simple Daily Returns using (P0 - P1)/P1
sp_ret = ((sp500 - sp500.shift(1))/sp500.shift(1)).dropna()

# Correctly specify the model by adding the intercept
sp_ret = sm.add_constant(sp_ret)

# specify the OLS endogenous and exogenous
reg1 = sm.OLS(endog=j_ret, exog=sp_ret)
type(reg1)


# Constructed the model

sm.regression.linear_model.OLS

# We need to use .fit() to obtain parameter estimates coeff and std err
results = reg1.fit()
type(results)


# We now have the fitted regression model stored in results
sm.regression.linear_model.RegressionResultsWrapper

# To view the OLS regression results, we can call the .summary() method
print(results.summary())

#############################################################################