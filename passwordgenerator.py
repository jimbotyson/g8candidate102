from random import randint

# We're going to give each digit, uppercase character, and lowercase character
# a unique number. ASCII codes already have this covered
# See http://www.asciitable.com/

DIGITS = list(range(48,58)) # range counts up to, but does not include the end value
UPPERCASE = list(range(65,91))
LOWERCASE = list(range(97,123))

def generate_password():
    # create the list of characters to choose from
    ascii_list = DIGITS + UPPERCASE + LOWERCASE
    ascii_list_length = len(ascii_list)
    # Randomly select 10 character codes from ascii_list and store them in char_codes
    char_codes = []
    for i in range(0,10):
        char_code = ascii_list[randint(0,ascii_list_length-1)] # randint does include end value
        char_codes.append(char_code)
    # map chr() function to list of character codes to convert them
    password_characters = map(chr,char_codes)
    # convert the list to a string and return the result
    return ''.join(password_characters)