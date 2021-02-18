import utils as utils

users = []

while True:
    print("Enter 1 to print information about user, 2 to add new user, 3 to delete user, 4 to quit")
    action = int(input("Your input: "))

    if action == 1:
        print("Enter 1 to search by e-mail 2 to search by username")
        get_by = int(input("Your input: "))

        try:
            if get_by == 1:
                email = input("Enter e-mail: ")
                user = utils.get_user_by_email(users=users,
                                               email=email)
                user.print_user()

            elif get_by == 2:
                username = input("Enter username: ")
                user = utils.get_user_by_username(users=users,
                                                  username=username)
                user.print_user()

        except Exception as exception:
            print(exception)

    elif action == 2:
        full_name = input("Full name: ")
        username = input("Username: ")
        email = input("E-mail: ")

        try:
            utils.add_user(users=users,
                           full_name=full_name,
                           username=username,
                           email=email)
            print("Added user")

        except Exception as exception:
            print(exception)

    elif action == 3:
        print("Enter 1 to delete by e-mail 2 to delete by username")
        delete_by = int(input("Your input: "))

        try:
            if delete_by == 1:
                email = input("Enter e-mail: ")
                user = utils.delete_user_by_email(users=users,
                                                  email=email)
            elif delete_by == 2:
                username = input("Enter username: ")
                user = utils.delete_user_by_username(users=users,
                                                     username=username)

            print("Removed user")

        except Exception as exception:
            print(exception)
    elif action == 4:
        quit()

    print("")
