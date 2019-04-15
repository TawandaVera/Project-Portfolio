# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 00:30:26 2018

@author: TempAdmin1
"""
#!/usr/bin/python
# -*- coding: utf-8 -*-
# quandl_data.py
from __future__ import print_function
import matplotlib.pyplot as plt
import pandas as pd
import requests
start_year = 1917
end_year = 2018

def construct_futures_symbols(symbol, start_year=(2017,2,1), end_year=(2017, 12, 2)):
    futures = []
    futures.append("%s%s%s" % (symbol,start_year, end_year))
    print(futures)

def download_contract_from_quandl(contract, dl_dir):
    api_call = "http://www.quandl.com/api/v1/datasets/"
    api_call += "BCB/UDJIAD1_%s.csv" % contract
    params = "?sort_order=asc"
    # Download the data from Quandl
    data = requests.get(full_url).text
# Store the data to disk
    fc = open('%s/%s.csv' % (dl_dir, contract), 'w')
    fc.write(data)
    fc.close()


