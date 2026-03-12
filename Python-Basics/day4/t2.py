import pandas as pd


data = {
    "age": [25,55,27],
    "city": ["vijayawada","guntur","vizag"]
}

df = pd.DataFrame(data)

print(df.head())