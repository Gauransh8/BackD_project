import pandas as pd
df = pd.read_csv("C:/Users/Admin/Documents/G10/database1.csv")
A = (input("Enter the tier : "))
df.loc['tier'] = 'A'
df.to_csv("C:/Users/Admin/Documents/G10/database1.csv", index=False)
print(df)

