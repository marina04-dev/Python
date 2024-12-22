def add_counter(value):
    value += 1
    return value
def strcount(data):
    chars = 0
    words = 1
    for x in data:
        if (x==" "):
            words=add_counter(words)
            chars=add_counter(chars)
        else:
            chars=add_counter(chars)
    return{"chars":chars,"words":words}
values=strcount("I Love Python")
print(f'''Total length: {values['chars']}
Total words: {values['words']}
''')
    
