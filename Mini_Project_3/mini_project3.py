# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 14:46:59 2018

@author: Tawanda Vera
"""

import pandas as pd
from pandas.io.json import json_normalize

df = pd.read_json('nutrients.json', orient='column', typ='series',
                  dtype=True, convert_axes=True, numpy=False,
                  precise_float=True, encoding='utf-8', lines=True)

df_normalized = json_normalize(df, 'nutrients',
                               ['group', 'manufacturer',
                                ['meta', 'ndb_no'],
                                ['name', 'long']])

info_keys = ['meta.ndb_no', 'name.long', 'group', 'manufacturer',
             'name', 'value']

info = pd.DataFrame(df_normalized, columns=info_keys)

col_mapping = {'name.long': 'food', 'group': 'fgroup',
               'meta.ndb_no': 'id', 'name': 'nutrient',
               'value': 'nutrient.value'}

usda_data = info.rename(columns=col_mapping, copy=False)

n_med = usda_data.groupby(['nutrient',
                           'fgroup'])['nutrient.value'].quantile(0.5)

print(n_med)

n_med['Zinc, Zn'].sort_values().plot(kind='barh')

print("----Median zinc values by nutrient group-----")

