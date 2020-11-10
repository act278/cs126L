import os
import json
import contact_lib as contact_store

VERSION_NUMBER = 'v1.3.7'

CONTACT_DATA_FILE_PATH = 'contact_data.json'

FIRST_NAME = "first name"
LAST_NAME = "last name"
EMAIL = "email"
PHONE_NUMBER = "phone number"
BIRTHDAY = "birthday"


def main():
    display_boot_message()
    contacts = load_or_create_contact_store()
    contacts = begin_user_interaction(contacts)
    save_contact_store(contacts)
    display_exit_message()


def display_boot_message():
    print(f"Welcome to Kontact Keeper {VERSION_NUMBER}!")
    print("Please report any issues via e-mail to bugs@kontact_keeper.net\n")


def load_or_create_contact_store():
    print("Attempting to load existing contact data...")

    if os.path.exists(CONTACT_DATA_FILE_PATH):
        with open(CONTACT_DATA_FILE_PATH, 'r') as contact_data_file:
            contacts = json.load(contact_data_file)
        print("\tExisting contact data loaded.\n")
    else:
        print("\tNo contact data found; starting fresh!\n")
        contacts = contact_store.new_contact_store()

    return contacts


def begin_user_interaction(contacts):
    user_action = prompt_for_action(first_time=True)
    print()  # Add empty line

    while user_action != 'q':
        contacts = execute(user_action, contacts)
        print()
        user_action = prompt_for_action()
        print()

    return contacts


def save_contact_store(contacts):
    print("Saving your contact data; please do not exit the program...")
    with open(CONTACT_DATA_FILE_PATH, 'w') as contact_data_file:
        json.dump(contacts, contact_data_file)
    print("\tContact data saved!\n")


def display_exit_message():
    print("Thank you for using Kontact Keeper!\n\n")


def prompt_for_action(first_time=False):
    print(f"What would you like to do{'' if first_time else ' next'}?")
    print("\t(c)reate contact")
    print("\t(v)iew contact")
    print("\t(d)elete contact")
    print("\t(u)pdate contact")
    print("\t(q)uit\n")

    if first_time:
        print("Type the letter in parentheses for your desired option, " +
              "then hit enter.\n")

    return input().lower()


def execute(user_action, contacts):
    if user_action not in ['c', 'v', 'd', 'u', 'q']:
        print(f"I'm sorry, {user_action} is not a valid choice.")
        return contacts

    # TODO: Make this better.  I want to use a dictionary instead of a bunch of
    #       if-elif's, but I'm not sure how to store a *behavior* as a value in
    #       a dictionary so it can be looked up and then carried out...
    if user_action == 'c':
        contacts = create_new_contact(contacts)
    elif user_action == 'v':
        contacts = view_contact(contacts)
    elif user_action == 'd':
        contacts = delete_contact(contacts)
    elif user_action == 'u':
        contacts = update_contact(contacts)
    # I don't think this ever happens because of the way the while-loop that
    # calls this function is structured, but just in case...
    elif user_action == 'q':
        print("Quitting...\n")

    return contacts


def create_new_contact(contacts):
    first_name = prompt_for_value_for_field(FIRST_NAME)
    last_name = prompt_for_value_for_field(LAST_NAME)
    email = prompt_for_value_for_field(EMAIL)
    phone_number = prompt_for_value_for_field(PHONE_NUMBER)
    birthday = prompt_for_value_for_field(BIRTHDAY)

    print("Creating a new contact...")
    contacts = contact_store.add_new_contact(contacts, first_name, last_name,
                                             email, phone_number, birthday)
    print("\tDone!\n")
    return contacts


def view_contact(contacts):
    first_name = prompt_for_value_for_field(FIRST_NAME)
    last_name = prompt_for_value_for_field(LAST_NAME)
    if not contact_store.has_contact(contacts, first_name, last_name):
        print("\nSorry, there doesn't seem to be any data for " +
              f"{first_name} {last_name} in your records.")
    else:
        print()
        print(contact_store.get_contact_string(contacts, first_name,
                                               last_name))
    return contacts


def delete_contact(contacts):
    first_name = prompt_for_value_for_field(FIRST_NAME)
    last_name = prompt_for_value_for_field(LAST_NAME)

    if not contact_store.has_contact(contacts, first_name, last_name):
        print("Sorry, there doesn't seem to be any data for " +
              f"{first_name} {last_name} in your records.")
        return contacts

    print("Are you sure you want to delete this contact:")
    print(contact_store.get_contact_string(contacts, first_name, last_name))

    if input("y/n: ") == "y":
        print("\nDeleting...")
        return contact_store.remove_contact(contacts, first_name, last_name)
        print("Done!")
    else:
        print("\nDeletion discontinued.")
        return contacts


def update_contact(contacts):
    first_name = prompt_for_value_for_field(FIRST_NAME)
    last_name = prompt_for_value_for_field(LAST_NAME)

    if not contact_store.has_contact(contacts, first_name, last_name):
        print("\nSorry, there doesn't seem to be any data for " +
              f"{first_name} {last_name} in your records.")
        return contacts

    print(contact_store.get_contact_string(contacts, first_name, last_name))

    # TODO: This is the same issue as the other TODO except this time the only
    #       thing changing for each case is which method to call instead of
    #       which function. I really need to ask someone about this, the
    #       copy-paste is making me nervous...
    field_to_update = prompt_for_field_choice()
    new_field_value = prompt_for_value_for_field(field_to_update)
    if field_to_update == FIRST_NAME:
        contacts = contact_store.update_contact_first_name(contacts,
                                                           first_name,
                                                           last_name,
                                                           new_field_value)
    elif field_to_update == LAST_NAME:
        contacts = contact_store.update_contact_last_name(contacts,
                                                           first_name,
                                                           last_name,
                                                           new_field_value)
    elif field_to_update == EMAIL:
        contacts = contact_store.update_contact_email(contacts,
                                                      first_name,
                                                      last_name,
                                                      new_field_value)
    elif field_to_update == PHONE_NUMBER:
        contacts = contact_store.update_contact_phone_number(contacts,
                                                             first_name,
                                                             last_name,
                                                             new_field_value)
    elif field_to_update == BIRTHDAY:
        contacts = contact_store.update_contact_birthday(contacts,
                                                         first_name,
                                                         last_name,
                                                         new_field_value)
    return contacts


def prompt_for_value_for_field(field_name):
    return input(f"Please enter a(n) {field_name}:\n\t")


def prompt_for_field_choice():
    menu_selections_to_field_names = {
        'f': FIRST_NAME,
        'l': LAST_NAME,
        'e': EMAIL,
        'p': PHONE_NUMBER,
        'b': BIRTHDAY,
    }

    field_choice = None
    while field_choice not in menu_selections_to_field_names:
        print(f"Which field would you like to do update?")
        print("\t(f)irst name")
        print("\t(l)ast name")
        print("\t(e)mail address")
        print("\t(p)hone number")
        print("\t(b)irthday\n")
        field_choice = input()
        print()

    return menu_selections_to_field_names[field_choice]


if __name__ == '__main__':
    main()
