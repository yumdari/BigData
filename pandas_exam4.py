import pandas as pd
#파이썬은 언어의 구조상 3차원 배열이라는 개념이 없음
#3차원 배열을 많듬 - list of list of list [[[],[],[]]]

array = [[[1,2,3], [4,5,6]],
        [[7,8,9], [10,11,12]],
        [[13,14,15], [16,17,18]]]

array = pd.Panel(array)
print("타입 : ", type(array))
print(array)