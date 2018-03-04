import urllib.request
import argparse
import sys


def get_password_strength(password):
    strength = 0
    if is_in_black_list(password):
        return 0
    if is_safe_length(password):
        strength += 5
    if has_numbers(password):
        strength += 2
    if has_lower_and_upper_case(password):
        strength += 2
    if has_special_characters(password):
        strength += 1
    return strength


def is_safe_length(password):
    return len(password) > 12


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


def get_black_list(black_list_url):
    txt = urllib.request.urlopen(black_list_url).read().decode("utf-8")
    arr = txt.strip().splitlines()
    return arr


def is_in_black_list(password):
    url = get_black_list_url()
    if not url:
        return False
    black_list = get_black_list(url)
    for bad_password in black_list:
        if password == bad_password:
            return True
    return False


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p",
        "--password",
        dest="password",
        help="password to check"
    )
    parser.add_argument(
        "-b",
        "--blacklist",
        dest="blacklist",
        help="list of forbidden passwords"
    )
    return parser.parse_args()


def get_password():
    args = get_args()
    password = args.password
    if password is None:
        password = input("input password to check: ")
        if not password.strip():
            return None
    return password


def get_black_list_url():
    args = get_args()
    blacklist = args.blacklist
    if blacklist is None:
        blacklist = input("input blacklist file url: ")
        if not password.strip():
            return None
    return blacklist


if __name__ == "__main__":
    password = get_password()
    if password is None:
        sys.exit("password expected")
    password_strength = get_password_strength(password)
    print("password strength: {0}".format(str(password_strength)))
