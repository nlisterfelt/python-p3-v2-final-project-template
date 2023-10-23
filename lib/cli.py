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
        
        #Selecting a genre
        if choice == "1" or choice == "2" or choice = "3":
           
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




if __name__ == "__main__":
    main()