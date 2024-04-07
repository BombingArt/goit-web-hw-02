from collections import UserDict
from datetime import datetime

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            return self.data.pop(name)

    def get_upcoming_birthdays(self):
        upcoming_birthdays = []
        today_date = datetime.today().date()

        for record in self.data.values():
            if record.birthday:
                birthday_date = record.birthday.value.date()

                next_birthday = birthday_date.replace(year=today_date.year)

                if next_birthday < today_date:
                    next_birthday = next_birthday.replace(year=today_date.year + 1)

                if (next_birthday - today_date).days <= 7:
                    upcoming_birthdays.append({
                        "name": record.name.value,
                        "birthday": next_birthday.strftime("%d.%m.%Y")
                    })

        return upcoming_birthdays