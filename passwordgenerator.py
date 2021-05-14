from random import randint

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
    # validate the password_length
    if not isinstance(password_length, int):
        raise ValueError("password_length must be an integer value")
    elif password_length < 1:
        raise ValueError("password length cannot be less than 1")
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