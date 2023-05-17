# from pathlib import Path
# import csv

# path = Path('weather_data/death_valley_2021_simple.csv')
# lines = path.read_text().splitlines()

# reader = csv.reader(lines)
# header_row = next(reader)

# for index, column_header in enumerate(header_row):
#     print(index, column_header)

from pathlib import Path
import csv 
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('weather_data/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
#print(header_row)

#Extract high temperatures.
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f'Missing data for {current_date}')
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
        

print(highs)

# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates,highs, color='blue', alpha=0.5)
ax.plot(dates, lows, color ='red', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
ax.set_title("Daily High and Low Temperatures, 2021\nDeath Valley, CA", fontsize=20)
ax.set_xlabel('', fontsize=14)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=14)
ax.tick_params(labelsize=16)

plt.show()