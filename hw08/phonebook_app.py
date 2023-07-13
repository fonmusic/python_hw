def print_contacts(contacts):
    for contact in contacts:
        print("Фамилия:", contact["last_name"])
        print("Имя:", contact["first_name"])
        print("Город:", contact["city"])
        print("Номер телефона:", contact["phone_number"])
        print()


def add_contact(contacts):
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите город: ")
    phone_number = input("Введите номер телефона: ")

    contact = {
        "last_name": last_name,
        "first_name": first_name,
        "city": middle_name,
        "phone_number": phone_number
    }

    contacts.append(contact)
    print("Контакт успешно добавлен.")


def search_contact(contacts):
    search_key = input("Введите имя или фамилию: ")
    search_results = []

    for contact in contacts:
        if search_key.lower() in contact["last_name"].lower() or \
                search_key.lower() in contact["first_name"].lower() or \
                search_key.lower() in contact["city"].lower() or \
                search_key in contact["phone_number"]:
            search_results.append(contact)

    if search_results:
        print("Результаты поиска:")
        print_contacts(search_results)
    else:
        print("Записей не найдено.")


def export_contacts(contacts):
    filename = input("Введите имя файла для экспорта данных: ")

    try:
        with open(filename, "w") as file:
            for contact in contacts:
                file.write(f"Фамилия: {contact['last_name']}\n")
                file.write(f"Имя: {contact['first_name']}\n")
                file.write(f"Город: {contact['city']}\n")
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
            elif line.startswith("Город:"):
                contact["city"] = line.split(":")[1].strip()
            elif line.startswith("Номер телефона:"):
                contact["phone_number"] = line.split(":")[1].strip()
            elif line == "":
                contacts.append(contact)
                contact = {}

        print("Импорт успешно завершен.")
    except IOError:
        print("Ошибка при чтении файла.")


def update_contact(contacts):
    search_key = input("Введите имя или фамилию контакта для обновления: ")
    update_key = input("Введите, что вы хотели бы обновить (имя, фамилию, город или номер): ")
    update_value = input("Введите новое значение: ")
    updated = False

    for contact in contacts:
        if search_key.lower() in contact["last_name"].lower() or search_key.lower() in contact["first_name"].lower():
            if update_key.lower() == "фамилия":
                contact["last_name"] = update_value
                updated = True
            elif update_key.lower() == "имя":
                contact["first_name"] = update_value
                updated = True
            elif update_key.lower() == "город":
                contact["city"] = update_value
                updated = True
            elif update_key.lower() == "номер":
                contact["phone_number"] = update_value
                updated = True

    if updated:
        print("Данные контакта успешно обновлены.")
    else:
        print("Контакт с указанным именем или фамилией не найден.")


def delete_contact(contacts):
    search_key = input("Введите имя или фамилию контакта для удаления: ")
    deleted = False

    for contact in contacts:
        if search_key.lower() in contact["last_name"].lower() or search_key.lower() in contact["first_name"].lower():
            contacts.remove(contact)
            deleted = True

    if deleted:
        print("Контакт успешно удален.")
    else:
        print("Контакт с указанным именем или фамилией не найден.")


def phonebook():
    contacts = []

    while True:
        print("Меню:")
        print("1. Вывести все контакты")
        print("2. Добавить контакт")
        print("3. Поиск контакта")
        print("4. Изменить контакт")
        print("5. Удалить контакт")
        print("6. Экспорт контактов")
        print("7. Импорт контактов")
        print("8. Выход")

        choice = input("Введите номер операции: ")

        if choice == "1":
            print_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            export_contacts(contacts)
        elif choice == "7":
            import_contacts(contacts)
        elif choice == "8":
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")


phonebook()
