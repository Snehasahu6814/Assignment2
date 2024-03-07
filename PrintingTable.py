"""Importing the pandas to create data"""
import pandas as pd
from tabulate import tabulate
days_of_week=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
print("\n Dictionary with  the day information")
day_dict = {}
for i, day in enumerate(days_of_week, start=1):
    day_dict[day] = {
        "Occurrences":i,
        "ShortForm":day[:3],
        "NameinLower":day.lower(),
        "NameinUpper":day.upper(),
        "Length":len(day)
        }
headers = ["Name of the Day","Occurrences","ShortForm","NameinLower","NameinUpper","Length"]
Tabular = []
for day, data in day_dict .items():
    weekday = [day]
    for i in headers[1:]:
        weekday.append(data[i])
    Tabular.append(weekday)
print(tabulate(Tabular, headers=headers,tablefmt='grid'))
df = pd.DataFrame.from_dict(day_dict,orient='index',columns=["Occurrences",
"ShortForm","NameinLower","NameinUpper","Length"])
df.to_excel("days_tabular_dict.xlsx",
index_label="Name of the Day")
