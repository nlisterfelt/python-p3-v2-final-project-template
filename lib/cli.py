# lib/cli.py

from helpers import (
    list_genres,
    find_genre_by_id,
    find_genre_by_name,
    create_genre,
    update_genre,
    delete_genre,
    list_movies,
    find_movie_by_id,
    find_movie_by_name,
    find_movies_by_run_time,
    list_movies_by_genre,
    create_movie,
    update_movie,
    delete_movie,
    exit_program
)


def main():
    choice = "0"
    while choice != "e":
        main_menu()
        choice = input("> ")
        
        #Main menu - list all genres
        if choice == "1":
            all_genre_choice = 0
            while all_genre_choice != "m":
                print('''
~~~~~~~~~~~~~~~~~~~~
       Genres
~~~~~~~~~~~~~~~~~~~~

''')
                list_genres()
                print('''
            
~~~~~~~~~~~~~~~~~~~~
''')
                all_menu()
                all_genre_choice = input("> ")

                #All genres - id or name for genre details
                if all_genre_choice == "i" or all_genre_choice == "n":
                    if all_genre_choice == "i":
                        genre = find_genre_by_id()
                    else:
                        genre = find_genre_by_name()
                    genre_choice = 0

                    while genre_choice !="g":
                        print(f'''

~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
    Movies for {genre.name}
~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~


''')
                        list_movies_by_genre(genre.id)
                        print('''
            
~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
''')
                        genre_menu()
                        genre_choice = input("> ")
                        #Genre details - choose movie by id or name
                        if genre_choice == "i" or genre_choice == "n":
                            #One movie
                            if genre_choice == "i":
                                movie = find_movie_by_id()
                            else:
                                movie = find_movie_by_name()
                            movie_choice = 0
                            while movie_choice != "v":
                                print(f'''

------------------------------
    Movie: {movie.name}
    Run time: {movie.run_time} mins
    Genre id: {movie.genre_id}
------------------------------

''')
                                movie_menu()
                                movie_choice = input("> ")
                                #Movie details - update movie
                                if movie_choice == "u":
                                    update_movie(movie.id)
                                #Movie details - delete movie
                                elif movie_choice == "d":
                                    delete_movie(movie.id)
                                    movie_choice = "v"
                                #Movie details - back to all movies
                                elif movie_choice == "v":
                                    print("Back to Movie Menu")
                                    movie_choice = "v"
                                elif movie_choice == "e":
                                    exit_program()
                                elif movie_choice == "m":
                                    print("Back to Main Menu")
                                    movie_choice = "v"
                                    genre_choice = "g"
                                    all_genre_choice = "m"
                                else:
                                    print("Invalid choice")
                        #Genre details - update genre
                        elif genre_choice == "u":
                            update_genre(genre.id)
                        #Genre details - delete genre
                        elif genre_choice == "d":
                            delete_genre(genre.id)
                            genre_choice = "g"
                        #Genre details - back to all genres
                        elif genre_choice == "g":
                            print("Back to Genre Menu")
                        elif genre_choice == "e":
                            exit_program()
                        elif genre_choice == "m":
                            print("Back to Main Menu")
                            genre_choice = "g"
                            all_genre_choice = "m"
                        else:
                            print("Invalid choice")
                #All genres - create a new genre
                elif all_genre_choice == "c":
                    create_genre()
                elif all_genre_choice == "m":
                    print("Back to Main Menu")
                elif all_genre_choice == "e":
                    exit_program()
                else:
                    print("Invalid choice")
        #Main menu - list all movies or by run-time
        elif choice == "2" or choice == "3":
            all_movie_choice = 0
            while all_movie_choice != "m":
                if choice == "2":
                    print('''

~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
        Movies
~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~

''')
                    list_movies()
                    print('''
            
~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~

''')
                else: 
                    run_time = input("Enter a number of minutes to see all movies with a run time of at least this number: ")
                    print(f'''

~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~~-~-~-~-~-~-~-~-~-~-~-~
    Movies with a run time of at least {run_time} mins
~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~~-~-~-~-~-~-~-~-~-~-~-~

''')
                    find_movies_by_run_time(run_time)
                    print('''
            
~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~~-~-~-~-~-~-~-~-~-~-~-~
''')
                all_menu()
                all_movie_choice = input("> ")
                #All movie - choose movie by id or name
                if all_movie_choice == "i" or all_movie_choice == "n":
                    #One movie
                    if all_movie_choice == "i":
                        movie = find_movie_by_id()
                    else:
                        movie = find_movie_by_name()
                    movie_choice = 0
                    while movie_choice != "v":
                        if not movie:
                            movie_choice = "v"
                        print(f'''

------------------------------
    Movie: {movie.name}
    Run time: {movie.run_time} mins
    Genre id: {movie.genre_id}
------------------------------

''')
                        movie_menu()
                        movie_choice = input("> ")
                        #Movie details - update movie
                        if movie_choice == "u":
                            update_movie(movie.id)
                        #Movie details - delete movie
                        elif movie_choice == "d":
                            delete_movie(movie.id)
                            movie_choice = "v"
                        #Movie details - back to all movies
                        elif movie_choice == "v":
                            print("Back to Movie Menu")
                            choice = "2"
                        elif movie_choice == "e":
                            exit_program()
                        elif movie_choice == "m":
                            print("Back to Main Menu")
                            movie_choice = "v"
                            all_movie_choice = "m"
                        else:
                            print("Invalid choice")
                #All movie - create new movie
                elif all_movie_choice == "c":
                    create_movie()
                    choice = "2"
                elif all_movie_choice == "m":
                    print("Back to Main Menu")
                elif all_movie_choice == "e":
                    exit_program()
                else:
                    print("Invalid choice")
        #Main menu - exit
        elif choice == "e":
            exit_program()
        else:
            print("Invalid choice")


def main_menu():
    print('''

    ********************
        Main Menu
    ********************

    Select an option:
    1. List all genres
    2. List all movies
    3. List all movies with at least the run-time entered
    e. Exit the program

    ********************

''')

def all_menu():
    print('''
    
    ----------------------

    Select an option:
    i. Enter id for more details
    n. Enter name for more details 
    c. Create new 
    m. Back to Main Menu
    e. Exit the program

    ----------------------

''')

def genre_menu():
    print('''
    
    ----------------------
    
    Select an option:
    i. Enter id for more details
    n. Enter name for more details 
    u. Update
    d. delete
    g. Back to Genre Menu
    m. Back to Main Menu
    e. Exit the program

    ----------------------

''')

def movie_menu():
    print('''
    
    ----------------------
    
    Select an option:
    u. Update
    d. delete
    v. Back to Movie Menu
    m. Back to Main Menu
    e. Exit the program

    ----------------------

''')


if __name__ == "__main__":
    main()