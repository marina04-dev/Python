poem = """ There's a bluebird in my heat that 
wants to get out
but I'm too enough for him,
I say,
stay down, do you want too mess me up?
you want to screw up the works?
you want to blow my book sales in Europe?
""" 

while True:
    string = input("Give a word: ")
    string = string.strip()
        
    if string.isalpha():
        word = string.lower()
        break
    else:
        print("Only characters please!")
        
        
poem_lowered = poem.lower()
poem_lines = poem_lowered.splitlines()
print(poem_lines)

for pos in range(len(poem_lines)):   
    if poem_lines[pos].find(word)!=-1:
        print("Line " + str(pos) + ": " +poem_lines[pos].replace(word,word.upper()))
