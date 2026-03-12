import pandas as pd

data = {
    "Student" : ['siva','kumar','reddy'],
    "Marks" : [85,75,95]
}

df = pd.DataFrame(data)

print(df['Marks'].mean())