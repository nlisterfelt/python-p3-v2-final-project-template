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
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_genres()
        elif choice == "2":
            find_genre_by_id()
        elif choice == "3":
            find_genre_by_name()
        elif choice == "4":
            create_genre()
        elif choice == "5":
            update_genre()
        elif choice == "6":
            delete_genre()
        elif choice == "7":
            list_movies()
        elif choice == "8":
            find_movie_by_id()
        elif choice == "9":
            find_movie_by_title()
        elif choice == "10":
            find_movies_by_run_time()
        elif choice == "11":
            create_movie()
        elif choice == "12":
            update_movie()
        elif choice == "13":
            delete_movie()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. ")
    print("2. ")
    print("3. ")
    print("4. ")
    print("5. ")
    print("6. ")
    print("7. ")
    print("8. ")
    print("9. ")
    print("10. ")
    print("11. ")
    print("12. ")


if __name__ == "__main__":
    main()
