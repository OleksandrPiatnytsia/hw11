from collections import UserDict


class Field:
    def __init__(self, value):
        if not isinstance(value, str):
            raise ValueError("Inputed data must be str!")

        self.value = value

    def __str__(self):
        return self.value


class Name(Field):
    pass


class Phone(Field):

    def change_phone(self, new_phone: str):
        self.value = new_phone


class Record:
    def __init__(self, name: Name, phone: Phone = None):
        self.name = name
        self.phones = []

        if phone:
            if not isinstance(phone, Phone):
                raise ValueError("Phone must be class Phone")

            self.phones.append(phone)

    def __str__(self):
        return f"{self.name}: {', '.join([str(i) for i in self.phones])}"

    def add_phone(self, phone: Phone):

        if phone and isinstance(phone, Phone):
            for exist_phone in self.phones:
                if exist_phone.value == phone.value:
                    raise ValueError(f"Phone {phone} already exist!")

            self.phones.append(phone)
        else:
            raise ValueError(f"Phone must be class Phone")

    def remove_phone(self, phone: str):

        if phone:
            for exist_phone in self.phones:
                if exist_phone.value == phone:
                    self.phones.remove(exist_phone)
                    return f"Phone {phone} removed!"

    def change_phone(self, old_phone: Phone, new_phone: str):

        if not isinstance(new_phone, str):
            raise ValueError("New phone must be string")

        if not isinstance(old_phone, Phone):
            raise ValueError("Old phone must be class Phone")

        if old_phone.value == new_phone:
            return f"The phones are the same"

        phone_changed = False
        for exist_phone in self.phones:
            if exist_phone.value == old_phone.value:
                exist_phone.change_phone(new_phone)
                phone_changed = True

        if phone_changed:
            return f"Phone {old_phone} is changed"
        else:
            return f"Phone {old_phone} cant be changed! reason: phone exist!"


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def __str__(self):
        return ";\n".join([f"{k}: {v}" for k, v in self.data.items()])


if __name__ == '__main__':
    book = AddressBook()

    record1 = Record(Name("Тест1"), Phone("0960969696"))
    record1.add_phone(Phone("987865421"))
    print("record1: ", record1)

    record1.remove_phone("0960969696")
    print("record1: ", record1)

    # record1.change_phone(Phone("0960969696"), "0960969696")
    #
    # print("record1: ", record1)
    #
    # book.add_record(record1)
    #
    # record2 = Record(Name("Тест2"), Phone("987865421"))
    #
    # book.add_record(record2)
    #
    # print("AddressBook: ", book)
