from collections import Counter
import pandas as pd
days_of_week=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
print(" list of tuples which has the two consequtive days grouped together")
for i in range(len(days_of_week)-1):
    
    # print(" list of tuples which has the two consequtive days grouped together")
    consecutive_days = [(days_of_week[i], days_of_week[i+1]) ]
    print(consecutive_days,end=" ")
    
    
print("\n Dictionary with  the day information") 
day_dict = {}
for i, day in enumerate(days_of_week, start=1):
    day_dict[day] = (i, day[:3], day.lower(), day.upper(), len(day))
print(day_dict)
   
 
 
df = pd.DataFrame.from_dict(day_dict, orient='index', columns=["Occurences", "Short Form", "Name in Lower", "Name in Upper", "Length"])
df.to_excel("days_info_dict.xlsx", index_label="Name of the Day")
print("\ntuple with all the characters and their number of occurences in each name of the day.")


char_occurrences = tuple((day, Counter(day)) for day in days_of_week)
print(char_occurrences)
my_dict={"Name of the Day", "Occurences", "Short Form", "Name in Lower", "Name in upper", "Length"}

headers = list(my_dict.keys())
print(f'{headers[0] <10}{headers[1] <15}{headers[2]<15}{headers[3]<15}{headers[4]<15}{headers[5]<15}')
