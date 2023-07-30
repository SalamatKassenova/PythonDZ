def read_phonebook(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        phonebook = [line.strip().split(',') for line in file]
    return phonebook

def write_phonebook(filename, phonebook):
    with open(filename, 'w', encoding='utf-8') as file:
        for entry in phonebook:
            file.write(','.join(entry) + '\n')

def add_entry(phonebook, name, surname, phone):
    phonebook.append([name, surname, phone])

def find_entry(phonebook, keyword):
    result = []
    for entry in phonebook:
        if keyword.lower() in ' '.join(entry).lower():
            result.append(entry)
    return result

def update_entry(phonebook, old_entry, new_entry):
    for i, entry in enumerate(phonebook):
        if entry == old_entry:
            phonebook[i] = new_entry

def delete_entry(phonebook, entry):
    phonebook.remove(entry)

def view_entries(phonebook):
    if not phonebook:
        print("Справочник пуст.")
        return

    print("Все записи в справочнике:")
    for entry in phonebook:
        print(','.join(entry))

if __name__ == "__main__":
    filename = "file.txt"
    phonebook = read_phonebook(filename)

    while True:
        print("\n1. Добавить запись")
        print("2. Найти запись")
        print("3. Изменить запись")
        print("4. Удалить запись")
        print("5. Посмотреть все записи") 
        print("6. Выйти")

        choice = int(input("Выберите действие (1-6): "))

        if choice == 1:
            name = input("Введите имя: ")
            surname = input("Введите фамилию: ")
            phone = input("Введите телефон: ")
            add_entry(phonebook, name, surname, phone)
        elif choice == 2:
            keyword = input("Введите имя или фамилию для поиска: ")
            search_result = find_entry(phonebook, keyword)
            if search_result:
                for entry in search_result:
                    print(','.join(entry))
            else:
                print("Ничего не найдено.")
        elif choice == 3:
            old_name = input("Введите имя существующей записи: ")
            old_surname = input("Введите фамилию существующей записи: ")
            old_phone = input("Введите телефон существующей записи: ")
            old_entry = [old_name, old_surname, old_phone]

            new_name = input("Введите новое имя: ")
            new_surname = input("Введите новую фамилию: ")
            new_phone = input("Введите новый телефон: ")
            new_entry = [new_name, new_surname, new_phone]

            update_entry(phonebook, old_entry, new_entry)
        elif choice == 4:
            name = input("Введите имя существующей записи: ")
            surname = input("Введите фамилию существующей записи: ")
            phone = input("Введите телефон существующей записи: ")
            entry_to_delete = [name, surname, phone]

            delete_entry(phonebook, entry_to_delete)
        elif choice == 5:  # Новый пункт меню - просмотр всех записей
            view_entries(phonebook)
        elif choice == 6:
            write_phonebook(filename, phonebook)
            print("Справочник сохранен. До свидания!")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите число от 1 до 6.")
