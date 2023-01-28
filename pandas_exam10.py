import pandas as pd

data1 = {'kor':90, 'eng':70, 'mat':80}
data2 = {'kor':90, 'eng':70, 'mat':80}
data3 = {'kor':90, 'eng':70, 'mat':80}

data = pd.DataFrame()
data = data.append(data1, ignore_index = True)
data = data.append(data2, ignore_index = True)
data = data.append(data3, ignore_index = True)

# 각 필드 값들을 더하여 새로 작성한 필드에 저장
# 이미 있던 필드의 경우 data['kor'] 대신에 data.kor로 접근 가능

data['total'] = data.kor + data.eng + data.mat
data['avg'] = data.total/3

print(data)