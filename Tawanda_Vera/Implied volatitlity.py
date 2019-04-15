# -*- coding: utf-8 -*-

Created on Tue Oct  3 00:45:54 2017

@author: Code adopted from Nicolas Christou

#Inputs:
S <- 34                 # Yahoo Current Stock Price
K <- 34                   # Exercise Price
r <- 0.001               # Risk Free Rate
T <- 1                       # Time to Expiry
call_put <- 2.7240             # Call Option Price

def find_vol(target_value, call_put, S, K, T, r):
    MAX_ITERATIONS = 100
    PRECISION = 1.0e-8
    sigma = 0.1
    for i in xrange(0, MAX_ITERATIONS):
        price = bs_price(call_put, S, K, T, r, sigma)
        vega = bs_vega(call_put, S, K, T, r, sigma)
        price = price
        diff = target_value - price  # our root
        print i, sigma, diff
        if (abs(diff) < PRECISION):
            return sigma
        sigma = sigma + diff/vega # f(x) / f'(x)

