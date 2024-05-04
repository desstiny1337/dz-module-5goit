def input_error(message_type):
    def decorator(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError:
                if message_type == 'error_type_1':
                    return 'Give me name and phone please'
                elif message_type == 'error_type_2':
                    return 'Contact or phone number already entered'
            except KeyError:
                if message_type == 'error_type_1':
                    return 'Contact does not exist'
                elif message_type == 'error_type_2':
                    return 'No contacts found'
            except IndexError:
                if message_type == 'error_type_1':
                    return 'Invalid nums of args'

        return inner
    return decorator

@input_error('error_type_2')
def parse_input(user_input):
    # Dividing line to command and arguments
    # try:
        parts = user_input.strip().lower().split()
        if not parts:
            raise ValueError('Invalid command format')
        command = parts[0]
        args = parts[1:]
        return command, args
    # except ValueError:
    #     raise ValueError('Invalid command format')


@input_error('error_type_1')
def add_contact(args, contacts):
    name, phone_number = args
    if phone_number in contacts.values() or name in contacts:
        raise ValueError
    # Add a new contact to dictionary contacts
    contacts[name] = phone_number
    return "Contact added."

@input_error('error_type_1')
def change_contact(args, contacts):
    name, new_phone_number = args
    #  Changing already existing number
    if name not in contacts:
        raise KeyError
    contacts[name] = new_phone_number
    return 'Contact changed.'


@input_error('error_type_1')
def show_phone(args, contacts):
    name = args[0]
    # Displaying number for contact
    if name not in contacts:
        raise KeyError
    return contacts[name]

@input_error('error_type_1')
def show_all(contacts):
    # Displaying all numbers of contacts
    if not contacts:
        raise KeyError
    else:
        cont_info = "\n".join(f"{name}: {phone_number}" for name, phone_number in contacts.items())
        return cont_info

def main():
    contacts = {}  # Dict for contacts

    print("How can I help you?")

    while True:
        user_input = input("> Enter a command: ")

        # Parsing of entered string(line)
        command, args = parse_input(user_input)

        # Processing of various commands
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()