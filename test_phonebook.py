from phonebook import Phonebook

pb = Phonebook("test_phonebook.json")
contact_data = {
        "surname": "Иванов",
        "name": "Иван",
        "patronymic": "Петрович",
        "organization": "TestOrg",
        "work_phone": "8(800)777-77-77",
        "personal_phone": "8(800)888-88-88"
    }
pb.add_contact(**contact_data)
result = pb.search_contact(organization = "TestOrg")
print(result)
pb.list_contacts(numeric=1)
pb.edit_contact(contact_name='Иван Иванов', organization = '123123123')