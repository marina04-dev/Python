# Word Finding in Quote (Lesson 9: Exercise 7)
quote = "I don't hate them...I just feel better when they're not around."

while True:
    while True:
        string = input("Enter a Word or Quit to Exit: ").strip()

        if string.isalpha():
            word = string.lower()
            break
        else:
            print("Only Characters Please! ")

    if word == "quit":
        break

    quote_lowered = quote.lower()

    if quote.find(word)!=-1:
        print(quote_lowered.replace(word,word.upper()))
    else:
        print("Word does not exist in quote!")
