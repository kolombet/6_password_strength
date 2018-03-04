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
https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/10_million_password_list_top_1000.txt
```

# Quickstart

When you run this script, you will be promted to enter password to check and blacklist url. If blacklist url is empty string, program will skip blacklist check.

You specify password with parameter -p or --password and you can specify blacklist url with parameter -b or --blacklist

Example of script launch on Linux, Python 3.5:

```$ python3 password_strength.py 
input password to check: Abracadabra1234
input blacklist file url: https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/10_million_password_list_top_1000.txt
password strength: 9


```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
