import json

class Contact:
    def __init__(self, last_name, first_name, middle_name, organization, work_phone, personal_phone):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.organization = organization
        self.work_phone = work_phone
        self.personal_phone = personal_phone

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}, {self.organization}, {self.work_phone}, {self.personal_phone}"

class PhoneBook:
    def __init__(self, file_name):
        self.file_name = file_name
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.file_name, 'r') as file:
                data = json.load(file)
                for contact_data in data:
                    contact = Contact(**contact_data)
                    self.contacts.append(contact)
        except FileNotFoundError:
            # Если файл не найден, создаем пустой список контактов
            self.contacts = []

    def save_contacts(self):
        with open(self.file_name, 'w') as file:
            data = [vars(contact) for contact in self.contacts]
            json.dump(data, file)

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_contacts()

    def edit_contact(self, index, contact):
        self.contacts[index] = contact
        self.save_contacts()

    def search_contacts(self, **kwargs):
        results = []
        for contact in self.contacts:
            if all(getattr(contact, key) == value for key, value in kwargs.items()):
                results.append(contact)
        return results

    def display_contacts(self, page_num, page_size):
        start_index = (page_num - 1) * page_size
        end_index = start_index + page_size
        contacts_to_display = self.contacts[start_index:end_index]
        for contact in contacts_to_display:
            print(contact)

# Пример использования
            
class controls:
    phone_book = PhoneBook("phonebook.json")
    def start(self):
        phone_book = PhoneBook("phonebook.json")
        
        print("введите 1 для добавления контакта")
        print("введите 2 для вывода  контакох") 
        print("введите 3 для редактирования контакта") 
        print("введите 4 для поиска контакта")
        choose = int(input())
        # Добавление нового контакта
        if choose == 1:
            last_name = input("введите фамилию")
            name = input("введите имя")
            company = input("введите название компании")
            middle_name = input("введите отчество")
            personal_phone = input("введите личный телефон")
            work_phone = input("введите рабочий телефон")
            new_contact = Contact(last_name,name,middle_name,company,personal_phone,work_phone)
            phone_book.add_contact(new_contact)
            self.start()
        # Вывод контактов постранично
        elif choose==2:
            page  = int(input("введите номер страницы"))
            phone_book.display_contacts(page, 10)
            self.start()
         # Редактирование контакта
        elif choose == 3:
            id = int(input("введите номер контакта для редактирования"))
            last_name = input("введите фамилию")
            name = input("введите имя")
            company = input("введите название компании")
            middle_name = input("введите отчество")
            personal_phone = input("введите личный телефон")
            work_phone = input("введите рабочий телефон")
            edit_contact = Contact(last_name,name,middle_name,company,personal_phone,work_phone)
            phone_book.edit_contact(id-1, edit_contact)
            self.start()
         # Поиск контактов
        elif choose==4:
            print("введите 1 для поиска по имени")
            print("введите 2 для поиска по имени и фамилии") 
            second_chose = int(input())
            if second_chose==1:
                name = input("введите имя")
                search_results = phone_book.search_contacts(first_name=name)
                for result in search_results:
                    print(result)
                self.start()
            if second_chose==2:
                name = input("введите имя")
                last_name = input("введите фамилию")
                search_results = phone_book.search_contacts(first_name=name,last_name=last_name)
                for result in search_results:
                    print(result)
                self.start()    
        else:
            print("не такого варинта")
            self.start()


if __name__ == "__main__":
    obj = controls()
    obj.start()
    
	
