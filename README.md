# g8candidate 102
A simple demonstration program in Python

## Usage
By default [passgen.py](./passgen.py) generates a 10 character password containing a mix of uppercase, lowercase and digits.
### As a function
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
Set `digits`, `uppercase`, `lowercase` to false to remove those characters.
```
>>> generate_password(lowercase=False)
'LQL4BQHZ2J'
```
### From the command line
```
$ python passgen.py --help
usage: python3 genpw.py <args>

Password generator

optional arguments:
  -h, --help            show this help message and exit
  -n NUMBER, --number NUMBER
                        Number of characters
  --nodigits            Do not include digits
  --noupper             Do not include upper-case characters
  --nolower             Do not include lower-case characters
$ python passgen.py -n 8 --nolower
TEW2SOHP
```

## Version
1.0

## Author
[Tom Couch](mailto:t.couch@ucl.ac.uk)
