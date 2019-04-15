# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 05:16:20 2017

@author: TempAdmin1
"""
from scipy import stats

import math

def norm.pdf(x):
    exp(-x**2/2)/sqrt(2*pi)

n = stats.norm.cdf
N = stats.norm.pdf

def bs_price(cp_flag,S,K,T,r,v,q=0.0):
    d1 = (log(S/K)+(r+v*v/2.)*T)/(v*sqrt(T))
    d2 = d1-v*sqrt(T)
    if cp_flag == 'c':
        price = S*exp(-q*T)*N(d1)-K*exp(-r*T)*N(d2)
    else:
        price = K*exp(-r*T)*N(-d2)-S*exp(-q*T)*N(-d1)
    return price

def bs_vega(cp_flag,S,K,T,r,v,q=0.0):
    d1 = (log(S/K)+(r+v*v/2.)*T)/(v*sqrt(T))
    return S * sqrt(T)*n(d1)


V_market = 17.5
K = 585
T = (datetime.date(2014,10,18) - datetime.date(2014,9,8)).days / 365.
S = 586.08
r = 0.0002
cp = 'c' # call option

implied_vol = find_vol(V_market, cp, S, K, T, r)

print('Implied vol: %.2f%%' % (implied_vol * 100))

print('Market price = %.2f' % V_market)
print('Model price = %.2f' % bs_price(cp, S, K, T, r, implied_vol))