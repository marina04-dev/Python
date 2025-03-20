#exercise_1
def favorite_movie(movie_title):
    if "Batman" in movie_title:
        print("Goood choice")
    else:
        print("Awful taste!")
        
favorite_movie("Batman and Robin")
favorite_movie("Superman returns")


#exercise_2
def favorite_author(author):
    if "Tolkien" in author:
        for _ in range(500):
            print("Tolkien is the best!!!")
    else:
        print(author + "is good!")
        
favorite_author("J.R.R. Tolkien")
favorite_author("Stephen King")
