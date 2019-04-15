# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 15:56:09 2018

@author: Tawanda Vera
"""
"""
In this Mini Project, we will analyze the S&P500 Adjusted Close Price for the
 last 10 years.
 Write a Python program to download the historical data of S&P500 over that 
 period.
Show in a chart how the price of S&P 500 varied over that period. 
Plot Daily returns of the Index and identify periods of 5 worst historical
 monthly draw-downs.
The Calmar Ratio is a drawdown related measure which equal to the compounded 
annual growth rate divided by the maximum drawdown.
"""
##############################################################################

import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# Download the historical data of S&P500 Data
sdt = dt.datetime(2008, 4, 29)
edt = dt.datetime(2018, 4, 29)
data = web.DataReader("SP500", "fred", sdt, edt)


# Let's see a historical view of the closing price
data.plot(legend=True,figsize=(15,8))


#daily returns
daily_return = data.pct_change()
daily_return.rename(columns={'Open': 'price'}, inplace=True)
daily_return.plot(legend=True, subplots=False,figsize=(12,6))
fig=sns.distplot(daily_return.dropna(),bins=100,color='green')
fig.set(xlabel='Return Occurances',ylabel='Return Percentage',
        title='Distribution of Daily Returns',)

# Define a trailing 252 trading day window
window = 252
# Calculate the max drawdown in the past window days for each day 
rolling_max = data.rolling(window, min_periods=1).max()
daily_drawdown = data/rolling_max - 1.0
# Calculate the minimum (negative) daily drawdown
max_daily_drawdown = daily_drawdown.rolling(window, min_periods=1).min()
# Plot the results
daily_drawdown.plot(legend=True,figsize=(15,8))
max_daily_drawdown.plot(legend=True,figsize=(15,8))
# Show the plot
plt.show()


daily_return.head()
sp500 = daily_return.cumsum() + 1
sp500.plot()

# Annualised Return
 
days = (sp500.index[-1] - sp500.index[0]).days
cagr = ((((sp500[-1]) / sp500[1])) ** (365.0/days)) - 1
print ('CAGR =',str(round(cagr,4)*100)+"%")

# Performance
def create_drawdowns(sp500):
    """
    Calculate the largest peak-to-trough drawdown of the PnL curve
    as well as the duration of the drawdown. Requires that the 
    pnl_returns is a pandas Series.

    Parameters:
    pnl - A pandas Series representing period percentage returns.

    Returns:
    drawdown, duration - Highest peak-to-trough drawdown and duration.
    """

    # Calculate the cumulative returns curve 
    # and set up the High Water Mark
    # Then create the drawdown and duration series
    hwm = [0]
    eq_idx = sp500.index
    drawdown = pd.Series(index = eq_idx)
    duration = pd.Series(index = eq_idx)

    # Loop over the index range
    for t in range(1, len(eq_idx)):
        cur_hwm = max(hwm[t-1], sp500[t])
        hwm.append(cur_hwm)
        drawdown[t]= hwm[t] - sp500[t]
        duration[t]= 0 if drawdown[t] == 0 else duration[t-1] + 1
    return drawdown.max(), duration.max()


drawdown = create_drawdowns(sp500)
print(drawdown)

# ** Worst Drawdown was 73% and lasted 893 Days**

#Calmar Ratio is CAGR / MAXX
cr = cagr/drawdown.max()
print(cr)

#
strat = pd.DataFrame([sp500, daily_return]).transpose()
strat = strat.dropna()
strat.head()
data['SMA'] = data['price'].rolling(30).mean()
data.tail()
data.plot(title='SPY | 30 SMA',figsize=(10, 6))

#vector the signal
data['position'] = np.where(data['price'] > data['SMA'], 1, -1) 
data.dropna(inplace=True) 
data['position'].plot(ylim=[-1.1, 1.1], title='Market Positioning')
data['returns'] = np.log(data['price'] / data['price'].shift(1)) 

# plots returns in hist
data['returns'].hist(bins=35) 

# returns when strategy is true
data['strategy'] = data['position'].shift(1) * data['returns'] 

# sums for both stock and strategy
data[['returns', 'strategy']].sum() 

data[['returns', 'strategy']].cumsum().apply(np.exp).plot(figsize=(10, 6))
st = data['strategy'].cumsum().apply(np.exp)
st.head()

ABMR = np.sum(rets[rets < 0])
print(ABMR)   
          
TSMR = -0.532332 * 100  # sum of strategy *100
print(TSMR)

P2Gratio = TSMR / ABMR
print(P2Gratio)

# LAKE RATIO GRAPH

lr = pd.DataFrame(st)
lr = lr.dropna()
lr.head()
lr.plot(figsize=(10, 6))

# Define a trailing 252 trading day window
window = 252

rolling_max = lr.rolling(window, min_periods=1).max()
lr.plot(figsize=(10, 6))
rolling_max.plot(figsize=(10, 6))
plt.show()

lr["HWM"] = rolling_max
lr["Water"] = lr["HWM"] - lr["strategy"]
lr["Lake"] = lr["strategy"] - lr["Water"]
lr.head()

lr.plot(figsize=(10, 6))
#rolling_max.plot(figsize=(10, 6))
plt.show()

lr["Lake"].describe()
lr["Water"].sum()
lr["strategy"].sum()
Lake_Ratio = lr["Water"].sum() - lr["strategy"].sum()
print(Lake_Ratio)

############################################################################