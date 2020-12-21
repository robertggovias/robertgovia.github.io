import pandas as pd #our data manipulation
import matplotlib.pyplot as plt #low level methods, just in case
import seaborn as sns #graphic ploting
import os #thank to this we can change the directory to the right place


# This line isn't necessary, but it makes it so the later commands (e.g., read_csv)
# are in a consistent place (You will obviously need to change this to the correct location on _your_ computer.)
# If you have put the data files and your Python script in the same folder, you
# don't need this line.
os.chdir("/home/robert/Documentos/host/byui/robertgovia.github.io/python/cs241/w12/panda/nba_basketball_data")

# Load in the data
# The players data (basketball_players.csv) has the season stats
players = pd.read_csv("basketball_players.csv")

print("lista entera")
print(players)

print("lista de columnas")
print(players.columns)
min = players["rebounds"].min()
print("min player rebouns")
max = players["rebounds"].max()
print("max player rebouns")
mean = players["rebounds"].mean()
print("mean player rebouns")
median = players["rebounds"].median()
print("mediam player rebouns")

print("Rebounds per season: Min:{}, Max:{}, Mean:{:.2f}, Median:{}".format(min, max, mean, median))

print(players.sort_values("rebounds", ascending=False).head(10))

print(players[["playerID","year","tmID","rebounds"]].sort_values("rebounds", ascending = False).head(10))

master = pd.read_csv("basketball_master.csv")

nba = pd.merge(players, master, how ="left", left_on="playerID", right_on = "bioID")

print("player e master juntos")
print(nba.columns)

print(nba[["year","useFirst","lastName","tmID","rebounds"]].sort_values("rebounds", ascending=False).head(10))

nba["reboundsPerGame"] = nba["rebounds"] / nba["GP"]
print(nba[["year","useFirst","lastName","GP","rebounds","reboundsPerGame"]].sort_values("reboundsPerGame", ascending=False).head(10))
nba = nba[nba.GP > 0]
print(nba[["year","useFirst","lastName","GP","rebounds","reboundsPerGame"]].sort_values("reboundsPerGame", ascending=False).head(10))

sns.boxplot(data=nba.reboundsPerGame)
plt.show()

plt.savefig("boxplot_reboundsPerGame.png")

sns.boxplot(data = nba[["rebounds","oRebounds","dRebounds"]])
plt.show()

plt.savefig("3.png")

# Get a subset of the data where the year is between 1980 and 1990
eighties = nba[(nba.year >= 1980) & (nba.year < 1990)]

sns.boxplot(y=eighties["reboundsPerGame"],orient="v")
plt.show()

grid = sns.FacetGrid(eighties, col="year")
grid.map(sns.boxplot, "reboundsPerGame", orient ="Vertical")

plt.show()


nba_by_year = nba[["reboundsPerGame","year"]].groupby("year").median()
print(nba_by_year)

nba_by_year = nba_by_year.reset_index()
sns.regplot(data=nba_by_year, x="year", y="reboundsPerGame")
plt.show()

nba_by_year = nba_by_year[nba_by_year["reboundsPerGame"]>0]

sns.regplot(data = nba_by_year, x="year", y ="reboundsPerGame")
plt.show()

nba_by_year = nba[["reboundsPerGame","year"]].groupby("year").max()
nba_by_year = nba_by_year.reset_index()
nba_by_year = nba_by_year[nba_by_year["reboundsPerGame"]>0]
sns.regplot(data = nba_by_year, x= "year", y ="reboundsPerGame")
plt.show()

nba_top_rebounders_per_year = nba[["reboundsPerGame", "year"]].groupby("year")["reboundsPerGame"].nlargest(10)
nba_top_rebounders_per_year = nba_top_rebounders_per_year.groupby("year").median()
nba_top_rebounders_per_year = nba_top_rebounders_per_year.reset_index()
nba_top_rebounders_per_year = nba_top_rebounders_per_year[nba_top_rebounders_per_year["reboundsPerGame"]>0]
sns.regplot(data = nba_top_rebounders_per_year, x="year", y ="reboundsPerGame").set_title("Median of Top 10 Rebounder pr year")
plt.show()