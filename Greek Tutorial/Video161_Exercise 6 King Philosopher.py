class King:
    def __init__(self, kingdom):
        self.kingdom = kingdom
        
    def rule(self):
        print("Now I rule")
        
class Philosopher:
    def __init__(self, school):
        self.school = school
        
    def think(self):
        print("Now I think")
        
        
class PhilosopherKing(King, Philosopher):
    def __init__(self, kingdom, school):
        King.__init__(self,kingdom)
        Philosopher.__init__(self,school)
        
    def routine(self):
        self.think()
        self.rule()
        self.think()
        
        
marcus_avrilius = PhilosopherKing("Roman Empire", "Stoic")
marcus_avrilius.routine()
