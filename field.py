from datetime import datetime

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __str__(self):
        return f"І'мя: {self.value}"

class Phone(Field):
    def __init__(self, phone):
        if not self.validate_phone(phone):
            raise ValueError("Неправильний формат номеру. Введіть 10 цифр")
        super().__init__(phone)

    def validate_phone(self, phone):
        return len(phone) == 10 and phone.isdigit()

    def __str__(self):
        return f"{self.value}"

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Неправильний формат дати. Використовуйте ДД.ММ.РРРР")

    def __str__(self):
        return f"Дата народження: {self.value.strftime('%d.%m.%Y')}"
