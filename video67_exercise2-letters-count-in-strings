#first_way
string = "I guess the only time most people think about in justice is when it happens to them."

lstring = list(string)

chars = {}
for char in lstring:
    if char not in chars:
        chars[char] = 1
    else:
        chars[char] += 1
        
print(chars)


#second_way
string = "I guess the only time most people think about in justice is when it happens to them."

letters = set(string)
dictionary = {letter: 0 for letter in letters}
print(dictionary)

for char in string:
    dictionary[char] += 1
    
print(dictionary)

for key in sorted(dictionary.keys()):
    print(key + ": " + str(dictionary[key]))
