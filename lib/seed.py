from models.__init__ import CONN, CURSOR
from models.genre import Genre
from models.movie import Movie

def seed_database():
    Movie.drop_table()
    Genre.drop_table()
    Movie.create_table()
    Genre.create_table()

    rom_com = Genre.create("Romantic comedy")
    Movie.create("The Proposal", 108, rom_com.id)

seed_database()
print("Seeded database.")