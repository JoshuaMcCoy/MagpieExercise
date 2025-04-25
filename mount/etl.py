import pandas as pd
from datetime import datetime
from pytz import timezone

# Import the contents of dummy.csv
df = pd.read_csv('dummy.csv')

# Open the local file 'output.txt' and truncate it
with open('output.txt', 'w') as file:
    # Add the current time in 12-hour format
    pacific_time = datetime.now(timezone('US/Pacific'))
    current_time = pacific_time.strftime('%I:%M:%S %p')
    file.write(f"Current Time: {current_time}\n\n")
    
    # Add the contents of dummy.csv
    file.write(df.to_string(index=False))