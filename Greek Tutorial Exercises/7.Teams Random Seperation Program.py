# Teams Random Seperation Program  - (Lesson 7: Exercise 4)
from random import randrange
from random import seed
from datetime import datetime

seed(datetime.now())

# Even Number of Class Students
N = 30

# Set with Students IDs (without names)
pupils = set()
for number in range(N):
    pupils.add("Pupil " + str(number))
 
# Math Teams    
list_pupils = list(pupils)
math_teams = set()
for _ in range(N//2):
    pos1 = randrange(0,len(list_pupils))
    pupil1 = list_pupils.pop(pos1)
    pos2 = randrange(0,len(list_pupils))
    pupil2 = list_pupils.pop(pos2)
    team = (pupil1, pupil2)
    math_teams.add(team)
print("Math Teams: \n" + str(math_teams))

# Geography Teams
list_pupils = list(pupils)
geography_teams = set()
for _ in range(N//2):
    pos1 = randrange(0,len(list_pupils))
    pupil1 = list_pupils.pop(pos1)
    pos2 = randrange(0,len(list_pupils))
    pupil2 = list_pupils.pop(pos2)
    team = (pupil1, pupil2)
    geography_teams.add(team)
print("\nGeography Teams: \n" + str(geography_teams))
