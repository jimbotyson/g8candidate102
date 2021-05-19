#!/usr/bin/env python3
from argparse import ArgumentParser
from random import sample
from string import digits as ascii_digits, ascii_uppercase, ascii_lowercase
import sys

def generate_password(password_length:int=10,
                      digits=True,
                      uppercase=True,
                      lowercase=True):
    # validate the inputs
    if not isinstance(password_length, int):
        raise ValueError("password_length must be an integer value")
    elif password_length < 1:
        raise ValueError("password length cannot be less than 1")
    # don't allow all character types to be set to False
    if not any([digits,uppercase,lowercase]):
        raise ValueError("no characters available to choose from")
    # create the list of characters to choose from
    character_list = []
    if digits: character_list += ascii_digits
    if uppercase: character_list += ascii_uppercase
    if lowercase: character_list += ascii_lowercase
    # Take a random sample from character list of the requested length
    password_characters = sample(character_list, password_length)
    # convert the list to a string and return the result
    return ''.join(password_characters)

if __name__=='__main__':
    parser = ArgumentParser(
        description='Password generator',
        usage='python3 genpw.py <args>')
    parser.add_argument('-n','--number',
                        help='Number of characters')
    parser.add_argument('--nodigits', action='store_true', default=False,
                        help='Do not include digits')
    parser.add_argument('--noupper', action='store_true', default=False,
                        help='Do not include upper-case characters')
    parser.add_argument('--nolower', action='store_true', default=False,
                        help='Do not include lower-case characters')
    args = parser.parse_args(sys.argv[1:])
    kwargs = {}
    if args.number: kwargs['password_length'] = int(args.number)
    if args.nodigits: kwargs['digits'] = False
    if args.noupper: kwargs['uppercase'] = False
    if args.nolower: kwargs['lowercase'] = False
    print(generate_password(**kwargs))