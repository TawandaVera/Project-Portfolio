# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 15:56:09 2018

@author: Tawanda Vera
"""
###############################################################################

# Assignment 1
"""
Question1: In this assignment, we want to evaluate how Disney performed as 
an investment between October 2008 and September 2013 and how risky it is. 
To do that we need to regresses monthly raw returns on Disney against returns
 on the S&P 500 over that period.  
1. Download the historical data of Disney and S&P 500 over that period. 
2. Calculate the returns of Disney and the S&P 500 index.  
3. Using Python, plot the monthly returns on Disney against returns on the 
S&P 500 index from October 2008 to September 2013.  
4. Find the regression line for Disney return on S&P 500 index.  
5. What is the slope of the regression line? 
What is the meaning of this value? 
6. What is the Intercept of the Regression? 
What is the meaning of this value? 
Does Disney’s stock perform better or worse than expected? Why? 
Find the annualized excess return?  
7. What is the R squared of the regression? 
What is the significance of this value?  
8. What is Standard Error of Beta Estimate?
What is the significance of this value
"""
###############################################################################
import quandl    # pip install quandl
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import matplotlib.pyplot as plt

from scipy import stats

# Download the historical data of Disney and S&P 500 over that period. 

DIS = quandl.get("EOD/DIS", authtoken="nPxEmsTFZUATpB25wB_-", 
                 start_date="2008-10-01", end_date="2013-10-01")['Close']

# Download the historical data of S&P500 Data
sdt = dt.datetime(2008, 10, 1)
edt = dt.datetime(2013, 10, 1)
SP500 = web.DataReader("SP500", "fred", sdt, edt)

# Calculate the monthly returns of Disney and the S&P 500 index.  
data = pd.DataFrame()
data['x'] = DIS
data ['y'] = SP500
month_ret = data.pct_change(21)
ret = month_ret.dropna()

# Plot the relationship
x = np.array(ret.x)
y = np.array(ret.y)
plt.scatter(x, y);
plt.title("Scatterplot for DISNEY vs SP500")

# Calculate the regression line
beta, alpha, r_value, p_value, std_err =stats.linregress(x, y)

print('beta=',beta,'alpha=',alpha)

print('r_value', r_value, 'p_value', p_value)

print('std_err', std_err)

##############################################################################
#Comment
"""
The DISNEY Beta of 0.565 incorporates an asset’s total risk, which includes 
the market risk and firm specific risk. Thus, the Beta of DISNEY measures
 the degree of DISNEY stock’s market-risk. This market-risk is systemic, 
 undiversifiable risk. Since, Beta measures an asset’s price volatility; 
 the DISNEY Beta of 1.12 indicates that the DISNEY’s stock price will be 43.5%
less volatile than the market.
The DISNEY Alpha of 0.0134% indicates an underperformance of the stock to 
its benchmark by 0.013% of actual returns from its expected return as 
forecasted using that DISNEY’s Beta. 
The regression results show that both the Beta (p-value <0.0001) and 
Alpha (P-value <0.0001) were statically significant at the 99% level (strong).
Therefore, there is statistical confidence at the 99% confidence interval;
to support that DISNEY returns are affected by the S&P 500 index (market).
 
Furthermore, DISNEY’s returns have a strong positive relationship (r = 0.8400)
 with the market returns. If market return increases, DISNEY’s returns 
 increases and vice versa. As such, DISNEY tracks the S&P index. While, the 
 R2 of the regression is 0.8405. The tight scatter about the regression line 
 illustrates this. As such, 84.1% of variability of DISNEY stock returns
 between Oct 2008 to September 2013 that is explained by variability in 
 the market (S&P500). 
 R-square tells us what fraction of a firm’s volatility is attributable 
 to market movements. While, 1 - R2 = 0.15 so that 15% of DISNEY's return, 
 which is not explained by the market is the percentage of diversifiable risk. 

For each month, t, our estimate of the residual, et, which is the deviation of
 DISNEY’s excess return from the prediction of the SCL, equals 
 Deviation = Actual − Predicted return.
 The standard error of the regression (SD of e(t)) is 0.0104. 
 This is the typical distance of a dot from the regression line. 
"""
############################################################################## 