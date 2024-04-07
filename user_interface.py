from abc import ABC, abstractmethod


class UserInterface(ABC):
    @abstractmethod
    def show_commands_info(self):
        pass

    @abstractmethod
    def get_user_input(self):
        pass

class ConsoleUserInterface(UserInterface):
    def show_commands_info(self):
        print("Доступні команди:")
        print("hello - Привітальне повідомлення")
        print("add - Додати новий контакт або номер телефону (формат: add <ім'я> <телефон>)")
        print("change - Змінити номер телефону для контакту (формат: change <ім'я> <старий телефон> <новий телефон>)")
        print("phone - Показати номери телефонів для контакту (формат: phone <ім'я>)")
        print("remove-phone - Видалити номер телефону для контакту (формат: remove-phone <ім'я> <телефон>)")
        print("add-birthday - Додати дату народження для контакту (формат: add-birthday <ім'я> <дата народження>)")
        print("show-birthday - Показати дату народження для контакту (формат: show-birthday <ім'я>)")
        print("all - Показати всі контакти")
        print("birthdays - Показати дні народження цього тиждня")
        print("exit, close - Вийти з програми\n")


    def get_user_input(self):
        return input("Введіть команду: ")
