import pandas as pd

# 인덱스가 없을 경우 값이 NaN으로 들어가서 연산이 되지 않음

data1 = {'kor':90, 'mat':80}
data2 = {'kor':90, 'eng':70}
data3 = {'kor':90, 'eng':70, 'mat':80}
series1 = pd.Series(data1)
series2 = pd.Series(data2)
series3 = pd.Series(data3)
result1 = series1 + series2 + series3
print(result1)