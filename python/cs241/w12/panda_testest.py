import pandas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.close('all')

ts = pd.Series(np.random.randn(1000),
                   index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()

ts.plot()



s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
dates = pd.date_range('20130101', periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)

df2 = pd.                    DataFrame({'A': 1.,
                        'B': pd.Timestamp('20130102'),
                        'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                        'D': np.array([3] * 4, dtype='int32'),
                        'E': pd.Categorical(["test", "train", "test", "train"]),
                        'F': 'foo'})

print(df2)
df2types = df2.dtypes
print(df2types)


census_data = pandas.read_csv('/home/robert/Documentos/host/byui/robertgovia.github.io/python/cs241/w12/census.csv')

print(len(census_data))
print(census_data.columns)
print(census_data["n"])

mean = census_data.n.mean()
median =  census_data.n.median()
max = census_data.n.max()


print("the mean income is: {}\nthe mediam income is: {}\nthe max income is: {}".format(mean,median,max))

