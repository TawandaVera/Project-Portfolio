# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 05:56:42 2018

@author: Tawanda Vera
"""

import pandas as pd

#############################################################################
url = 'http://en.wikipedia.org/wiki/List_of_Presidents_of_the_United_States'

wk = pd.read_html(url, index_col=1, attrs={"class": "wikitable"})

df = pd.DataFrame(wk[0].dropna(axis=0, thresh=4))

df.to_csv('uspresidents.csv')

##############################################################################


ind = pd.DataFrame()

ind = pd.read_csv('IndexFile.csv')
ind['SPCreturns'] = ind['SPC'] / ind['SPC'].shift(1)
ind['DJIreturns'] = ind['DJI'] / ind['DJI'].shift(1)

print('n\----Group by Presidents-----\n')

indgroupParty = ind[['President', 'SPCreturns',
                         'DJIreturns']].groupby('President').sum()
#Plot
indgroupParty.plot(kind='barh')
plt.show()

print('n\----Group by Presidents Descriptives-----\n')

indgroupParty = ind[['President', 'SPCreturns',
                         'DJIreturns']].groupby('President')
#Descriptives
print(indgroupParty.describe())

####################  By Party    ###########################################

print('n\----Group by Party-----\n')

indgroupParty = ind[['Party', 'SPCreturns',
                         'DJIreturns']].groupby('Party').sum()

#plot
indgroupParty.plot(kind='barh')
plt.show()

print('n\----Group by Party Descriptives-----\n')

indgroupParty = ind[['Party', 'SPCreturns',
                         'DJIreturns']].groupby('Party')

#Descriptives
print(indgroupParty.describe())