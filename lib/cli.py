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
        
        if choice == "1":
            genre_choice = 0
            while genre_choice != "m":
                print('''
~~~~~Genres~~~~~

''')
                list_genres()
                print('''
            
~~~~~~~~~~~~~~~~
''')
                all_genres_menu()
                genre_choice = input("> ")

                if genre_choice == "i" or genre_choice == "n":
                    if genre_choice == "i":
                        genre = find_genre_by_id()
                    else:
                        genre = find_genre_by_name()
                    movie_choice = 0

                    while movie_choice !="m":
                        print(f'''
~~~~~Movies for {genre.name}~~~~~

''')
                        list_movies_by_genre(genre.id)
                        print('''
            
~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
''')
                        all_movies_menu()
                        movie_choice = input("> ")
                        if movie_choice == "i":
                            print("ok")
                        elif movie_choice == "e":
                            exit_program()
                        else:
                            print("Invalid choice")
                elif genre_choice == "c":
                    create_genre()
                elif genre_choice == "e":
                    exit_program()
                else:
                    print("Invalid choice")
        elif choice == "3":
            find_movies_by_run_time()
        elif choice == "e":
            exit_program()
        else:
            print("Invalid choice")

def main_menu():
    print('''

    *****Main Menu*****

    Select an option:
    1. List all genres
    2. List all movies
    3. List all movies with at least the run-time entered
    e. Exit the program

    *******************

''')

def all_menu():
    print('''
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
    Select an option:
    i. Enter id for more details
    n. Enter name for more details 
    u. Update
    d. delete
    m. Back to Main Menu
    e. Exit the program

----------------------

''')

def movie_menu():
    print('''
    Select an option:
    u. Update
    d. delete
    m. Back to Main Menu
    e. Exit the program

----------------------

''')


if __name__ == "__main__":
    main()