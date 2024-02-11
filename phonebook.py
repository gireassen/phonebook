import json
import os

class Phonebook:
    def __init__(self, file_path: str) -> None:
        '''
        Конструктор
        Принимает аргумент file_path, который представляет путь к файлу телефонного справочника.

        Параметры:
        - file_path: str - путь к json файлу.
        '''
        self.file_path = file_path
        self.create_file_if_not_exists()

    def create_file_if_not_exists(self) -> None:
        '''
        Метод для создания файла phonebook.json, если его нет.
        '''
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump({}, file, indent=4, ensure_ascii=False)

    def read_file(self) -> dict:
        '''
        Метод для чтения данных из файла.

        Возвращает:
        dict: Содержимое json файла.
        '''
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                contacts = json.load(file)
            return contacts
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File not found: {self.file_path}") from e

    def write_file(self, contacts: dict) -> None:
        '''
        Метод для записи данных в файл.

        Параметры:
        - contacts: dict - данные для записи контакта в справочник;
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

        Параметры:
        - numeric: int - число контактов в группе при просмотре контактов в справочнике;

        Выводит: группы контактов из телефонного справочника.
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
                    input("Next ->")
            if count == lenght:
                break

    def add_contact(self, **kwargs: dict) -> None:
        '''
        метод для добавления нового контакта в справочник

        Параметры
        - **kwargs: dict - используется для передачи неопределенного числа именованных аргументов(словаря),
        для заполнения данных нового контакта. если какие-либо параметры не заполнены, они создадутся пустыми;
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

        Параметры
        - **kwargs: dict - используется для передачи неопределенного числа именованных аргументов(словаря),
        по которым будет производится поиск;

        Возвращает: 
        - dict - словарь со словарями, где хранятся контакты которые удволетворяют запросам поиска;
        '''
        contacts = self.read_file()
        founded_contacts: dict = {}
        for contact_name, contact_data in contacts.items():
            is_match = all(contact_data.get(attribute) == value for attribute, value in kwargs.items())
            if is_match:
                founded_contacts[contact_name] = contact_data
        return founded_contacts

    def if_contact(self, contact_name: str) -> bool:
        '''
        метод для проверки, есть данный contact_name в файле
        '''
        contacts = self.read_file()
        if contact_name in contacts:
            return True
        else:
            return False
        

    def edit_contact(self, contact_name: str, new_cn: str = None, **kwargs: dict) -> None:
        '''
        метод для изменения контакта по его названию 

        Параметры:
        - contact_name: str - параметр для передачи названия контакта, по которому хотим произвести редактирование;
        - new_cn: str - новое название контакта (по умолчанию None);
        - **kwargs: dict - используется для передачи неопределенного числа новых именованных аргументов(словаря),
        по которым будет произведена корректировка(изменение);
        '''
        contacts = self.read_file()
        if contact_name not in contacts:
            raise ValueError(f"Contact '{contact_name}' not found.")
        contact_data = contacts.pop(contact_name)
        if new_cn:
            contacts[new_cn] = contact_data
        for attribute, value in kwargs.items():
            if attribute in contact_data:
                contact_data[attribute] = value
        self.write_file(contacts)

if __name__ == "__main__":
    print(__name__)

