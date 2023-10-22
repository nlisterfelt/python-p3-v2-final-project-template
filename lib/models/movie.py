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

    