# lib/helpers.py
from models.genre import Genre
from models.movie import Movie

def list_genres():
    genres = Genre.get_all()
    for genre in genres:
        print(genre)

def find_genre_by_id():
    _id = input("Enter the movie's id: ")
    genre = Genre.find_by_id(_id)
    print(genre) if genre else print(f"Genre {_id} not found.")

    


def exit_program():
    print("Goodbye!")
    exit()
