# -*- coding: utf-8 -*-
"""
Created on Mon May 21 20:37:39 2018

@author: Tawanda Vera
"""
"""
In this Mini Project, we will analyze the difference frictionless trading and 
trading in real life. Most of the data published in popular media on the 
return profiles of trading systems consider frictionless trading – an ideal 
universe where there is no slippage, no commissions, trading costs and gaps.
""" 
import pandas as pd
import numpy as np
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import statsmodels.api as sm
import seaborn as sns
import datetime


sns.set(style='darkgrid', context='talk', palette='Dark2')
my_year_month_fmt = mdates.DateFormatter('%m/%y')

# Download the data for the last 15 years for DJIA and DJTA
sdt = datetime.datetime.now() - datetime.timedelta(15*365)
edt = datetime.datetime.now()
djia = web.DataReader("DJIA", "fred", sdt, edt)

djia.tail()


# Construct a simple trading system that goes long when DJIA closes above its 
# 20 Day Exponential Moving Average of Close Prices (20 DEMA) and closes in 
# position and goes short when prices close below the 20 DEMA.

data = djia

# Create the indicator (20 day SMA)
data['20DEMA'] = data.DJIA.ewm(span=20, adjust=True).mean()

# Generate signals based on trading logic
data['Signal'] = data.DJIA - data['20DEMA']  

# Generate positions held
data['Position'] = data['Signal'] * 20

# Start with 10,000$ and always invest 1,000$ in every single trade

# Calculate performance metrics
data['Return'] = data.DJIA.diff() * data['Position']* 10000

print(data['Return'][-1])

# Plot equity curve
data.plot(subplots=True)
"""Chart 1: There are price data available for each day (There are no missing 
data for very large periods of time).
# Chart 2: Clear that the 20 day SMA smooths out the data and that we don’t 
have any gaps or abnormal spikes.
# Chart 3: In this chart, we have to multiply the signal value by a multiple 
to generate the Position. (Not the best position sizing technique by a long 
shot but this is a toy strategy.)
# Chart 4: represents the number of lots we are holding at any given point in time.
# Chart 5: Daily returns
"""
#Data Validation
data = data.apply(lambda series: series.loc[:series.last_valid_index()].ffill())

data.plot(subplots=True)

# Exit from Trades are made by stop Market orders at the price of the 20 DEMA. 
#
Exit = 0   # Deviations at zero is used as the threshold
data['Buy'] = np.where(data['Signal'] > Exit, 1000, 0)   # long
data['Exit'] = np.where(data['Signal'] == Exit, -1000, 0) # stop market order
data['Sell'] = np.where(data['Signal'] < Exit, -1000, 0) # short
data['Strategy'] = data['Buy'] + data['Exit'] + data['Sell']

data['Buy'].sum()
data['Sell'].sum()
data['Exit'].sum()

# Case 1: Consider frictionless trading 
"""Consider that you are able to enter into trades exactly at the close price 
of the day on which the trend starts. 
Consider ideal fills exactly on entry and stop loss exits on the 20DEMA. 
No Slippage or brokerage or commissions to be taken into account – consider 
you are trading for free!
"""
# Generate positions held
data['Fric_trad'] = data.DJIA.diff() * data['Strategy'] 
 
# Plot the return profile of such a trading system.

data['Fric_trad'].cumsum().plot(subplots=True)

# Case 2: Consider Real Trading
"""Gaps: Enter trades at Market Open the next day through Stop Limit Orders – 
this is the way traders have to do things in real life (hence exposed to 
opening gaps)
Brokerage & Commissions: Check the Interactive brokers site and decide on a 
Brokerage ratio to use for your trades
Slippage: Use the model generated in Unit 5 Assignment to consider slippages 
on each and every trade. 
"""

# Slippage
bid = data[['DJIA', 'Buy']].to_dict('split')
ask = data[['20DEMA', 'Sell']].to_dict('split')

