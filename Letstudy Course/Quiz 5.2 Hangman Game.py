def word_to_array(data):
    new_word=list(data)
    return new_word

def initialize_word(new_word):
    for i in range(len(new_word)):
        word_with_underscores.append('_')

def check_letter(letter,new_word,word_with_underscores):
        letter=letter.upper()
        if letter in word_with_underscores:
            print('You have already used this letter. Please choose another: ')
        for i , k  in enumerate(new_word):
            if letter == k and word_with_underscores[i]!= letter:
                word_with_underscores[i]=letter
            
        if letter not in new_word :
            global tries
            tries-=1
            if tries > 1:
                print(f'This letter does not exist. You have another {tries} tries')
            elif tries == 1:
                print(f'This letter does not exist. You have another {tries} try')
            if tries == 0:
                print('You lost!!!')
                print(f'The word was {word}')
        if word_with_underscores == new_word:
            print (f'YOU WIN!!!! You found the word {word}')
            tries=0
            
word_with_underscores = []
tries = 6
word = input('Insert a word: ')
word = word.upper()
initialize_word(word_to_array(word))        
print(word_with_underscores)
while tries > 0:
    letter = input('Pick a letter: ')        
    check_letter(letter,word_to_array(word),word_with_underscores)
    if tries > 0:
        print(word_with_underscores)
