import json

class Phonebook:
    def __init__(self, file_path: str) -> None:
        '''
        конструктор
        принимаем аргумент file_path, который представляет путь к файлу телефонного справочника
        '''
        self.file_path = file_path

    def read_file(self) -> dict:
        '''
        метод для чтения данных из файла
        '''
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                contacts = json.load(file)
            return contacts
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File not found: {self.file_path}") from e

    def write_file(self, contacts: dict) -> None:
        '''
        метод для записи данных в файл
        '''
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(contacts, file, indent=4, ensure_ascii=False)

    def list_contacts(self, numeric: int) -> None:
        '''
        метод для вывода на экран контактов из телефонного справоника
        по нескольку(numeric) контактов за раз.
        например list_contacts(3) будет выводит по три контакта
        при нажатии клавиши Enter выведется следующая группа
        из 3-х контактов
        '''
        contacts = self.read_file()
        lenght = len(contacts)
        count = 0
        fixed_numeric = numeric
        while True:
            for contact_name, contact_data in contacts.items():
                print(f"{contact_name}:")
                for attribute, value in contact_data.items():
                    print(f"\t{attribute}: {value}")
                count += 1
                if count == numeric:
                    numeric += fixed_numeric
                    input()
            if count == lenght:
                break

    def add_contact(self, **kwargs: dict) -> None:
        '''
        метод для добавления нового контакта в справочник
        '''
        contacts = self.read_file()
        data = {
            "surname": kwargs.get('surname', ''),
            "name": kwargs.get('name', ''),
            "patronymic": kwargs.get('patronymic', ''),
            "organization": kwargs.get('organization', ''),
            "work phone": kwargs.get('work_phone', ''),
            "personal phone": kwargs.get('personal_phone', '')
        }
        contacts[kwargs.get('name', '') + ' ' + kwargs.get('surname', '')] = data
        self.write_file(contacts)

    def search_contact(self, **kwargs: dict) -> dict:
        '''
        метод для поиска контактов по 1 или нескольким аргументам.
        если есть одинаковые аргументы у контактов, то вернет несколько результатов
        '''
        contacts = self.read_file()
        founded_contacts: dict = {}
        for contact_name, contact_data in contacts.items():
            is_match = all(contact_data.get(attribute) == value for attribute, value in kwargs.items())
            if is_match:
                founded_contacts[contact_name] = contact_data
        return founded_contacts

    def edit_contact(self, contact_name: str, **kwargs: dict) -> None:
        '''
        метод для изменения контакта по его названию 
        '''
        contacts = self.read_file()
        if contact_name not in contacts:
            raise ValueError(f"Contact '{contact_name}' not found.")
        contact_data = contacts[contact_name]
        for attribute, value in kwargs.items():
            if attribute in contact_data:
                contact_data[attribute] = value
        self.write_file(contacts)

if __name__ == "__main__":
    print(__name__)

