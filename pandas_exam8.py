import pandas as pd

data1 = {'ko':90, 'eng':70, 'mat':80}
data2 = {'ko':90, 'eng':70, 'mat':80}
data3 = {'ko':90, 'eng':70, 'mat':80}
data4 = {'ko':90, 'eng':70, 'mat':80}
series1 = pd.Series(data1)
series2 = pd.Series(data2)
series3 = pd.Series(data3)
series4 = pd.Series(data4)

result1 = series1 + series2 + series3 + series4
result2 = result1/4

print("총점 ----------")
print(result1)
print("평균 ----------")
print(result2)
