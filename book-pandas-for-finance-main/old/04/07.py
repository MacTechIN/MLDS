from pandas import DataFrame

data = [
    ["037730", "3R", 1510],
    ["036360", "3SOFT", 1790],
    ["005760", "ACTS", 1185],
]
columns = ["종목코드", "종목명", "현재가"]
df = DataFrame(data=data, columns=columns)

print(df.loc[0]["종목코드"])            # 로우 -> 컬럼
print(df["종목코드"][0])                # 컬럼 -> 로우
