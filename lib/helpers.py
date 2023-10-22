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
    movie = Movie.find_by_title(movie)
    print(movie) if movie else print(f"Movie {title} not found.")



def exit_program():
    print("Goodbye!")
    exit()
