import matplotlib.pyplot as plt

# Data
players = ['Harry Kane', 'Mo Salah', 'Bruno Fernandes', 'Jamie Vardy', 'Son Heung-min']
teams = ['Tottenham Hotspur', 'Liverpool', 'Manchester United', 'Leicester City', 'Tottenham Hotspur']
goals_season = [23, 25, 21, 22, 19]
assists_season = [8, 7, 11, 6, 10]
games_played_season = [34, 33, 34, 35, 33]
team_points_season = [65, 74, 70, 64, 65]

# Line Plot
# Create a line plot to show the number of goals scored by each player throughout the season.'''
plt.figure(figsize=(10, 6))
plt.plot(players, goals_season, marker='o')
plt.xlabel("Players")
plt.ylabel("Goals Scored")
plt.grid(True)
plt.title("Goals Scored by EPL PLayers in a Season")
plt.show()


# Scatter Plot
# Create a scatter plot to represent the correlation between the number of games played and the number of goals scored.'''
plt.figure(figsize=(10,6))
plt.scatter(games_played_season, goals_season, c='blue')
plt.xlabel("Games Played")
plt.ylabel("Goals Scored")
plt.grid(True)
plt.title("Goals Scored vs Games Played (Season)")
plt.show()


# Bar Plot
# Create a bar plot to show the total points earned by each team.
plt.figure(figsize=(10,6))
plt.bar(teams, team_points_season, color=['blue', 'red','red','blue', 'blue'])
plt.xlabel("Teams")
plt.ylabel("Points")
plt.grid(True)
plt.title("EPL Team Points (Season)")
plt.show()


# Pie Plot
# Create a pie chart to show the distribution of assists among the players.
plt.figure(figsize=(10,6))
plt.pie(assists_season,labels=players, autopct='%1.1f%%')
plt.title("Assists Distribution among EPL Players (Season)")
plt.axis('equal')
plt.show()
