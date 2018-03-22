# Password Strength Calculator

This script check password strength using:
1. Length check: safe password must be more than 12 chars (score 5)
2. Numbers use check (score 2)
3. Lower and upper case check (score 2)
4. Special characters check (score 1)

Best possible score of password check is 10, worst is 0. 

You can specify black list url, to check if your password compromised. 

You can use compromised passwords lists from [danielmiessler / SecLists](https://github.com/danielmiessler/SecLists/tree/master/Passwords) repository

For example:
```
https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt
```

# Quickstart

When you run this script, you will be promted to enter password to check. 

You can specify blacklist url with parameter -b or --blacklist
If blacklist url is empty string, program will skip blacklist check.

Example of script launch on Linux, Python 3.5:

```
$ python3 password_strength.py -b https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt
input password to check:
password strength: 0

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
