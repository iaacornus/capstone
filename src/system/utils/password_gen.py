import random
import string


str_set = [
    string.ascii_lowercase,
    string.ascii_uppercase,
    string.punctuation,
    string.digits
]

print(''.join([random.choice(random.choice(str_set)) for x in range(32)]))
