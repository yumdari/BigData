import pandas as pd

data = {'one':'일', 'two':'이', 'three':'삼', 'four':'사', 'five':'오'}
series = pd.Series(data)
print(series)
print(series['one'])
print(series[0:3])
print(series['one':'three'])
print(series['two':])