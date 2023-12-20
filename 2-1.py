from pandas import DataFrame

# 방법 1
# data = {
#     "종가" : [15000,14000,13500],
#     "PER": [30.1, 23.1,11],
#     "PBR": [2,3,1],
# }
# index = ["네이버", "삼성전자", "카카오"]
#
# df = DataFrame(data=data, index=index)
# print(df)

# 방법 2 :
# data = [
#     [15000, 30.1, 2],
#     [14000, 23.1, 3],
#     [13500, 11, 1],
# ]
# index = ["네이버", "삼성전자", "카카오"]
# columns = ["종가", "PER", "PBR"]
#
# df = DataFrame(data=data, index=index, columns=columns)
# print(df)

# 방법 3
data = [
    {"종가" : 15000, "PER": 30.1, "PBR": 2},
    {"종가" : 14000, "PER": 23.1, "PBR": 3},
    {"종가" : 13500, "PER": 11, "PBR": 1},
]
index = ["네이버", "삼성전자", "카카오"]
df = DataFrame(data=data, index=index)
# print(df)
#
# print(df['종가'])
# print(df[['종가','PBR']])

# print(df.iloc[0])
# print(df.iloc[[0, 2]])
# print(df.loc["삼성전자"])
# print(df.loc[["삼성전자", "카카오"]])
#
# print(df.iloc[0:1]) # 슬라이싱
# print(df.loc["네이버":"삼성전자"]) # 슬라이싱

# 값가져오기
print(df.iloc[0,1])
print(df.loc["네이버","종가"])

# 영역 값 가져오기
print(df.iloc[[0,1],[0,1]])
print(df.loc[["네이버","카카오"],["종가","PBR"]])

