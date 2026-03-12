import pandas as pd

timestamp = pd.Timestamp(year=2003, month=8, day=31)
print("Date and Time: \n",timestamp)

print("\nCheck month end:\n",timestamp.is_month_end)