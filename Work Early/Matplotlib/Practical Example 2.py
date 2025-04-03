import matplotlib.pyplot as plt

# Data
players = ['Lionel Messi', 'Cristiano Ronaldo', 'Robert Lewandowski', 'Kylian Mbappe', 'Erling Haaland']
teams = ['PSG', 'Manchester United', 'Bayern Munich', 'PSG', 'Borussia Dortmund' ]
goals_scored = [12, 15, 16, 13, 14]
assists = [5,6,4,7,5]
games_played = [10,10,10,10,10]


# Problem 1: Titles, Labels & Legends
# Create a line plot to show the number of goals scored by
# each player throughout the Champions League.
plt.figure(figsize=(12,8))
plt.plot(players, goals_scored, marker='o', label='Goals')
plt.xlabel("Players")
plt.ylabel("Goals Scored")
plt.title("Goals Scored by PLayers in the Champions League")
plt.show()


# Problem 2: Colors, Markers & Line Styles
# Create a scatter plot to represent
# the correlation between the number of
# games played and the number of goals scored, using
# different colors and markers for different players.
colors = ['darkblue', 'darkgreen', 'darkred', 'purple', 'darkorange']
markers = ['o', 'v', '^', '<', '>']
plt.figure(figsize=(12,8))
for i in range(len(players)):
    plt.scatter(games_played[i], goals_scored[i], color=colors[i], marker=markers[i])
plt.xlabel("Games Played")
plt.ylabel("Goals Scored")
plt.title("Goals Scored vs Games Played")
plt.show()

# Problem 3: Ticks, Tick Labels & Limits
# Create a bar plot to show the total assists
# provided by each player. Adjust the ticks and
# limits of the y-axis for better visualization.
plt.figure(figsize=(10,6))
plt.bar(players, assists, color='skyblue')
plt.xlabel("Players")
plt.ylabel("Assists")
plt.title("Assists by Players in Champions League")
plt.yticks(range(0, 10, 1))  # setting the ticks from 0 to 10 with a step of 1
plt.ylim(0, 10)  # setting the limits from 0 to 10
plt.show()
