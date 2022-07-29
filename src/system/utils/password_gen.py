from random import choice
from string import (
    ascii_lowercase,
    ascii_uppercase,
    punctuation,
    digits
)
from hashlib import sha256
from time import sleep


str_set = [
        ascii_lowercase,
        ascii_uppercase,
        punctuation,
        digits
    ]
password = "".join([choice(choice(str_set)) for x in range(32)])

for n in range(10):
    print(f"Your password is: {password}\nRemoving in {10-n}", end="\r")
    sleep(1)

print(
    sha256(password.encode("utf-8")).hexdigest()
)
