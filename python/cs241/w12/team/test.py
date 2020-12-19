import pandas
import matplotlib

from datetime import datetime





data = pandas.read_csv("python/cs241/w12/team/data/weather_year.csv")
print(data)
print(len(data))
f = data.mean_temp.head()
print(f)
data.mean_temp.hist()