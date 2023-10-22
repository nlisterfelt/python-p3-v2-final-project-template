from models.__init__ import CURSOR, CONN
from models.genre import Genre

class Movie:
    all = {}
    def __init__(self, title, run_time, genre_id, id=None):
        self.id = id
        self.title = title
        self.run_time = run_time
        self.genre_id = genre_id

    def __repr__(self):
        return (f"<Movie {self.id}: {self.title}, {run_time}, Genre ID: {self.genre_id}")

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title):
            self._title = title
        else:
            raise ValueError("Title must be a non-empty string.")

    @property
    def run_time(self):
        return self._run_time

    @run_time.setter
    def run_time(self, run_time):
        if isinstance(run_time, int) and run_time>0:
            self._run_time = run_time
        else:
            raise ValueError("Run-time must me an integer above 0 representing minutes.")

    @property
    def genre_id(self):
        return self._genre_id

    @genre_id.setter
    def genre_id(self, genre_id):
        if isinstance(genre_id, int) and Genre.find_by_id(genre_id):
            self._genre_id = genre_id
        else:
            raise ValueError("genre_id must refrence a genre in the database.")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY,
                title TEXT,
                run_time INTEGER,
                genre_id INTEGER,
                FOREIGN KEY (genre_id) REFRENCES genres(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS movies;
        """
        CURSOR.execute(sql)
        CONN.commit()

    