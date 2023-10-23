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
        return (f"<Movie {self.id}: {self.title}, {self.run_time} mins, Genre ID: {self.genre_id}>")

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
        if type(run_time) is int and run_time>0:
            self._run_time = run_time
        else:
            raise ValueError("Run-time must me an integer above 0 representing minutes.")

    @property
    def genre_id(self):
        return self._genre_id

    @genre_id.setter
    def genre_id(self, genre_id):
        if type(genre_id) is int and Genre.find_by_id(genre_id):
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
                FOREIGN KEY (genre_id) REFERENCES genres(id))
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

    def save(self):
        sql = """
            INSERT INTO movies (title, run_time, genre_id)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.title, self.run_time, self.genre_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE movies
            SET title = ?, run_time = ?, genre_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.title, self.run_time, self.genre_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM movies
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, title, run_time, genre_id):
        movie = cls(title, run_time, genre_id)
        movie.save()
        return movie
    
    @classmethod
    def instance_from_db(cls, row):
        movie = cls.all.get(row[0])
        if movie:
            movie.title = row[1]
            movie.run_time = row[2]
            movie.genre_id = row[3]
        else:
            movie = cls(row[1], row[2], row[3])
            movie.id = row[0]
            cls.all[movie.id] = movie
        return movie

    @classmethod
    def get_all(cls):
        sql = """
            SELECT * 
            FROM movies
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM movies
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_title(cls, title):
        sql = """
            SELECT *
            FROM movies
            WHERE title = ?
        """
        row = CURSOR.execute(sql, (title,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_at_least_run_time(cls, run_time):
        sql = """
            SELECT *
            FROM movies
            WHERE run_time >= ?
        """
        rows = CURSOR.execute(sql, (run_time,)).fetchall()
        return[cls.instance_from_db(row) for row in rows]