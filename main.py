import json

class Phonebook:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                contacts = json.load(file)
            return contacts
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File not found: {self.file_path}") from e

    def write_file(self, contacts):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(contacts, file, indent=4, ensure_ascii=False)

    def list_contacts(self, numeric):
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

    def add_contact(self, **kwargs):
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


    def search_contact(self, **kwargs):
        contacts = self.read_file()
        founded_contacts = {}
        for contact_name, contact_data in contacts.items():
            is_match = all(contact_data.get(attribute) == value for attribute, value in kwargs.items())
            if is_match:
                founded_contacts[contact_name] = contact_data
        return founded_contacts

    def edit_contact(self, contact_name, **kwargs):
        contacts = self.read_file()
        if contact_name not in contacts:
            raise ValueError(f"Contact '{contact_name}' not found.")
        contact_data = contacts[contact_name]
        for attribute, value in kwargs.items():
            if attribute in contact_data:
                contact_data[attribute] = value
        self.write_file(contacts)

if __name__ == "__main__":
    # file_path = 'phonebook.json'
    # pb = Phonebook(file_path)
    # start_index = 1
    # pb.list_contacts(start_index)
    # pb.add_contact(surname = 'testov', name = 'test', patronymic = 'testovisch', organization = 'EffectiveMobile', work_phone = '8(800)555-35-35', personal_phone = '8(800)666-36-36')
    # contacts = pb.search_contact(surname="Иванов")
    # pb.edit_contact(contact_name="test_contact_2", surname="Андре111ев", name="Ан111дрей", organization="NotEffectiveMobile")
    pb.list_all_contacts()
