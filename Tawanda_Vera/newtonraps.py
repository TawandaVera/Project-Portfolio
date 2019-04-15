# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 04:35:39 2017

@author: TempAdmin1
"""
from scipy import stats

import math

def newtonRap(cp, price, s, k, t, rf):
    """ Price an option using the Black-Scholes model.

        s: initial stock price

        k: strike price

        t: expiration time

        v: volatility

        rf: risk-free rate

        div: dividend

        cp: +1/-1 for call/put"""
        
    v = sqrt(2*pi/t)*price/s
    print("initial volatility: ", v)
    for i in range(1, 100):
        d1 = (log(s/k)+(rf+0.5*pow(v,2))*t)/(v*sqrt(t))
        d2 = d1 - v*sqrt(t)
        vega = s*norm.pdf(d1)*sqrt(t)
        price0 = cp*s*norm.cdf(cp*d1) - cp*k*exp(-rf*t)*norm.cdf(cp*d2)
        v = v - (price0 - price)/vega
        print("price, vega, volatility\n",(price0, vega, v))
        if abs(price0 - price) < 1e-25 :
            break
        return v