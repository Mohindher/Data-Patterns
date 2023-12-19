# -*- coding: utf-8 -*-
"""
@author: mohindher.thirumalai
"""

import data_patterns
import pandas as pd

df = pd.DataFrame(columns=['Name', 'Grade', 'value1',
                           'Value2', 'Value3', 'Value4', 'value5'],
                  data=[['Alpha', 'A', 1000, 800, 0, 200, 200],
                        ['Beta', 'B', 4000, 0, 3200, 800, 800],
                        ['Gamma', 'A', 800, 0, 700, 100, 100],
                        ['Theta', 'B', 2500, 1800, 0, 700, 700],
                        ['Ceta', 'C', 2100, 0, 2200, 200, 200],
                        ['Sayian', 'C', 9000, 8800, 0, 200, 200],
                        ['SSai', 'A', 9000, 0, 8800, 200, 200],
                        ['SSay', 'A', 9000, 8800, 0, 200, 200],
                        ['Geeks', 'A', 9000, 0, 8800, 200, 200],
                        ['SsBlue', 'B', 9000, 0, 8800, 200, 19]])

df.set_index('Name', inplace=True)
miner = data_patterns.PatternMiner(df)

# finding the pattern in the dataframe
# name is optional
# other patterns which can be used  ‘>’, ‘<’, ‘<=’, ‘>=’, ‘!=’, ‘sum’
df_patterns = miner.find({'name': 'equal values',
                          'pattern': '=',
                          'parameters': {"min_confidence": 0.5,
                                         "min_support": 2,
                                         "decimal": 8}})

df_results = miner.analyze(df)
print(df_results)