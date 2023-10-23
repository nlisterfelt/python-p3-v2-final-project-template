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
            helper_1()
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
