import pandas as pd
data = {
    'name' : ['홍길동', '임꺽정', '장길산', '홍경래'],
    'kor' : [90, 80, 70, 70],
    'eng' : [99, 98, 97, 46],
    'mat' : [90, 70, 70, 60]
}
df = pd.DataFrame(data)
print(df.head())            # 앞의 다섯 명에 대한 데이터만 나옴

print( " 지정한 열만 출력 ")
print(df[ ' name '])
print(df[ ' kor '])
print(df.columns)           # 컬럼 이름만 출력

#iloc 함수 : 배열에서의 위치 값으로 데이터를 접근할 수 있음
print("iloc 함수 사용 ---------------")
print(df.iloc[0,0])         # 0, 0 번에 해당하는 데이터 출력
print(df.iloc[3,2])         # 3번째 행의 2번째 열
print(df.iloc[2:4,2])
print(df.iloc[2:4, 2:4])

print("loc 함수 사용 ---------------")
#loc 함수는 필드명으로 데이터를 출력할 수 있음
print(df.loc[0, 'name'])    # 0번째 행의 name 필드값 출력
print(df.loc[3, 'eng'])     # 0번째 행의 eng 필드값 출력
print(df.loc[:, 'name':'eng'])