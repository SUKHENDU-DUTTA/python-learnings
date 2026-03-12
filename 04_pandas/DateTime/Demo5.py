import pandas as pd

timestamp = pd.Timestamp(year=2003, month=8, day=22)
print("Date and Time: \n",timestamp)

print("\nCheck leap year:\n",timestamp.is_leap_year)