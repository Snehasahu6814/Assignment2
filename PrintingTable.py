from collections import Counter
import pandas as pd
from tabulate import tabulate
days_of_week=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

    
    
print("\n Dictionary with  the day information") 
day_dict = {}
for i, day in enumerate(days_of_week, start=1):
    day_dict[day] = {
        "Occurrences":i,
        "Short Form":day[:3],
        "Name in Lower":day.lower(),
        "Name in Upper":day.upper(),
        "Length":len(day)}

headers = ["Name of the Day", "Occurrences", "Short Form", "Name in Lower", "Name in Upper", "Length"]
 
 
Tabular = []
for day, data in day_dict .items():
    weekday = [day]
    for i in headers[1:]:
        weekday.append(data[i])
    Tabular.append(weekday)
print(tabulate(Tabular, headers=headers,tablefmt='grid'))

df = pd.DataFrame.from_dict(day_dict, orient='index', columns=["Occurrences", "Short Form", "Name in Lower", "Name in Upper", "Length"])
df.to_excel("days_tabular_dict.xlsx", index_label="Name of the Day")