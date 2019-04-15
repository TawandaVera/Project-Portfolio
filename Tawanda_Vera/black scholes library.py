# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 03:25:10 2017

@author: TempAdmin1
"""

from scipy import stats

import math



def black_scholes (cp, s, k, t, v, rf, div):

        """ Price an option using the Black-Scholes model.

        s: initial stock price

        k: strike price

        t: expiration time

        v: volatility

        rf: risk-free rate

        div: dividend

        cp: +1/-1 for call/put

        """



        d1 = (math.log(s/k)+(rf-div+0.5*math.pow(v,2))*t)/(v*math.sqrt(t))

        d2 = d1 - v*math.sqrt(t)

        
        optprice = (cp*s*math.exp(-div*t)*stats.norm.cdf(cp*d1)) - (cp*k*math.exp(-rf*t)*stats.norm.cdf(cp*d2))

        return optprice




#code from Paper by Sanjiv R. Das and Brian Granger

#web address: http://algo.scu.edu/~sanjivdas/cython.pdf