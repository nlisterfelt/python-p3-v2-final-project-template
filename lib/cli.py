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
    e. Exit the program.

*******************

''')

def genre_menu():
    print(f'''
-----Genre Menu-----
ID: Name''')
    list_genres()       
    print('''
                        
    Select an option:
    c. Create new genre.
    n. Find genre by name.
    m. Main Menu
    e. Exit the program.
                
--------------------''')