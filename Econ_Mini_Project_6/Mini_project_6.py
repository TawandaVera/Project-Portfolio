# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 05:01:02 2018

@author: Tawanda Vera
"""


import pandas_datareader as web
import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.base.datetools import dates_from_str
from statsmodels.tsa.api import VAR
from statsmodels.tsa.stattools import adfuller, coint
import statsmodels.graphics.tsaplots
import matplotlib.pyplot as plt

##############################################################################
# Data preparation
##############################################################################

# Variables from Fred Database
"INDPRO"	
# Industrial Production Index, Index 2012=100, Monthly, Seasonally Adjusted
"JPNPROINDMISMEI"
# Production of Total Industry in Japan, Index 2010=100, Monthly, Seasonally Adjusted
"CPIAUCSL"
# US Consumer Price Index for All Urban Consumers: All Items,
# Index 1982-1984=100, Monthly, Seasonally Adjusted
"JPNCPIALLMINMEI"
# Consumer Price Index of All Items in Japan,
# Index 2010=100, Monthly, Not Seasonally Adjusted
"FEDFUNDS"
# Effective Federal Funds Rate, Percent, Monthly, Not Seasonally Adjusted
"INTDSRJPM193N"
# Interest Rates, Discount Rate for Japan, Percent per Annum,
# Monthly, Not Seasonally Adjusted
"EXJPUS"
# Japan / U.S. Foreign Exchange Rate, Japanese Yen to One U.S. Dollar,
# Monthly, Not Seasonally Adjusted

# Download data from Fred 
indicator = ["EXJPUS", "INDPRO", "JPNPROINDMISMEI", "CPIAUCSL", "FEDFUNDS",
             "INTDSRJPM193N", "JPNCPIALLMINMEI"]

df = web.DataReader(indicator, 'fred').dropna() 

# Rename the columns
df.columns = ['fx', 'ip_US', 'ip_JP', 'cpi_US', 'fed_rate',
              'jpn_rate', 'cpi_JP']

# Check period of valid data 
df.tail()
df.head()
"Period Jan 2010 to April 2017"



##############################################################################
# Q2. Calculate the equilibrium FX using cointegration with one macroeconomic
# variable
##############################################################################

# Jap/US FX movement as determined by the Consumer Price Index (CPI)
#
fx = df['fx'].values
#Logarithm values
cpi_US = np.log(df['cpi_US'])
cpi_JP = np.log(df['cpi_JP'])

# To determine the order of integration or the stationarity of each series
# Perform a Cointegration test with a function as follows:
# Define a function that implements linear regression and returns 
# the ADF test results:
#
def calc_adf(x, y): 
    result = sm.OLS(x, y).fit() 
    return adfuller(result.resid) 

# Calculate the cointegration of how with itself: 
print("fx & cpi_US ADF test:", calc_adf(fx, cpi_US))
print("fx & cpi_JP ADF test:", calc_adf(fx, cpi_JP))
print("cpi_JP & cpi_US ADF test:", calc_adf(cpi_US, cpi_JP ))

# Comments
#
print('\n The cointegration p-values for three variables fx & cpi_US (-1.01),\
      fx & cpi_JP (-1.01) and cpi_JP & cpi_US (-2.38) are all higher or less \
      negative compared to the critical values of(1%)= -3.51,\
      (5%) = -2.90 and (10%) = -2.58. Therefore, there is strong evidence to\
      suggest that we cannot reject the null hypothesis (unit root). And\
      conclude that the variables fx, cpi_US, and cpi_JP are nonstationary')

# The nonstationary variables become stationary after applying 
# the first difference as follows:

mdf = df[['fx', 'cpi_US', 'cpi_JP']]
data = np.log(mdf).diff().dropna() # Applying the first difference
e_t = data['fx']        # e_t – log of the price of foreign exchange
p_t = data['cpi_US']    # p_t – log of domestic price level
p_ft = data['cpi_JP']    # p_ft – log of foreign price level

# According to long-run Purchasing Power Parity (PPP), there is a linear 
# combination e_t + p_ft -p_t that is stationary.
# Calculated as follows:

equilibrium_fx = df['equilibrium_fx'] = e_t + p_t - p_ft

# Equilibrium_fx implies that domestic and foreign price levels 
# are cointegrated, as follows:
print("e_t & p_ft ADF test:", calc_adf(e_t, p_ft))
print("e_t & p_t ADF test:", calc_adf(e_t, p_t))
print("p_ft & p_t ADF test:", calc_adf(p_ft, p_t ))
print("e_t & equilibrium_fx ADF:", calc_adf(e_t, equilibrium_fx))

# Comments

print('\n The cointegration p-values for the first difference variables\
      e_t & p_ft (-6.36), e_t & p_t (-6.35) and p_ft & p_t (-6.88) are more\
     negative than the critical values, which implies that they have become\
     stationary variables. Additionally, the results supports the long-run \
     Purchasing Power Parity (PPP) theory on the linear combination \
     e_t + p_ft -p_t being stationary.\
     Thus, the equilibrium_fx represents the cointegration of domestic and\
     foreign price levels\n')

##############################################################################
# Q3. Calculate the equilibrium FX using cointegration with two or more
# macroeconomic variables
##############################################################################

# Macroeconomic variables that are influenced by both Macroeconomic policy and
# Macroeconomic conditions. The FX evolution is influenced by the central 
# banks through indicators that influences the supply and "cost" of money, 
# which is reflected by the level of interest rates. While, Macroeconomic 
# conditions like industrial production capacity utilization also influence 
# the FX evolution.
 
# Vector Autoregression (VAR)/Vector Error Correction model (VECM) will be
# used to calculate the long run equilibrum relation between FX and FEDRATE,
# As well, as FX evolution and CPI.

# Variables from Fred Database
"INDPRO"	
# Industrial Production Index, Index 2012=100, Monthly, Seasonally Adjusted
"JPNPROINDMISMEI"
# Production of Total Industry in Japan, Index 2010=100, Monthly, Seasonally Adjusted
"CPIAUCSL"
# US Consumer Price Index for All Urban Consumers: All Items,
# Index 1982-1984=100, Monthly, Seasonally Adjusted
"JPNCPIALLMINMEI"
# Consumer Price Index of All Items in Japan,
# Index 2010=100, Monthly, Not Seasonally Adjusted
"FEDFUNDS"
# Effective Federal Funds Rate, Percent, Monthly, Not Seasonally Adjusted
"INTDSRJPM193N"
# Interest Rates, Discount Rate for Japan, Percent per Annum,
# Monthly, Not Seasonally Adjusted
"EXJPUS"
# Japan / U.S. Foreign Exchange Rate, Japanese Yen to One U.S. Dollar,
# Monthly, Not Seasonally Adjusted

# The VAR class assumes that the passed time series are stationary. 
# Non-stationary or trending data can often be transformed to be stationary
# by first-differencing.

ldf = df[['fx', 'ip_US', 'cpi_US', 'fed_rate']]

df2 = np.log(ldf).diff().dropna()


# Make a VAR model
model = VAR(df2)


# Have the model select a lag order based on a standard information criterion
#
model.select_order(15)

# model estimation, use the fit method with the desired lag order of 15. 
results = model.fit(maxlags=15, ic='aic')
results.summary()
print(results.resid.plot())


# Impulse responses are of interest, as they are 
# the estimated responses to a unit impulse in one of the variables.
# perform an impulse response analysis by calling 
# the irf function on a VARResults object: 
irf = results.irf()
# visualize using the plot function, in non-orthogonalized form.
# The cumulative effects  can be plotted with the long run effects
print(irf.plot_cum_effects())


# Comments

"""Question 4\
The individual coefficients from the error-correction model are hard to\
 interpret in the case of vector-auto-regressive model. Consequently, \
 the dynamic properties of the model are analyzed by examining the impulse \
 response functions. The impulse response functions trace the dynamic \
 responses to the effect of shock in one variable upon itself and on all other\
 variables i.e. it is a tool that portrays the expected path over time of the \
 variable to shocks in the innovations. These impulse response functions were
 plotted and show that one standard deviation shock applied to exchange \
 produces negative effects on the FX evolution over time.
A one standard deviation shock to US industrial production index has a no \
perceptible effect on JPY/US FX in the short, but gradually increases in the \
medium to long term and eventually corrects the increase with a decrease in \
the long run. Therefore, the relationship is mean reverting in the long run. \
A one standard deviation shock to CPI has a negative effect on FX evolution in \
the short run, and is mean reverting in the medium term and will increase FX \
in the long run. While, one standard deviation shock in the FEDRATE will have \
a negative effect on the JPY/US FX in the short to medium term, with a mean \
reverting property in the long run. The main implications of the findings are \
that the JPY/US exchange rate is decreasing over time, which means the JPY \
likely undervalued at the moment and it is advisable to invest in the JPY \
short to medium term as there may be opportunities for arbitrage. \
Additionally, the US Industrial production will likely improve in the near \
term, especially with the current administration pushing for protectionist \
policies. This will see an increase in the JPY/US FX as the increase in \
domestic production will strengthen the US dollar against major currencies.\
 However, the increased access to exchange rate for production could have \
 significant impact on industrial production in the long run. This, therefore,\
 suggests that more foreign exchange should be made available to reduce the \
 gap between the supply and demand for exchange rate thereby enhancing the \
 value of the domestic currency. 
