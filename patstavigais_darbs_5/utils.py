from user import User


def add_user(users, full_name, username, email):
    for i in users:
        if i.username == username or i.email == email:
            raise Exception("User with such username or e-mail already exists")

    user = User(full_name, username, email)
    users.append(user)


def delete_user_by_email(users, email):
    for user in users:
        if user.email == email:
            users.remove(user)
            return

    raise Exception("User not found")


def delete_user_by_username(users, username):
    for user in users:
        if user.username == username:
            users.remove(user)
            return

    raise Exception("User not found")


def get_user_by_email(users, email):
    for user in users:
        if user.email == email:
            return user

    raise Exception("User not found")


def get_user_by_username(users, username):
    for user in users:
        if user.username == username:
            return user

    raise Exception("User not found")
