from user_interface import ConsoleUserInterface
from input_parser import parse_input
from data_management import save_data, load_data
from commands import add_contact, change_contact, show_phone, remove_phone, add_birthday, show_birthday


def main():
    ui = ConsoleUserInterface()
    book = load_data()

    print("\nПомічник вітає Вас\n")
    ui.show_commands_info()
    while True:
        user_input = ui.get_user_input()
        command, *args = parse_input(user_input)

        if command == "exit" or command == "close":
            print("До зустрічі!")
            save_data(book)
            break

        elif command == "hello":
            print("Чим можу допомогти?")

        elif command == "add":
            print(add_contact(book, args))

        elif command == "change":
            print(change_contact(book, args))

        elif command == "phone":
            print(show_phone(book, args))

        elif command == "remove-phone":
            print(remove_phone(book, args))

        elif command == "add-birthday":
            print(add_birthday(book, args))

        elif command == "show-birthday":
            print(show_birthday(book, args))
        
        elif command == "all":
            contacts = book.data
            if contacts:
                for contact in contacts.values():
                    print(contact)

        elif command == "birthdays":
            upcoming_birthdays = book.get_upcoming_birthdays()
            if upcoming_birthdays:
                for bday in upcoming_birthdays:
                    print(f"День рождения {bday['name']} - {bday['birthday']}")
            else:
                print("Немає днів народження цього тиждня")

        elif command == "help":
            ui.show_commands_info()

        else:
            print("Неправильна команда. Для списку команд введіть 'help'.")

if __name__ == "__main__":
    main()