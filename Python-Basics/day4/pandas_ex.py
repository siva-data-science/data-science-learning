import pandas as pd

data = {
    "name": ["siva", "mahesh", "narendra"],
    "marks" : [85,75,95]

}
# print(data)
df = pd.DataFrame(data)
print(df)


#average

print(df["marks"].mean())


#firstrow

print(df.head())