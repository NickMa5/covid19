import requests
import json
import urllib3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

state = input("Enter state initials: ")

if str.isalpha(state) == False:
    print("No numbers allowed.")
elif len(state) != 2:
    print("Initials can only be 2 letters.")
elif len(state) == 2:
    print(state)
# api source for additional info, https://covidtracking.com/api
# https://covidtracking.com/api/v1/states/
url = "https://covidtracking.com/api/v1/states/" + state + "/daily.json"

data = requests.get(url).json()

#print("positive " + str(data['positive']))

def get_data(key):
    empty_list = []
    for item in data:
        total = item.get(key)
        empty_list.append(total)
    return empty_list

dates = get_data('date')
total_positive = get_data('positive')
diff = [i-j for i, j in zip(total_positive[:-1], total_positive[1:])]+[0]
df = pd.DataFrame(list(zip(dates, total_positive, diff)), columns=['date', 'positive', 'diff'])
df['date'] = df['date'].astype('str')
df['date'] = pd.to_datetime(df['date'], yearfirst=True, format="%Y/%m/%d").dt.date
print(dates)
print(total_positive)
print(diff)
print(df)
print(df.info())
fig, ax = plt.subplots()
#fig.set_size_inches(8, 15)
plt.xticks(rotation=70)
sns.barplot(data=df, x="date", y="diff")
plt.show()