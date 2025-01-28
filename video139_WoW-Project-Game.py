# Game Project: WoW (Part 1): Lesson 16 - Exercise 14
from random import randrange
from random import seed 
from datetime import datetime


class Character:
    def __init__(self,character_name,attack_speed=2,delay=0):
        self.character_name = character_name
        self.health = 100
        self.attack_speed = attack_speed
        self.delay = delay
    def attack(self):
        self.delay = 5 - self.attack_speed
        return randrange(3,11)
    def is_dead(self):
        return self.health <= 0 
    def end_round(self):
        self.health = self.health + 1 if self.health+1 <= 100 else 100
        self.delay -= 1 
    def print(self):
        print(f"{self.character_name} H:{self.health} D:{self.delay}")
        
class Arena:
    def __init__(self, team_A, team_B):
        self.team_A = team_A
        self.team_B = team_B
    def print_state(self):
        print("-" * 15)
        print("TEAM A")
        for character in self.team_A:
            character.print()
        print("-" * 15)
        print("TEAM B")
        for character in self.team_B:
            character.print()
        print("-" * 15)
    def play(self):
        time = -1 
        while True:
            time += 1 
            print("-" * 20)
            print("Time = " + str(time))
            print("-" * 20)
            self.print_state()
    
            # Creation of Characters List who can play 
            chars_to_play = []
            for character in self.team_A:
                if character.delay == 0:
                    chars_to_play.append(("A",character))
            for character in self.team_B:
                if character.delay == 0:
                    chars_to_play.append(("B",character))
                    
            # Active Characters Attack 
            for character in chars_to_play:
                attacking = character[1]
                if character[0] == "A":
                    defending = self.team_B[randrange(len(self.team_B))]
                else:
                    defending = self.team_A[randrange(len(self.team_A))]
                    
                damage = attacking.attack()
                defending.health -= damage
                print(f"{attacking.character_name} dealt {damage} to {defending.character_name}")
                
            # Dead Characters Check 
            for pos in range(len(self.team_A)-1,-1,-1):
                if self.team_A[pos].is_dead():
                    print(f"{self.team_A[pos].character_name} is dead!")
                    self.team_A.pop(pos)
                    
            for pos in range(len(self.team_B)-1,-1,-1):
                if self.team_B[pos].is_dead():
                    print(f"{self.team_B[pos].character_name} is dead!")
                    self.team_B.pop(pos)
                    
            # Check if There is a winner Team/game ended
            if len(self.team_A) == 0:
                print("Team B Won!!!")
                break
            elif len(self.team_B) == 0:
                print("Team A Won!!!")
                break 
            
            # End round
            for character in self.team_A:
                character.end_round()
            for character in self.team_B:
                character.end_round()
            input("Press Enter to Continue")
            
            
def main():
    seed(datetime.now())
    orcs = [Character("Orc-" + str(i+1),2,randrange(4)) for i in range(5)]
    night_elvs = [Character("Night Elf-" + str(i+1),3,randrange(3)) for i in range(5)]
    
    a = Arena(orcs, night_elvs)
    a.play()
    
main()
    
