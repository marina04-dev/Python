def strcount(data):
    chars = 0
    words = 0
    vowels = 0
    consonants = 0
    chars = len(data)
    for x in data:
        if (x==" "):
            words += 1
        elif (x in ('a','A','e','E','i','I','o','O','u','U')):
            vowels += 1
        else:
            consonants += 1
    return[chars,words,vowels,consonants]
    
values = strcount("Hi my name is Giorgos")
print(type(values))
print(f'''Total length: {values[0]}
Total words: {values[1]}
Total vowels: {values[2]}
Total consonants: {values[3]}
''')
