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

def exit_program():
    print("Goodbye!")
    exit()
