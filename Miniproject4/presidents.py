# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 05:56:42 2018

@author: Tawanda Vera
"""

import pandas as pd
import matplotlib.pyplot as plt
#############################################################################
url = 'http://en.wikipedia.org/wiki/List_of_Presidents_of_the_United_States'

wk = pd.read_html(url, index_col=1, attrs={"class": "wikitable"})

df = pd.DataFrame(wk[0].dropna(axis=0, thresh=4))

df.to_csv('uspresidents.csv')


##############################################################################
def uspresidentEffect():
    '''
    to see the effect of US president & Party on stock market index.
    There are lots of factors which affect the price together.
    Thus we cannot make conclusion based this single factor.
    :return:
    '''
    # Only has data since 1950 and 1985
    # df = getPandasYahooData(['^GSPC','^DJI'],date(1920,1,1),date(2018,2,1))

    ind = pd.read_csv('IndexFile.csv')
    ind['SPCreturns'] = ind['SPC'] / ind['SPC'].shift(1)
    ind['DJIreturns'] = ind['DJI'] / ind['DJI'].shift(1)
    indgroupParty = ind[['President', 'SPCreturns',
                         'DJIreturns']].groupby('President').sum()
    indgroupParty.plot(kind='barh')
    plt.show()

    indgroupParty = ind[['Party', 'SPCreturns',
                         'DJIreturns']].groupby('Party').sum()
    indgroupParty.plot(kind='barh')
    plt.show()

    indgroupParty = ind[['Party', 'SPCreturns',
                         'DJIreturns']].groupby('Party')
    print(indgroupParty.describe())


if __name__ == '__main__':
    uspresidentEffect()