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
        
        #Entering all genre menu
        if choice == "1":
            genre_choice = "0"
            while genre_choice != "m":
                print('''

-----List of Genres-----''')
                list_genres()
                all_genre_menu()
                genre_choice = input("> ")

                if genre_choice == "c":
                    create_genre()
                elif genre_choice == "e":
                    exit_program()
                elif genre_choice == "m":
                    print("Back to main menu.")
                else:
                    find_genre_by_id(int(genre_choice))

        #Entering genre edit menu
        elif choice =="2":
            _id = int(input("Enter the genre's id: "))
            genre = find_genre_by_id(_id)
            movie_choice = 0
            while movie_choice != "m":
                print(genre)
                print('''

-----List of Movies in this Genre-----''')
                
                genre_edit_menu()

        #Entering genre edit menu
        elif choice =="3":
            pass
        #Entering all movie menu
        elif choice =="4":
            pass
        #Entering movie edit menu
        elif choice =="5":
            pass
        #Entering movie edit menu
        elif choice =="6":
            pass
        #Entering all movie menu
        elif choice =="7":
            pass
        elif choice == "e":
            exit_program()
        else:
            print("Invalid choice")

def main_menu():
    print('''

*****Main Menu*****

    Select an option:
    1. List all genres
    2. Find genre by id
    3. Find genre by name
    4. List all movies
    5. Find movie by id
    6. Find movie by title
    7. Find all movies with at least the run-time entered
    e. Exit the program

*******************

''')

def all_genre_menu():
    print('''
-----Genre Menu-----

    Enter genre id to see more details.

    OR

    Select an option:
    c. Create new genre
    m. Main Menu
    e. Exit the program
                
--------------------''')

def all_movie_menu():
    print('''
-----Movie Menu-----

    Enter Movie id to see more details.

    OR

    Select an option:
    c. Create new movie
    m. Main Menu
    e. Exit the program
                
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
    e. Exit the program
                
~~~~~~~~~~~~~~~~~~~~''')

def movie_edit_menu():
    print('''
~~~~~Edit Menu~~~~~

    Select an option:
    u. Update movie
    d. Delete movie
    m. Main Menu
    e. Exit the program
                
~~~~~~~~~~~~~~~~~~~~''')


if __name__ == "__main__":
    main()