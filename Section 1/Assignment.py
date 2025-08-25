# Assignment on tuples
favorite_movies = ("PeekBlinders", "Theflash", "Snowfall", "Teenwolf", "Blidemask")
print("All list of the movies:", favorite_movies)
print("The first movie:",favorite_movies[0]) # Printing the first movie in the tuple
print("The last movie:",favorite_movies[-1]) # Printing the last movie in the tuple

print("The Total number of the movies:",len(favorite_movies)) # Printing the total number of the movies in the tuple

# checking if the movie is exist in the list

movie_check = input("Enter the name of movie to check if it is on your favorite list of movies: ")
if movie_check in favorite_movies:
    print(f"Yes, '{movie_check}' is one of your favorite movie")
else:
    print(f"No, '{movie_check}' is not in your favorite movies")

new_movie = input("Enter the new movie you would like to add on your favorite movie list: ")
new_movie_favorite = favorite_movies + (new_movie,)

print("\n Here are all your favorite movies now")
for movie in new_movie_favorite:
    print(movie)