def calc_slippage(book, volume, side):
    """Calculate slippage given a market order and order book snapshot.
    Args:
        book: A dict representing a snapshot of an order book.
            Contains two dicts for each side of the order book.
            Each dict representing order book side has a price level as
            key and volume at price level as value.
                Example: book = {
                                'bid': {100: 5, 95: 2},
                                'ask': {120: 3, 115: 4}
                                }
            This book has two bid price levels: 100 with volume of 5 and
            95 with volume of 2; Also two ask levels: 120 with volume 3 and
            115 with volume 4.
            Volume: Volume of a market order that is used to calculate 
            corresponding slippage.
            Side: Side of a market order; either 'bid' or 'ask'.
    Returns:
    A dict with slippage cost and percentage, and some other intermediate 
    data that was used in the calculation:
    slippage_cost - absolute value of slippage cost for a given market order
    slippage_frac - what fraction of the quote total price does the slippage 
    cost constitute
    quote_price - either lowest ask or highest bid, depending on the selected 
    side of the market
    quote_total - total cost of market order when entire volume is filled at 
    quote price
    actual_total - total cost of market order when order is filled using 
    available order book liquidity
    """
    price_levels = get_price_levels(book, side)
        
    # Assume the high value is the maximum in 'ask'
    High =  max(book['ask'])
    
    # Assume the low value is the minimum in 'bid'
    Low = min(book['bid'])  
    
    # Assume the first ask price in book is the open
    Open = list(book['ask'])[0] 
    
    # Assume the last ask price in book is the close
    Close = list(book['ask'])[-1]
    
    # identical to get_quote_price, just don't need to recalc price_levels twice
    quote_price = price_levels[0][0]
    quote_total = volume * quote_price
    actual_total = 0
    volume_to_fill = volume
    for price, level_volume in price_levels:
        if volume_to_fill - level_volume <= 0:
            actual_total += volume_to_fill * price
            break
        volume_to_fill -= level_volume
        actual_total += level_volume * price
        
    # Bid-Ask Spread
    c0 = Close - Open
    c1 = High - Low
    bid_ask_spread = c0 + c1
    slippage_cost = abs(quote_total - actual_total + bid_ask_spread)
    
    slippage_frac = slippage_cost / quote_total
    slippage = {'slippage_cost': slippage_cost,
                'slippage_frac': slippage_frac,
                'quote_price': quote_price,
                'quote_total': quote_total,
                'actual_total': actual_total,
                'high' : High,
                'low' : Low,
                'open': Open,
                'close': Close
                }
    return slippage

def get_quote_price(book, side):
    """Useful if need just the current quote price.
    Args:
        book: Same dict as in book arg to calc_slipage().
        side: Either 'bid' or 'ask'.
    Returns:
        The current quote price at the chosen side of the market, i.e.
        highest bid(Best Bid) or lowest ask(Best Ask).
    """
    price_levels = get_price_levels(book, side)
    quote_price = price_levels[0][0]
    return quote_price


def get_price_levels(book, side):
    """Returns price levels according to their fill order.
    Args:
        book: Same dict as in book arg to calc_slipage().
        side: Either 'bid' or 'ask'.
    Returns:
        A list of price levels from a chosen side of the order book sorted in the following order:
            Fill order for bid side: highest price -> lowest price
            Fill order for ask side: lowest price -> highest price
        Each price level item in the list is a tuple: (price, volume).
        * Sorting tuples without specifying a key works fine here since tuples are compared
          position by position, and the first element of price level tuple is the price.
    """
    if side == 'bid':
        levels = book['bid']
        price_levels = sorted(levels.items(), reverse=True)
    elif side == 'ask':
        levels = book['ask']
        price_levels = sorted(levels.items())
    return price_levels

  
if __name__=='__main__':
    
    slippage = calc_slippage(bid, 15, 'bid')
    print(slippage)
    
    






# Compare the Risk-Return Profiles of both the systems and draw inferences
