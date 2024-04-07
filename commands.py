from record import Record
from decorator import input_error


@input_error
def add_contact(book, args):
    if len(args) != 2:
        raise ValueError("Для додавання контакту введіть ім'я та номер телефону у форматі: add <ім'я> <телефон>")
    name, phone = args
    record = book.find(name)
    if record is None:
        record = Record(name)
        book.add_record(record)
    record.add_phone(phone)
    return "Контакт додано"

@input_error
def change_contact(book, args):
    if len(args) != 3:
        raise ValueError("Для зміни контакту вкажіть ім'я, поточний та новий номер телефону у форматі: change <ім'я> <старий телефон> <новий телефон>")
    name, old_phone, new_phone = args
    record = book.find(name)
    if record is not None:
        record.edit_phone(old_phone, new_phone)
        return "Номер змінено"
    else:
        return "Контакт не знайдено"

@input_error
def show_phone(book, args):
    if not args:
        raise ValueError("Вкажіть ім'я для перегляду номера телефону у форматі: phone <ім'я>")
    name = " ".join(args)
    record = book.find(name)
    if record is not None:
        phones = [str(phone) for phone in record.phones]
        if phones:
            return ", ".join(phones)
        else:
            return "Немає номерів для цього контакту"
    else:
        return "Контакт не знайдено"

@input_error
def remove_phone(book, args):
    if len(args) != 2:
        raise ValueError("Вкажіть ім'я контакту та номер для видалення у форматі: remove-phone <ім'я> <номер>")
    name, phone = args
    record = book.find(name)
    if record is not None:
        record.remove_phone(phone)
        return "Номер видалено"
    else:
        return "Контакт не знайдено"

@input_error
def add_birthday(book, args):
    if len(args) != 2:
        raise ValueError("Вкажіть ім'я та дату народження у форматі: add-birthday <ім'я> <дата народження>")
    name, birthday = args
    record = book.find(name)
    if record is not None:
        record.add_birthday(birthday)
        return "Дату народження додано"
    else:
        return "Контакт не знайдено"

@input_error
def show_birthday(book, args):
    if not args:
        raise ValueError("Вкажіть ім'я для перегляду дати народження у форматі: show-birthday <ім'я>")
    name = args[0]
    record = book.find(name)
    if record is not None and record.birthday is not None:
        return str(record.birthday)
    else:
        return "Дату народження не знайдено"
    
