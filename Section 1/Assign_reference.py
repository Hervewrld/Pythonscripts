# favorite_movies.py

# 1. Create a Tuple: Define a tuple with 5 favorite movies
favorite_movies = ("Inception", "The Dark Knight", "Interstellar", "The Matrix", "Avengers: Endgame")

# 2. Access Elements
print("All favorite movies:", favorite_movies)       # Print the entire tuple
print("First movie:", favorite_movies[0])            # First movie (index 0)
print("Last movie:", favorite_movies[-1])            # Last movie (index -1)

# 3. Count Movies
print("Total number of movies:", len(favorite_movies))

# 4. Check Membership: Ask the user for a movie and check if it's in the tuple
movie_check = input("Enter a movie name to check if it is in your favorites: ")
if movie_check in favorite_movies:
    print(f"Yes, '{movie_check}' is one of your favorite movies!")
else:
    print(f"No, '{movie_check}' is not in your favorite movies.")

# 5. Create a New Tuple: Add another movie from user input
new_movie = input("Enter another movie to add to your favorites: ")
new_favorite_movies = favorite_movies + (new_movie,)

# 6. Display All Movies: Print each movie on a new line
print("\nHere are all your favorite movies now:")
for movie in new_favorite_movies:
    print(movie)
