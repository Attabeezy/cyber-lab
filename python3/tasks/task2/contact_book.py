"""
Basic Contact Book
- allows users to add, view, search, and delete contacts in a file
- stores contacts in a csv file
- each contact has name and phone Number

Logic:
- add contact
- view contacts
- search contacts
- delete contact
- exit program
"""

import csv
import os

contact_file = "contacts.csv"
fieldnames = ['Name', 'PhoneNumber']

def initialize_contact_file():
    """
    check if file exists, else create it
    """
    if not os.path.exists(contact_file):
        with open(contact_file, 'w') as file:
            write = csv.DictWriter(file, fieldnames=fieldnames)
            write.writeheader()
            return

def addContact(name, phoneNumber):
    """
    loads contact.csv an appends name and contact with write lines
    then prints contact has been added!
    """
    with open(contact_file, 'a') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({'Name': name, 'PhoneNumber': phoneNumber})
        print(f"Contact '{name}' added!")
        return

def viewContacts():
    """
    
    """
    with open(contact_file, 'r') as file:
        contacts = file.readlines()
        print("-" * 25)
        for index, name in enumerate(contacts, start=1):
            name, phone = name.strip().split(',')
            print(f"{index}. {name} -- {phone}")
        print("-" * 25)

def removeContact(contact_number):
    with open(contact_file, 'r') as file:
        contacts = file.readlines()
        
        if len(contacts) == 0:
            print("No contacts saved!")
            return
        
        if contact_number < 1 or contact_number > len(contacts):
            print("Invalid contact number")
            return
        
        removed = contacts[contact_number - 1]
        name, contact = removed.strip().split(',')
        contacts.pop(contact_number -1)
        with open(contact_file, 'w') as file:
            file.writelines(contacts)
            print(f"'{name.strip()}' removed!")

def quit():
    print("quitting....")
    exit()

def main():
    ## tasks inputs, logic check, etc
    while True:
        opt = input("Choose an option: add, view, remove, quit: ")
        if opt == "add":
            name = input("Enter contact name: ")
            phoneNumber = input("Enter phone number: ")
            addContact(name, phoneNumber)
        elif opt == "view":
            viewContacts()
        elif opt == "remove":
            viewContacts()
            contact_number = int(input("Enter contact number to remove: "))
            removeContact(contact_number)
        elif opt == "quit":
            quit()
        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()