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
    find_movie_by_title,
    find_movies_by_run_time,
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
        
        #Entering Genre menu
        if choice == "g":
            genre_choice = "0"
            while genre_choice != "m":
                genre_menu()
                genre_choice = input("> ")

                if genre_choice == "c":
                    create_genre()
                #Entering Movie menu
                elif genre_choice == "n":
                    find_genre_by_name()
                elif genre_choice == "i":
                    find_genre_by_id()

                elif genre_choice == "e":
                    exit_program()
                else:
                    find_genre_by_id()
        elif choice == "e":
            exit_program()
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()

def main_menu():
    print('''

*****Main Menu*****

    Select an option:
    1. List all genres.
    2. Find genre by id.
    3. Find genre by name.
    4. List all movies.
    5. Find movie by id.
    6. Find movie by title.
    7. Find all movies with at least the run-time entered.
    e. Exit the program.

*******************

''')

def all_genre_menu():
    print('''
-----Genre Menu-----

    Enter genre id to see more details.

    OR

    Select an option:
    c. Create new genre.
    m. Main Menu
    e. Exit the program.
                
--------------------''')

def all_movie_menu():
    print('''
-----Movie Menu-----

    Enter Movie id to see more details.

    OR

    Select an option:
    c. Create new movie.
    m. Main Menu
    e. Exit the program.
                
--------------------''')

def genre_edit_menu():
    print('''
~~~~~Edit Menu~~~~~

    Enter Movie id to see more details.

    OR
 
    Select an option:
    u. Update genre
    d. Delete genre
    m. Main Menu
    e. Exit the program.
                
~~~~~~~~~~~~~~~~~~~~''')

def movie_edit_menu():
    print('''
~~~~~Edit Menu~~~~~

    Select an option:
    u. Update movie
    d. Delete movie
    m. Main Menu
    e. Exit the program.
                
~~~~~~~~~~~~~~~~~~~~''')