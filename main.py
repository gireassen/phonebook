import json

class Phonebook():
    
    def __init__(self, phonebook = 'phonebook.json'):
        with open(phonebook, encoding = 'utf-8') as file:
            self.data_load = json.load(file)

    def list_contacts():
        ...

    def add_contact():
        ...

    def edit_contact():
        ...

    def serach_contact():
        ...

    
