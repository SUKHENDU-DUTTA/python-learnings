import pandas as pd

timestamp = pd.Timestamp(year=2003, month=1, day=10)
print("Date and Time: \n",timestamp)

print("\nCheck 1st month of year?:\n",timestamp.is_year_start)