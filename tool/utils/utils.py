import getpass


def get_user_name():
    user_name = getpass.getuser()
    return user_name
