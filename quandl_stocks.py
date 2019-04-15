# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 14:14:18 2018

@author: TempAdmin1
"""
import quandl
import datetime
 

quandl.ApiConfig.api_key = 'MgUeDFrhs9JjaA4gKzEx'
 
def quandl_stocks(symbol, start_date= datetime.date.today()-datetime.timedelta(30), end_date=None):
    
    #symbol is a string representing a stock symbol, e.g. 'AAPL'
 
    '''start_date and end_date are tuples of integers representing the year, month,
    and day end_date defaults to the current date when None'''
 
    query_list = ['WIKI' + '/' + symbol + '.' + str(k) for k in range(1, 13)]
 
    start_date = start_date
 
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
        
        symbol = "appl"
        symbol_data = quandl_stocks('appl', start_date, end_date)
        print(symbol_data)