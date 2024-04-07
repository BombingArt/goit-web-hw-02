from field import Name, Phone, Birthday
    
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        found = False
        for p in self.phones:
            if p.value == old_phone:
                found = True
                if p.validate_phone(new_phone):
                    p.value = new_phone
                else:
                    raise ValueError("Новий номер недійсний. Спробуйте ще раз")
        if not found:
            raise ValueError("Номер не знайдено")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def __str__(self):
        return f"\nКонтакт: {self.name}, Телефони: {' '.join(str(p)+', ' for p in self.phones)} {self.birthday if self.birthday else ''}"