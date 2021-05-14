# g8candidate 102
A simple demonstration program in Python

## Usage
By default generate_password generates a 10 character password containing a mix of uppercase, lowercase and digits.
```
>>> from passgen import generate_password
>>> generate_password()
'4it8p7eKcN'
```
Pass an integer as an argument to change the password length.
```
>>> generate_password(16)
'sfp25SrTzVv5siP4'
```
Set `use_digits`, `use_upper`, `use_lower` to false to remove those characters.
```
>>> generate_password(use_lower=False)
'LQL4BQHZ2J'
```

## Author
[Tom Couch](mailto:t.couch@ucl.ac.uk)
