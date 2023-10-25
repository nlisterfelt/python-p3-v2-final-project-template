# lib/helpers.py
from models.genre import Genre
from models.movie import Movie

def list_genres():
    genres = Genre.get_all()
    for genre in genres:
        print(f"{genre.id}: {genre.name}")

def find_genre_by_id():
    _id = int(input("Enter the genre's id: "))
    genre = Genre.find_by_id(_id)
    if genre:
        return genre
    else:
        print(f"Genre {_id} not found.")

def find_genre_by_name():
    name = input("Enter the genre's name: ")
    genre = Genre.find_by_name(name)
    if genre:
        return genre
    else:
        print(f"Genre {name} not found.")

def create_genre():
    name = input("Enter the genre's name: ")
    try: 
        genre = Genre.create(name)
        print(f"Success: {genre}")
    except Exception as exc:
        print("Error creating genre: ", exc)

def update_genre(_id):
    if genre := Genre.find_by_id(_id):
        try: 
            name = input("Enter the genre's name: ")
            genre.name = name
            genre.update()
            print(f"Success updating {genre.name}")
        except Exception as exc:
            print("Error updating genre: ")
    else:
        print(f"Genre {_id} not found.")

def delete_genre(_id):
    if genre := Genre.find_by_id(_id):
        for movie in Movie.get_all():
            if movie.genre_id == _id:
                movie.delete()
        genre.delete()
        print(f"Success {_id} deleted.")
    else:
        print(f"Genre {_id} not found.")

def list_movies():
    movies = Movie.get_all()
    for movie in movies:
        print(f"{movie.id}: {movie.name}")

def list_movies_by_genre(genre_id):
    movies = Movie.find_movies_by_genre(genre_id)
    for movie in movies:
        print(f"{movie.id}: {movie.name}")

def find_movie_by_id():
    _id = input("Enter the movie's id: ")
    movie = Movie.find_by_id(_id)
    if movie:
        return movie
    else:
        print(f"Movie {_id} not found.")

def find_movie_by_name():
    name = input("Enter the movie's name: ")
    movie = Movie.find_by_name(name)
    if movie:
        return movie
    else:
        print(f"Movie {name} not found.")

def find_movies_by_run_time(run_time):
    movies = Movie.find_at_least_run_time(run_time)
    if movies:
        for movie in movies:
            print(f"{movie.id}: {movie.name}")
    else:
        print(f"No movies found with a run-time of at least {run_time} mins.")

def create_movie():
    name = input("Enter the movie's name: ")
    run_time = int(input("Enter the movie's run-time in minutes: "))
    genre_id = input("Enter the movie's genre id: ")
    try: 
        movie = Movie.create(name, run_time, genre_id)
        print(f"Success: {movie}")
    except Exception as exc:
        print("Error creating movie: ", exc)

def update_movie(_id):
    if movie := Movie.find_by_id(_id):
        try: 
            name = input("Enter the movie's name: ")
            movie.name = name
            run_time = int(input("Enter the movie's run-time in minutes: "))
            movie.run_time = run_time
            genre_id = input("Enter the movie's genre id: ")
            movie.genre_id = genre_id
            movie.update()
            print(f"Success: {movie}")
        except Exception as exc:
            print("Error updating movie: ", exc)
    else:
        print(f"Movie {_id} not found.")

def delete_movie(_id):
    if movie := Movie.find_by_id(_id):
        movie.delete()
        print(f"Success {_id} deleted.")
    else:
        print(f"Movie {_id} not found.")

def exit_program():
    print("Goodbye!")
    exit()
