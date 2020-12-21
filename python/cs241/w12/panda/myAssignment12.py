import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.chdir("/home/robert/Documentos/host/byui/robertgovia.github.io/python/cs241/w12/panda/nba_basketball_data")

nba_data = pd.read_csv("basketball_players.csv")

#Calculate the mean and median number of points scored. (In other words, each row is the amount of points a player scored during a particular season. Calculate the median of these values. The result of this is that we have the median number of points players score each season.)

nba_points_median = nba_data["points"].median()
nba_points_mean = nba_data["points"].mean()
print("This is the median of all the point made on the nba history.\n", nba_points_median)
print("This is the mean of all the point made on the nba history.\n",nba_points_mean)

#just in case that have to be the median and mean of each player
"""
players = pd.read_csv("basketball_master.csv")

nba_player_points = pd.merge(nba_data, players, how ="left", left_on="playerID", right_on = "bioID")

print(nba_player_points)
points_per_player = nba_player_points[["playerID","useFirst","lastName","year","points"]].groupby("playerID").max()
print(points_per_player)
#points_per_player.to_csv("tes.csv")

print("median test")
points_per_player_median = nba_player_points[["playerID","useFirst","lastName","year","points"]].groupby("playerID").median()
print(points_per_player_median)

points_per_player_mean = nba_player_points[["playerID","useFirst","lastName","year","points"]].groupby("playerID").mean()
print(points_per_player_median.sort_values)

print("mean test")
points_per_player_mean = nba_player_points[["useFirst","lastName","year","points"]].groupby("playerID").mean()
points_per_player_mean_sorted = points_per_player_mean.sort_values("points",ascending=False).head(10)
print(points_per_player_mean)


"""


#Determine the highest number of points recorded in a single season. Identify who scored those points and the year they did so.
players = pd.read_csv("basketball_master.csv")

nba_player_points = pd.merge(nba_data, players, how ="left", left_on="playerID", right_on = "bioID")
#print(nba_player_points.columns)



player_most_points = nba_player_points[["useFirst","lastName","year","points"]].sort_values("points", ascending=False).head(1)
player_most_points = player_most_points.reset_index()

#nba_player_points.to_csv("nba_player_points.csv")
#Produce a boxplot that shows the distribution of total points, total assists, and total rebounds (each of these three is a separate box plot, but they can be on the same scale and in the same graphic).
print(player_most_points)
sns.boxplot(data=nba_data.points)
plt.show()
sns.boxplot(data=nba_data.assists)
plt.show()
sns.boxplot(data=nba_data.rebounds)
plt.show()


#Produce a plot that shows how the number of points scored has changed over time by showing the median of points scored per year, over time. The x-axis is the year and the y-axis is the median number of points among all players for that year.

nba_points_median = nba_data[["points","year"]].groupby("year").median()
nba_points_median = nba_points_median.reset_index()
sns.regplot(data=nba_points_median, x="year", y = "points")
plt.show()

