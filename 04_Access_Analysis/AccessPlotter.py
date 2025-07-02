import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("04_Access_Analysis/Access_Summary.csv", parse_dates=['StartTime', 'StopTime'])
df['Duration_min'] = df['Duration(s)'] / 60
df['Gap_min'] = df['StartTime'].diff().dt.total_seconds() / 60

plt.figure()
plt.plot(df['StartTime'], df['Duration_min'], marker='o')
plt.title("Access Duration per Pass")
plt.ylabel("Duration (min)")
plt.xlabel("Time")
plt.xticks(rotation=30)
plt.grid(True)
plt.tight_layout()
plt.savefig("04_Access_Analysis/Access_Duration_Toronto.png")
plt.show()
