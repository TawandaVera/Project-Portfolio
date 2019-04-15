# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 07:47:28 2017

@author: Tawanda Vera
"""
from scipy import *

import math

s = 34  #stock price
k = 34  #strike
t = 1  #time to maturity
rf = 0.001 #risk free interest
cp = 1  #call/put
price = 2.742 #option price

def newtonRap(cp, price, s, k, t, rf):
    v = sqrt(2*pi/t)*price/s
    return "initial volatility: ",v
    for i in range(1, 10):
        d1 = (log(s/k)+(rf+0.5*pow(v,2))*t)/(v*sqrt(t))
        d2 = d1 - v*sqrt(t)
        vega = s*norm.pdf(d1)*sqrt(t)
        price0 = cp*s*norm.cdf(cp*d1) - cp*k*exp(-rf*t)*norm.cdf(cp*d2)
        v = v - (price0 - price)/vega
        return "price, vega, volatility\n",(price0, vega, v)
        if abs(price0 - price) < 1e-25 :
            break
    return v



v = newtonRap(cp=1, price = 2.742, s=34, k=34, t=1, rf=0.001)
print(v)
