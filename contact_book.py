def print_intro():
    print("Simple Contact Book")


def main():
    print_intro()
    print()
    print(f'To add new contact, type "add"', "\n"
          f'To edit or update contacts, type "edit"', "\n"
          f'To search for contacts, type "search"', "\n"
          f'To view or list details of contacts, type "view"', "\n"
          f'To delete existing contacts, type "delete"', "\n"
          f'To end program execution, type "end"', "\n")

    user_input = ""
    valid_inputs = ["add", "edit", "delete", "view", "search", "end"]
    contact_book = []
    person_details = {"name": "", "phoneNumber": "", "address": "", "emailAddress": ""}

    # Program starts
    while user_input != "end":
        user_input = input("> ").lower()

        # User input validation
        if user_input not in valid_inputs:
            print("Error‼️ -- > Invalid command")

        if user_input == "add" or user_input == "edit" or user_input == "delete" or \
                user_input == "view" or user_input == "search":

            # Add contacts
            if user_input == "add":
                add_input = input("How many contacts do you want to add? > ")
                if add_input.isdigit():
                    for i in range(1, int(add_input) + 1):
                        contact_details = input(f"Enter contact details of contact {i} > ").split('-')

                        person_details["name"], person_details["phoneNumber"], person_details["address"], \
                            person_details["emailAddress"] \
                            = contact_details[0], contact_details[1], contact_details[2], contact_details[3]
                        contact_book.append(person_details)
                        person_details = {}
                else:
                    print("Error‼️-- > Please enter a number, number cannot be less or equal to zero")

            # View contacts
            if user_input == "view":
                if contact_book == [] or contact_book == 0:
                    print("Contact book empty.")
                for i in contact_book:
                    print(i)
                print("\n"f'Number of contacts : {len(contact_book)}')

            # Edit contacts
            if user_input == "edit":
                while True:
                    name = input("Enter name to edit (Hit <Enter> to skip) > ")
                    new_name = input("Enter new name (Hit <Enter> to skip) > ")
                    if name != "" and new_name != "":
                        for i in range(0, len(contact_book)):
                            if contact_book[i]["name"].lower() == name.lower():
                                for key in contact_book[i].keys():
                                    if key == "name":
                                        contact_book[i][key] = new_name

                    name_for_number_change = input(
                        "Enter name of person for number change (Hit <Enter> to skip) > ")
                    new_phone_number = input("Enter new phone number (Hit <Enter> to skip) > ")
                    if name_for_number_change != "" and new_phone_number != "":
                        for i in range(0, len(contact_book)):
                            if contact_book[i]["name"].lower() == name_for_number_change.lower():
                                for key in contact_book[i].keys():
                                    if key == "phoneNumber":
                                        contact_book[i][key] = new_phone_number

                    name_for_address_change = input(
                        "Enter name of person for address change (Hit <Enter> to skip) > ")
                    new_address = input("Enter new address (Hit <Enter> to skip) > ")
                    if name_for_address_change != "" and new_address != "":
                        for i in range(0, len(contact_book)):
                            if contact_book[i]["name"].lower() == name_for_address_change.lower():
                                for key in contact_book[i].keys():
                                    if key == "address":
                                        contact_book[i][key] = new_address

                    name_for_email_address_change = input(
                        "Enter name of person for email address change (Hit <Enter> to skip) > ")
                    new_email_address = input("Enter new email address (Hit <Enter> to skip) > ")
                    if name_for_email_address_change != "" and new_email_address != "":
                        for i in range(0, len(contact_book)):
                            if contact_book[i]["name"].lower() == name_for_email_address_change.lower():
                                for key in contact_book[i].keys():
                                    if key == "emailAddress":
                                        contact_book[i][key] = new_email_address

                    close = input("Do you want to exit? (y/n) > ")
                    if close.lower() == "y" or close.lower() == "yes":
                        break

            # Search contacts
            if user_input == "search":
                name_to_search = input("Enter name of person you want to find > ").lower()
                split_name = name_to_search.split()
                full_name = []

                if len(split_name) == 1:
                    for i in range(0, len(contact_book)):
                        if contact_book[i]["name"].lower() == name_to_search:
                            print(contact_book[i])
                        if contact_book[i]["name"].lower() != name_to_search:
                            continue
                        break
                    else:
                        matched_names_list = []
                        for i in range(0, len(contact_book)):
                            if name_to_search in contact_book[i]["name"].lower():
                                if contact_book[i] not in matched_names_list:
                                    matched_names_list.append(str(contact_book[i]))
                        if len(matched_names_list) == 0:
                            print("No such contact")
                        else:
                            matched_names_text = "\n".join(matched_names_list)
                            print(matched_names_text)

                if len(split_name) == 2:
                    full_name = " ".join(split_name)
                    for i in range(0, len(contact_book)):
                        if contact_book[i]["name"].lower() == full_name.lower():
                            print(contact_book[i])
                        if contact_book[i]["name"].lower() != full_name.lower():
                            continue
                        break
                    else:
                        matched_names_list = []
                        for i in range(0, len(contact_book)):
                            first_name, second_name = split_name[0], split_name[1]
                            if first_name.lower() in contact_book[i]["name"].lower() \
                                    or second_name.lower() in contact_book[i]["name"].lower():
                                if contact_book[i] not in matched_names_list:
                                    matched_names_list.append(str(contact_book[i]))
                        if len(matched_names_list) == 0:
                            print("No such contact")
                        else:
                            matched_names_text = "\n".join(matched_names_list)
                            print(matched_names_text)

                if len(split_name) == 3:
                    full_name = " ".join(split_name)
                    for i in range(0, len(contact_book)):
                        if contact_book[i]["name"].lower() == full_name.lower():
                            print(contact_book[i])
                        if contact_book[i]["name"].lower() != full_name.lower():
                            continue
                        break
                    else:
                        matched_names_list = []
                        for i in range(0, len(contact_book)):
                            first_name, middle_name, last_name = split_name[0], split_name[1], split_name[2]
                            if first_name.lower() in contact_book[i]["name"].lower() \
                                    or middle_name.lower() in contact_book[i]["name"].lower() \
                                    or last_name.lower() in contact_book[i]["name"].lower():
                                if contact_book[i] not in matched_names_list:
                                    matched_names_list.append(str(contact_book[i]))
                        if len(matched_names_list) == 0:
                            print("No such contact")
                        else:
                            matched_names_text = "\n".join(matched_names_list)
                            print(matched_names_text)

            # Delete contacts
            if user_input == "delete":
                if contact_book == [] or len(contact_book) == 0:
                    print("Contact book empty.")
                else:
                    delete_name = input("Enter name to delete > ").lower()
                    for i in range(0, len(contact_book)):
                        if contact_book[i]["name"].lower() == delete_name:
                            del contact_book[i]
                            print("Successfully deleted ✅")
                            break
                    else:
                        print("< Name not found, deletion unsuccessful >")

    # Program ends
    else:
        print("Program ended")


main()
