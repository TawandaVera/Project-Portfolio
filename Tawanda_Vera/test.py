# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 20:49:15 2017

@author: TempAdmin1
"""
import plotly as py
import cufflinks as cf

import pandas as pd

cf.set_config_file(offline=False, world_readable=True, theme='pearl')

df=cf.datagen.lines(4)

df.iplot(subplots=True, shape=(4,1), shared_xaxes=True, fill=True, filename='cufflinks/simple-subplots')