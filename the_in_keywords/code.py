movies_watched = {"the matrix", "green book", "her"}    #usando set = {} pois as chaves(filmes) são únicas

user_movie = input("Enter something you've watched recently: ").lower()

print(user_movie in movies_watched)

# user = "the matrix"
# print("rix" in user)

# list = ["Rose", "Ted", "Joe"]
# print("Ted" in list)

## More Examples
#movies_watched = {"the matrix", "green book", "her"}    #usando set = {} pois as chaves(filmes) são únicas
#user_movie = input("Enter something you've watched recently: ")

#if user_movie in movies_watched:
#    print(f"I've watched {user_movie} too!")
#else:
#    print("I haven't watched that yet.")