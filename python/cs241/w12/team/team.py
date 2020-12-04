import pandas
import matplotlib

from datetime import datetime





data = pandas.read_csv("python/cs241/w12/team/data/weather_year.csv")
print(data)
print(len(data))
print(data.columns)
print(data["EDT"])
print(data[["EDT", "Mean TemperatureF"]])
print(data.EDT)
print(data.EDT.head())
print(data.EDT.head(50))
print(data["Mean TemperatureF"].head())
#print(data.mean_temp_head())
#print(data.mean_temp.std())

data.columns = ["date", "max_temp", "mean_temp", "min_temp", "max_dew",
                "mean_dew", "min_dew", "max_humidity", "mean_humidity",
                "min_humidity", "max_pressure", "mean_pressure",
                "min_pressure", "max_visibilty", "mean_visibility",
                "min_visibility", "max_wind", "mean_wind", "min_wind",
                "precipitation", "cloud_cover", "events", "wind_dir"]

print(data.mean_temp.hist())
print(data.std)

first_date = data.date.values[0]
print(first_date)

print(datetime.strptime(first_date, "%Y-%m-%d"))

data.date = data.date.apply(lambda d: datetime.strptime(d, "%Y-%m-%d"))
print(data.date.head())

data.index = data.date
print(data)

print(data.loc[datetime(2012, 9, 19)])
#plt.show()

data = data.drop(["date"], axis=1)
print(data.columns)

empty = data.apply(lambda col: pandas.isnull(col))

print(empty.events.head(7))

print(data.events.head(10))

print(data.dropna(subset=["events"]))

data.events = data.events.fillna("")
print(data.events.head(10))
