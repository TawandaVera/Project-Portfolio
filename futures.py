# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 00:30:26 2018

@author: TempAdmin1
"""

from __future__ import print_function
import matplotlib.pyplot as plt
import pandas as pd
import requests
start_year = 2017
end_year = 2018

def construct_futures_symbols(symbol, start_year=2017, end_year=2018):
    futures = []
    months = 'HMUZ'
for y in range(start_year, end_year+1):
    for m in months:
        futures.append("%s%s%s" % (symbol, m, y))
    print(futures)

def download_contract_from_quandl(contract, dl_dir):
    api_call = "http://www.quandl.com/api/v1/datasets/"
    api_call += "OFDP/FUTURE_%s.csv" % contract
    params = "?sort_order=asc"
    # Download the data from Quandl
    data = requests.get(full_url).text
# Store the data to disk
    fc = open('%s/%s.csv' % (dl_dir, contract), 'w')
    fc.write(data)
    fc.close()

def download_historical_contracts(
symbol, dl_dir, start_year=2017, end_year=2018):
    contracts = construct_futures_symbols(
            symbol, start_year, end_year)
    for c in contracts:
        print("Downloading contract: %s" % c)
        download_contract_from_quandl(c, dl_dir)
if __name__ == "__main__":
    symbol = 'ES'
    dl_dir = 'quandl/futures/ES'
    download_historical_contracts(symbol, dl_dir, start_year, end_year)
    es = pd.io.parsers.read_csv("%s/ESH2010.csv" % dl_dir, index_col="Date")
    es["Settle"].plot()
    plt.show()
    
# Make sure you’ve created t