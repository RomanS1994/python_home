""""
This code implements an assistant for managing contact information and birthday reminders.

Classes:
- `Field` — base class for creating contact fields, including `Name`, `Phone`, and `Birthday`.
- `Name` — subclass of `Field` representing a contact's name.
- `Phone` — subclass of `Field` representing a phone number, with format validation.
- `Birthday` — subclass of `Field` storing a birthday date in the `DD.MM.YYYY` format.
- `Record` — stores contact information (name, phones, birthday) and allows phone editing.
- `AddressBook` — a dictionary of contacts with support for adding, deleting, searching, and retrieving birthday reminders.

Decorator:
- `input_error` — handles exceptions raised during command execution.

Main functions:
- `parse_input` — parses the user input into a command and arguments.
- `add_contact`, `change_number`, `show_phones`, `show_all`, `add_birthday`, `show_birthday`, `show_reminder` — user command handlers.
- `save_data`, `load_data` — functions for serializing and deserializing the address book data.

"""

from collections import UserDict
from datetime import datetime, date, timedelta
import re
import pickle



class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)



class Name(Field):
    pass



class Phone(Field):
    def check_phone(self):
        if len(self.value) == 10 and self.value.isdigit():
            return True 
        else:
            return False
             



class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)
        pattern = r'\d{2}.\d{2}.\d{4}'
        try:
            if re.search(pattern, value):
                datetime_object = datetime.strptime(value, '%d.%m.%Y').date()
                self.value = datetime_object
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


class Record: 
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None


    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        if phone.check_phone():
            self.phones.append(phone)
            print(f"Phone {phone_number} added.")
        else:
            print("Failed to add phone due to invalid format.")
            return None        

    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                


    def edit_phone(self, old_phone, new_phone):
        for index, phone in enumerate(self.phones):
            if phone.value == old_phone:
                if Phone(new_phone).check_phone():
                    self.phones[index] = Phone(new_phone)
                    return f"Phone {old_phone} changed to {new_phone}"
            else:
                return f"Phone {old_phone} not found"
    

    def find_phone(self, phone_number):
        try:
            for phone in self.phones:
                if phone.value == phone_number:
                    return phone.value
        except ValueError as e:
            print(e)

           
    def add_birthday(self, birthday_value):
        birthday = Birthday(birthday_value)
        if birthday:
            self.birthday = birthday



    def __str__(self):
        birthday_str = f", birthday: {self.birthday.value}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)} {birthday_str}"



class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
        print(f'Contact {record.name} added' )


    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            print(f'Contact with name "{name}" not found')
            return None


    def delete(self, name):
        if name in self.data:
            del self.data[name]
            
        else:
            print(f'Contact with name "{name}" not found')


    def get_upcoming_birthdays(self):
        """
        Returns a list of contacts with birthdays in the next 7 days.
        Returns:
            list of dict:
        """
        today = datetime.today().date()
        reminder = []

        for contact in self.data.values():
            birthday = contact.birthday
            if birthday != None:
                birthday_this_year = date(today.year, birthday.value.month, birthday.value.day)
                if birthday_this_year < today:
                    birthday_this_year = date(today.year + 1, birthday.value.month, birthday.value.day)
                days_until_birthday = (birthday_this_year - today).days

                if days_until_birthday <= 7:
                    if(birthday_this_year.weekday() == 5):
                        congratulation_date = birthday_this_year + timedelta(days=2)
                    elif(birthday_this_year.weekday() == 6):
                        congratulation_date = birthday_this_year + timedelta(days=1)
                    else:
                        congratulation_date = birthday_this_year

                    congratulation_date_str = datetime.strftime(congratulation_date, '%d.%m.%Y')
                    reminder.append({'name': contact.name.value, 'congratulation_date': congratulation_date_str}) 

        return reminder



def input_error(func):
    '''
    Decorator for handling errors in command processing functions.
    Parameters:
    func (function): The function to which the decorator is applied.

    Returns:
    function: Internal function that handles errors
    '''


    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            return e
        except ValueError as e:
            return e
        except IndexError as e:
            return e
        except Exception as e:
            return f'An unexpected error occurred: {e}. Please try again.'
    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args



@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@input_error
def remove_record(args, book: AddressBook):
    name, *_ = args 
    record = book.find(name)
    if record:
        book.delete(name)
        return f'Contact with name "{name}" is deleted'

@input_error
def change_number(args, book: AddressBook):
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    if record is None:
        return "Contact not found."
    return record.edit_phone(old_phone, new_phone)


@input_error
def show_phones(name, book: AddressBook):
    record = book.find(name)
    if record:
        phones = [phone.value for phone in record.phones]
        return f'numbers of name {name} is {phones}'
    
@input_error
def remove_phone(args, book: AddressBook):
    name, phone = args
    record = book.find(name)
    print(record)
    if record:
        for el in record.phones:
            if el.value == phone:
                record.remove_phone(phone)
                return f'phone "{phone}" is delete'
            else: 
                return f'phone "{phone}" is not defined'
        
        


@input_error
def show_all(book: AddressBook):
    result = [f"{record}" for _, record in book.data.items()]
    if result:
        return result
    else:
        return "Book is empty"

@input_error
def add_birthday(args, book: AddressBook):
    name, birthday_date = args
    record = book.find(name)
    if Birthday(birthday_date):
        record.add_birthday(birthday_date)
        return f'{birthday_date} added for name {name}'

@input_error
def show_birthday(name, book: AddressBook):
    record = book.find(name)
    if record:
        birthday = record.birthday.value
        return f'Birthday of {name} is {birthday}'
    return f'Birthday of {name} is not found'    

@input_error
def show_reminder(book):
    if book.get_upcoming_birthdays():
        return book.get_upcoming_birthdays()
    return 'No reminders for this week'


def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  


def main(): 
    '''
    The main function for launching an assistant bot.

    Accepts commands from the user and executes them.
    '''

    book = load_data()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_data(book)
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")        

        elif command == "add":                  
            print(add_contact(args, book))  

        
        elif command == "rm_contact":                  
            print(remove_record(args, book))  


        elif command == "rm_phone":                  
            print(remove_phone(args, book))  


        elif command == "change":               
            print(change_number(args, book))  

        elif command == "phone":               
            print(show_phones(args[0], book))

        elif command == "all":                  
            print(show_all(book))
            
        elif command == "add-birthday":         
            print(add_birthday(args, book))

        elif command == "show-birthday":        
            print(show_birthday(args[0], book))

        elif command == "birthdays":         
            print(show_reminder(book))


        else:
            print("Invalid command.")



if __name__ == "__main__":
    main()
