from phonebook import Phonebook

file = "phonebook.json"
pb = Phonebook(file)

try:
  while True:
    print("\nПрограмма телефонного справочника\nCписок команд:\n\t1)Вывести список контактов.\n\t2)Добавить запись в телефонный справочник\n\t3)Отредактировать запись.\n\t4)поиск записей по одной или нескольким характеристикам.\n\t5)Выход из программы.")
    choose = input("Введите команду: ")
    match choose:
        case "1":
            pb.list_contacts(numeric=3)
            input("Ok...")
        case "2":
            data = {}

            data['surname'] = input('Введите фамилию: ').strip()
            while not data['surname']:
                print('Фамилия не может быть пустой строкой. Пожалуйста, введите заново.')
                data['surname'] = input('Введите фамилию: ').strip()

            data['name'] = input('Введите имя: ').strip()
            while not data['name']:
                print('Имя не может быть пустой строкой. Пожалуйста, введите заново.')
                data['name'] = input('Введите имя: ').strip()

            data['patronymic'] = input('Введите отчество: ').strip()
            while not data['patronymic']:
                print('Отчество не может быть пустой строкой. Пожалуйста, введите заново.')
                data['patronymic'] = input('Введите отчество: ').strip()

            data['organization'] = input('Введите название организации: ').strip()
            data['work phone'] = input('Введите рабочий телефон: ').strip()
            data['personal phone'] = input('Введите личный телефон: ').strip()

            pb.add_contact(**data)
            print(f"\n\tБыл добавлен контакт: {data['name']} {data['surname']}")
            for key, value in data.items():
                print(f"\t{key}: {value}")
            input("Ok...")

        case "3":
            contact_name = input('\nВведите название контакта, которое хотите отредактировать: ').strip()
            if pb.if_contact(contact_name):
                while True:
                    choose_2 = input('\nХотите изменить название контакта? (Да/Нет): ').strip().lower()
                    if choose_2 in ['да', 'нет']:
                        if choose_2 == 'да':
                            new_cn = input(f"\nНовое имя контакта для {contact_name}: ")
                            break
                        else:
                            new_cn = None
                            break
                    else:
                        print("\nПожалуйста, введите 'Да' или 'Нет'.")
                
                data = {}
                surname = input('Введите фамилию: ').strip()
                if surname:
                    data['surname'] = surname
                name = input('Введите имя: ').strip()
                if name:
                    data['name'] = name
                patronymic = input('Введите отчество: ').strip()
                if patronymic:
                    data['patronymic'] = patronymic
                organization = input('Введите название организации: ').strip()
                if organization:
                    data['organization'] = organization
                work_phone = input('Введите рабочий телефон: ').strip()
                if work_phone:
                    data['work phone'] = work_phone
                personal_phone = input('Введите личный телефон: ').strip()
                if personal_phone:
                    data['personal phone'] = personal_phone
                pb.edit_contact(contact_name=contact_name, new_cn =  new_cn, **data)
                input("Ok...")
            else:
                print(f"\nКонтакт {contact_name} не найден в файле \"{file}\" ")
                input("Ok...")

        case "4":
            data = {}
            surname = input('\nВведите фамилию: ').strip()
            if surname:
                data['surname'] = surname
            name = input('Введите имя: ').strip()
            if name:
                data['name'] = name
            patronymic = input('Введите отчество: ').strip()
            if patronymic:
                data['patronymic'] = patronymic
            organization = input('Введите название организации: ').strip()
            if organization:
                data['organization'] = organization
            work_phone = input('Введите рабочий телефон: ').strip()
            if work_phone:
                data['work phone'] = work_phone
            personal_phone = input('Введите личный телефон: ').strip()
            if personal_phone:
                data['personal phone'] = personal_phone
            result = pb.search_contact(**data)

            if bool(result):
                for key, value in result.items():
                    print(f"\n\tБыл найден контакт: {key}:")
                    for k,v in value.items():
                        print(f"\t{k}: {v}")
            else: 
                print("По данным параметрам ничего не найдено...")
            input("Ok...") 
        case "5":
            break
finally:
  print('Выполнение программы прекращено.')
