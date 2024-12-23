quote = "I don't hate them...I just feel better when they're not around."

while True:
    while True:
        string = input("Give a word: ")
        string = string.strip()
        
        if string.isalpha():
            word = string.lower()
            break
        else:
            print("Only characters please!")
            
    if word == "quit":
        break
            
    quote_lowered = quote.lower()
    
    if quote.find(word)!=-1:
        print(quote_lowered.replace(word,word.upper()))
    else:
        print("Word does not exist in quote!")
