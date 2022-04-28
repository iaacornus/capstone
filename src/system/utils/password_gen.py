import random
import string

print(''.join([random.choice(random.choice([string.ascii_lowercase, string.ascii_uppercase, string.punctuation, string.digits])) for x in range(32)]))
