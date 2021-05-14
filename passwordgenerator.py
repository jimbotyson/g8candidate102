#!/usr/bin/env python3
from argparse import ArgumentParser
from random import randint
import sys

# We're going to give each digit, uppercase character, and lowercase character
# a unique number. ASCII codes already have this covered
# See http://www.asciitable.com/

DIGITS = list(range(48,58)) # range counts up to, but does not include the end value
UPPERCASE = list(range(65,91))
LOWERCASE = list(range(97,123))

def generate_password(password_length:int=10,
                      use_digits=True,
                      use_upper=True,
                      use_lower=True):
    # validate the inputs
    if not isinstance(password_length, int):
        raise ValueError("password_length must be an integer value")
    elif password_length < 1:
        raise ValueError("password length cannot be less than 1")
    # don't allow all character types to be set to False
    if not any([use_digits,use_upper,use_lower]):
        raise ValueError("no characters available to choose from")
    # create the list of characters to choose from
    ascii_list = []
    if use_digits: ascii_list += DIGITS
    if use_upper: ascii_list += UPPERCASE
    if use_lower: ascii_list += LOWERCASE
    ascii_list_length = len(ascii_list)
    # Randomly select character codes from ascii_list and store them in char_codes
    # Do this 'password_length' times
    char_codes = []
    for i in range(0,password_length):
        char_code = ascii_list[randint(0,ascii_list_length-1)] # randint does include end value
        char_codes.append(char_code)
    # map chr() function to list of character codes to convert them
    password_characters = map(chr,char_codes)
    # convert the list to a string and return the result
    return ''.join(password_characters)

if __name__=='__main__':
    parser = ArgumentParser(
        description='Password generator',
        usage='''python3 genpw.py [<args>]

-n          Number of characters
--nodigits Do not use digits
--noupper  Do not use upper-case characters
--nolower  Do not use lower-case characters
''')
    parser.add_argument('-n','--number',
                        help='Number of characters')
    parser.add_argument('--nodigits', action='store_true', default=False,
                        help='Do not include digits')
    parser.add_argument('--noupper', action='store_true', default=False,
                        help='Do not include uppercase')
    parser.add_argument('--nolower', action='store_true', default=False,
                        help='Do not include lowercase')
    args = parser.parse_args(sys.argv[1:])
    kwargs = {}
    if args.number: kwargs['password_length'] = int(args.number)
    if args.nodigits: kwargs['use_digits'] = False
    if args.noupper: kwargs['use_upper'] = False
    if args.nolower: kwargs['use_lower'] = False
    print(generate_password(**kwargs))