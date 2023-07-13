def print_contacts(contacts):
    for contact in contacts:
        print("Фамилия:", contact["last_name"])
        print("Имя:", contact["first_name"])
        print("Отчество:", contact["middle_name"])
        print("Номер телефона:", contact["phone_number"])
        print()

def add_contact(contacts):
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")

    contact = {
        "last_name": last_name,
        "first_name": first_name,
        "middle_name": middle_name,
        "phone_number": phone_number
    }

    contacts.append(contact)
    print("Контакт успешно добавлен.")

def search_contact(contacts):
    search_key = input("Введите характеристику для поиска (например, имя или фамилию): ")
    search_results = []

    for contact in contacts:
        if search_key.lower() in contact["last_name"].lower() or \
           search_key.lower() in contact["first_name"].lower() or \
           search_key.lower() in contact["middle_name"].lower() or \
           search_key in contact["phone_number"]:
            search_results.append(contact)

    if search_results:
        print("Результаты поиска:")
        print_contacts(search_results)
    else:
        print("Записей с указанной характеристикой не найдено.")

def export_contacts(contacts):
    filename = input("Введите имя файла для экспорта данных: ")

    try:
        with open(filename, "w") as file:
            for contact in contacts:
                file.write(f"Фамилия: {contact['last_name']}\n")
                file.write(f"Имя: {contact['first_name']}\n")
                file.write(f"Отчество: {contact['middle_name']}\n")
                file.write(f"Номер телефона: {contact['phone_number']}\n")
                file.write("\n")
        print("Экспорт успешно завершен.")
    except IOError:
        print("Ошибка при сохранении файла.")

def import_contacts(contacts):
    filename = input("Введите имя файла для импорта данных: ")

    try:
        with open(filename, "r") as file:
            data = file.readlines()

        contact = {}
        for line in data:
            line = line.strip()
            if line.startswith("Фамилия:"):
                contact["last_name"] = line.split(":")[1].strip()
            elif line.startswith("Имя:"):
                contact["first_name"] = line.split(":")[1].strip()
            elif line.startswith("Отчество:"):
                contact["middle_name"] = line.split(":")[1].strip()
            elif line.startswith("Номер телефона:"):
                contact["phone_number"] = line.split(":")[1].strip()
            elif line == "":
                contacts.append(contact)
                contact = {}

        print("Импорт успешно завершен.")
    except IOError:
        print("Ошибка при чтении файла.")

def phonebook():
    contacts = []

    while True:
        print("Меню:")
        print("1. Вывести все контакты")
        print("2. Добавить контакт")
        print("3. Поиск контакта")
        print("4. Экспорт контактов")
        print("5. Импорт контактов")
        print("6. Выход")

        choice = input("Введите номер операции: ")

        if choice == "1":
            print_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            export_contacts(contacts)
        elif choice == "5":
            import_contacts(contacts)
        elif choice == "6":
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

phonebook()
