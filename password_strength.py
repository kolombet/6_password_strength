import urllib.request


def get_password_strength(password):
    if not has_numbers(password):
        return False
    if not is_lower_and_upper_case(password):
        return False
    return True


def has_lower_and_upper_case(password):
    return not password.islower() and not password.isupper()


def has_numbers(password):
    return any(char.isdigit() for char in password)


def has_special_characters(password):
    special = "@#$"
    for char in special:
        if char in password:
            return True
    return False


def get_black_list():
    target_url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/10_million_password_list_top_1000.txt"
    txt = urllib.request.urlopen(target_url).read().decode("utf-8")
    arr = txt.strip().splitlines()
    print(arr[0])
    return arr


def is_in_black_list(password):
    black_list = get_black_list()
    for bad_password in black_list:
        if password == bad_password:
            return True
    return False


if __name__ == "__main__":
    # is_secure = get_password_strength("Qwerty1")
    password = "12345dsf678"
    # is_secure = has_special_characters(password)
    is_secure = not is_in_black_list(password)
    print("secure" if is_secure else "not secure")
