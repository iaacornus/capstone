import random
import string

def main():
   return ''.join([random.choice(random.choice([string.ascii_lowercase, string.ascii_uppercase, string.punctuation, string.digits])) for x in range(32)])

if __name__ == "__main__":
    main()