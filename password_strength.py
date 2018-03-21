from urllib import request
import argparse
import sys
import getpass


def get_password_strength(password, black_list_url):
    strength = 0
    in_black_list_score = 0
    length_score = 5
    numbers_score = 2
    both_cases_score = 2
    special_characters_score = 1

    if black_list_url and is_in_black_list(black_list_url, password):
        return in_black_list_score

    if is_safe_length(password):
        strength += length_score
    if has_numbers(password):
        strength += numbers_score
    if has_lower_and_upper_case(password):
        strength += both_cases_score
    if has_special_characters(password):
        strength += special_characters_score
    return strength


def is_safe_length(password):
    wiki_password_length_recommendation = 12
    return len(password) > wiki_password_length_recommendation


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


def get_black_list(blacklist_url):
    stream = request.urlopen(blacklist_url)
    blacklist_content = stream.read().decode("utf-8")
    return blacklist_content.strip().splitlines()


def is_in_black_list(url, password):
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
        dest="blacklist_url",
        help="link to list of forbidden passwords"
    )
    return parser.parse_args()


def get_password():
    password = getpass.getpass("input password to check:")
    if not password.strip():
        return None
    return password


def get_black_list_url(blacklist):
    if blacklist is None:
        blacklist = input("input blacklist file url: ")
        if not password.strip():
            return None
    return blacklist


if __name__ == "__main__":
    args = get_args()

    password = args.password
    if password is None:
        password = get_password()
    if password is None:
        sys.exit("password expected")

    blacklist_url = args.blacklist_url
    password_strength = get_password_strength(password, args.blacklist_url)
    print("password strength: {0}".format(str(password_strength)))
