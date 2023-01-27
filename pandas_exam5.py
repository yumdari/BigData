import pandas as pd
data = [10, 20, 30, 40, 50, 60]
s = pd.Series(data)
print(s[0])     # 0번째 해당 데이터 출력
s[1] = 200      # 1번째 데이터 200으로 수정
print(s)
print(s[:5])    # 5번째 데이터부터 마지막까지 출력
print(s[2:5])   # 2번 데이터부터 4번 데이터까지 출력
print(s[3:])    # 3번 이후로 출력