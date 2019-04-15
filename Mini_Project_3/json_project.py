# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 11:49:18 2018

@author: Tawanda Vera
"""


import pandas as pd
from pandas.io.json import json_normalize

# Load JSON using Pandas JSON class
df = pd.read_json('nutrients.json', orient='column', typ='series',
                  dtype=True, convert_axes=True, numpy=False,
                  precise_float=True, encoding='utf-8', lines=True)

print(df[0].keys())

# To get the list of columns in data series

# the Database length is 8789, json_normalize create 17 columns x 8789 rows

df_normalized = json_normalize(df, 'nutrients',
                               ['group', 'manufacturer',
                                ['meta', 'ndb_no'],
                                ['name', 'long']])

print(df_normalized[:10])

# Converting a list of food dicts to an info DataFrame

info_keys = ['meta.ndb_no', 'name.long', 'group', 'manufacturer',
             'name', 'value']

info = pd.DataFrame(df_normalized, columns=info_keys)

print(info.keys())

print(info[:10])

# Foor clarity the columns of the DataFrame objects are renamed

col_mapping = {'name.long': 'food', 'group': 'fgroup',
               'meta.ndb_no': 'id', 'name': 'nutrient',
               'value': 'nutrient.value'}

# Present the USDA data as renamed dataframe
usda_data = info.rename(columns=col_mapping, copy=False)

# use the info to get the range index

print(usda_data.info())


print(usda_data.iloc[30000])


# We are now able to make a plot of median values
# by food group and nutrient type. However, the data did not have nutrient
# groups so the table presented is for nutrient group by food groups


n_med = usda_data.groupby(['nutrient',
                           'fgroup'])['nutrient.value'].quantile(0.5)

print(n_med)

# Plot the median Zinc Values
n_med['Zinc, Zn'].sort_values().plot(kind='barh')

print("----Median zinc values by nutrient group-----")

