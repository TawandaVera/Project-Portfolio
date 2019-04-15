# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 07:55:23 2018
Mini Project: 1
@author: Tawanda Vera
"""


# Pandas are used for calculating returns
# statsmodels is used to calculate the CAPM alpha and beta

import statsmodels.api as sm
import pandas as pd
from scipy import stats


# Download and Calculate Stock returns
#############################################################################

# Download data for the targeted stock historical prices Yahoo Finance:

# https://finance.yahoo.com/quote/ORCL/history?p=ORCL

# Then Use Pandas to read the csv file saved in the Project directory:
"""
The data is checked and the Adj Closing Prices are in Column 5, so we\
import only column 5 into the pandas.
The dataframe.sort_index() is used to ensure that the adj. closing prices\
are in ascending order
"""
orcl = (pd.read_csv('ORCL.csv', usecols=[5])).sort_index()

sp500 = pd.read_csv('^GSPC.csv', usecols=[5]).sort_index()


# Calculate the Simple Daily Returns using (P0 - P1)/P1
"""
The dropna() suffix is used for Filtering Out Missing Data
"""
orcl_ret = (orcl.pct_change()).dropna()

sp_ret = (sp500.pct_change()).dropna()

print(orcl_ret.mean()))
#############################################################################
# Calculate the CAPM using Scipy stats module

sp_ret = sm.add_constant(sp_ret)

# specify the OLS endogenous and exogenous
reg1 = sm.OLS(endog=orcl_ret, exog=sp_ret)
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
# Discuss the regression summary results provided by Python
#############################################################################
