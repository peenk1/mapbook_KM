import mapbook_lib.controller
from mapbook_lib.controller import user_info, add_user, remove_user, update_user, get_map
from mapbook_lib.model import users


def main():

    while True:
        print("===================MENU=======================")
        print("0. Wyjscie z programu")
        print("1. Wyświetlanie użytkowników")
        print("2. Dodaj znajomego")
        print("3. Usuń znajomego")
        print("4. Aktualizuj znajomego")
        print("5. Generuj mape")
        print("=============================================")

        tmp_choice:int= int(input('Wybierz opcje menu: '))
        if tmp_choice == 0:
            break
        if tmp_choice == 1:
            user_info(users)
        if tmp_choice == 2:
            add_user(users)
        if tmp_choice == 3:
            remove_user(users)
        if tmp_choice == 4:
            update_user(users)
        if tmp_choice == 5:
            get_map(users)

if __name__ == '__main__':
    main()