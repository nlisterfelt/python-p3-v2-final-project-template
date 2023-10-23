# lib/helpers.py
from models.genre import Genre
from models.movie import Movie

def list_genres():
    genres = Genre.get_all()
    for genre in genres:
        print(genre)

def find_genre_by_id():
    _id = input("Enter the genre's id: ")
    genre = Genre.find_by_id(_id)
    print(genre) if genre else print(f"Genre {_id} not found.")

def find_genre_by_name():
    name = input("Enter the genre's name: ")
    genre = Genre.find_by_name(name)
    print(genre) if genre else print(f"Genre {name} not found.")

def create_genre():
    name = input("Enter the genre's name: ")
    try: 
        genre = Genre.create(name)
        print(f"Success: {genre}")
    except Exception as exc:
        print("Error creating genre: ", exc)

def update_genre():
    _id = input("Enter the genre's id: ")
    if genre := Genre.find_by_id(_id):
        try: 
            name = input("Enter the genre's name: ")
            genre.name = name
            genre.update()
            print(f"Success: {genre}")
        except Exception as exc:
            print("Error updating genre: ")
    else:
        print(f"Genre {_id} not found.")

def delete_genre():
    _id = input("Enter the genre's id: ")
    if genre := Genre.find_by_id(_id):
        genre.delete()
        print(f"Success {_id} deleted.")
    else:
        print(f"Genre {_id} not found.")

def list_movies():
    movies = Movie.get_all()
    for movie in movies:
        print(movie)

def find_movie_by_id():
    _id = input("Enter the movie's id: ")
    movie = Movie.find_by_id(_id)
    print(movie) if movie else print(f"Movie {_id} not found.")

def find_movie_by_title():
    title = input("Enter the movie's title: ")
    movie = Movie.find_by_title(title)
    print(movie) if movie else print(f"Movie {title} not found.")

def find_movies_by_run_time():
    run_time = input("Enter a number of minutes to see all movies with a runtime of at least this number: ")
    movies = Movie.find_at_least_run_time(run_time)
    print(movies) if movies else print(f"No movies found with a run-time of at least {run_time}")

def create_movie():
    title = input("Enter the movie's title: ")
    run_time = input("Enter the movie's run-time in minutes: ")
    genre_id = input("Enter the movie's genre id: ")
    try: 
        movie = Movie.create(title, run_time, genre_id)
        print(f"Success: {movie}")
    except Exception as exc:
        print("Error creating movie: ", exc)

def update_movie():
    _id = input("Enter the movie's id: ")
    if movie := Movie.find_by_id(_id):
        try: 
            title = input("Enter the movie's title: ")
            movie.title = title
            run_time = input("Enter the movie's run-time in minutes: ")
            movie.run_time = run_time
            genre_id = input("Enter the movie's genre id: ")
            movie.genre_id = genre_id
            movie.update()
            print(f"Success: {movie}")
        except Exception as exc:
            print("Error updating movie: ", exc)
    else:
        print(f"Movie {_id} not found.")

def delete_movie():
    _id = input("Enter the movie's id: ")
    if movie := Movie.find_by_id(_id):
        movie.delete()
        print(f"Success {_id} deleted.")
    else:
        print(f"Movie {_id} not found.")

def exit_program():
    print("Goodbye!")
    exit()
