import pandas as pd

data = {
    'name' : ['홍길동', '임꺽정', '장길산', '홍경래'],
    'kor' : [90, 80, 70, 70],
    'eng' : [99, 98, 97, 46],
    'mat' : [90, 70, 70, 60]
}
df = pd.DataFrame(data)
print("타입 : ", type(df))
print(df)