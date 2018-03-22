from urllib import request
import argparse
import sys
import getpass
import string


def get_password_strength(password, blacklist):
    in_blacklist_score = 0
    length_score = 5
    numbers_score = 2
    both_cases_score = 2
    special_characters_score = 1

    if blacklist and is_in_blacklist(blacklist, password):
        return in_blacklist_score
        
    return sum([
        is_safe_length(password)*length_score,
        has_numbers(password)*numbers_score,
        has_lower_and_upper_case(password)*both_cases_score,
        has_special_characters(password)*special_characters_score
    ])


def is_safe_length(password):
    wiki_password_length_recommendation = 12
    return len(password) > wiki_password_length_recommendation


def has_lower_and_upper_case(password):
    return not password.islower() and not password.isupper()


def has_numbers(password):
    return any(char.isdigit() for char in password)


def has_special_characters(password):
    for char in string.punctuation:
        if char in password:
            return True
    return False


def get_blacklist(blacklist_url):
    try:
        stream = request.urlopen(blacklist_url)
        blacklist_content = stream.read().decode("utf-8")
        return blacklist_content.strip().splitlines()
    except ValueError:
        return None


def is_in_blacklist(blacklist, password):
    return password in blacklist


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-b",
        "--blacklist",
        dest="blacklist_url",
        help="link to list of forbidden passwords"
    )
    return parser.parse_args()


def get_password():
    password = getpass.getpass("input password to check:")
    if password.isspace():
        return None
    return password


if __name__ == "__main__":
    args = get_args()

    password = get_password()
    if password is None:
        sys.exit("password expected")

    blacklist_url = args.blacklist_url
    blacklist = []
    if blacklist_url:
        blacklist += get_blacklist(blacklist_url)
    
    if not blacklist:
        print("blacklist is empty, skipping list check")
        
    password_strength = get_password_strength(password, blacklist)
    print("password strength: {0}".format(password_strength))
