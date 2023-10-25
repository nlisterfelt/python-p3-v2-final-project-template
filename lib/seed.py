from models.__init__ import CONN, CURSOR
from models.genre import Genre
from models.movie import Movie

def seed_database():
    Movie.drop_table()
    Genre.drop_table()
    Genre.create_table()
    Movie.create_table()
    rom_com = Genre.create("Romantic comedy")
    action = Genre.create("Action")
    Movie.create("The Proposal", 108, rom_com.id)
    Movie.create("27 Dresses", 111, rom_com.id)
    Movie.create("Dune", 155, action.id)
    Movie.create("Transformers", 127, action.id)
    Movie.create("Blue Beetle", 127, action.id)

seed_database()
print("Seeded database.")