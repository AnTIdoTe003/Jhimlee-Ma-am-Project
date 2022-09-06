import pandas as pd
from datetime import datetime

df = pd.read_csv('app_protoype - Sheet1.csv')
amount = int(input("Enter the amount of ammonia"))
now = datetime.now()

data = [{'Time': now.strftime("%H:%M:%S"), 'Measurement': amount}]
df = df.append(data, ignore_index=True)
df.to_csv('app_protoype - Sheet1.csv',index=False)
print(df)
