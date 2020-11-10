def new_contact_store():
    dictionary = {}
    return dictionary


def add_new_contact(contacts, first_name, last_name, email, phone_number,
                    birthday):
    dictionary = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone_number": phone_number,
        "birthday": birthday
    }
    return_list = []
    for contact in contacts:
        return_list.append(contact)
    return_list.append(dictionary)
    return return_list


def has_contact(contacts, first_name, last_name):
    for contact in contacts:
        if contact.get("first_name") == first_name:
            if contact.get("last_name") == last_name:
                return True
    return False


def get_contact_string(contacts, first_name, last_name):
    original_first, original_last, original_email,\
        original_phone, original_birthday = get_original_contact_values(
            contacts, first_name, last_name)
    return f"First Name: {original_first}\nLast Name: {original_last}\n"\
        f"Email: {original_email}\nPhone Number: {original_phone}\n"\
        f"Birthday: {original_birthday}"


def get_original_contact_values(contacts, first_name, last_name):
    for contact in contacts:
        if contact.get("first_name") == first_name:
            if contact.get("last_name") == last_name:
                original_first = contact.get("first_name")
                original_last = contact.get("last_name")
                original_email = contact.get("email")
                original_phone = contact.get("phone_number")
                original_birthday = contact.get("birthday")
    return original_first, original_last, original_email,\
        original_phone, original_birthday


def remove_contact(contacts, first_name, last_name):
    new_contacts = []
    for contact in contacts:
        if contact.get("first_name") == first_name:
            if contact.get("last_name") == last_name:
                pass
            else:
                new_contacts.append(contact)
        else:
            new_contacts.append(contact)
    return new_contacts


def update_contact_first_name(contacts, first_name,
                              last_name, new_field_value):
    _, original_last, original_email, original_phone,\
        original_birthday = get_original_contact_values(
            contacts, first_name, last_name)
    rem_contacts = remove_contact(contacts, first_name, last_name)
    new_contacts = add_new_contact(
        rem_contacts, new_field_value, original_last, original_email,
        original_phone, original_birthday)
    return new_contacts


def update_contact_last_name(contacts, first_name, last_name, new_field_value):
    original_first, _, original_email, original_phone,\
        original_birthday = get_original_contact_values(
            contacts, first_name, last_name)
    rem_contacts = remove_contact(contacts, first_name, last_name)
    new_contacts = add_new_contact(
        rem_contacts, original_first, new_field_value, original_email,
        original_phone, original_birthday)
    return new_contacts


def update_contact_email(contacts, first_name, last_name, new_field_value):
    original_first, original_last, _, original_phone, \
        original_birthday = get_original_contact_values(
            contacts, first_name, last_name)
    rem_contacts = remove_contact(contacts, first_name, last_name)
    new_contacts = add_new_contact(
        rem_contacts, original_first, original_last, new_field_value,
        original_phone, original_birthday)
    return new_contacts


def update_contact_phone_number(contacts, first_name,
                                last_name, new_field_value):
    original_first, original_last, original_email, _, \
        original_birthday = get_original_contact_values(
            contacts, first_name, last_name)
    rem_contacts = remove_contact(contacts, first_name, last_name)
    new_contacts = add_new_contact(
        rem_contacts, original_first, original_last, original_email,
        new_field_value, original_birthday)
    return new_contacts


def update_contact_birthday(contacts, first_name, last_name, new_field_value):
    original_first, original_last, original_email, original_phone, \
        _ = get_original_contact_values(
            contacts, first_name, last_name)
    rem_contacts = remove_contact(contacts, first_name, last_name)
    new_contacts = add_new_contact(
        rem_contacts, original_first, original_last, original_email,
        original_phone, new_field_value)
    return new_contacts
