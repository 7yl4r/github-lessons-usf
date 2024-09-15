import random
import string


while True:
    input()
    letter = random.choice(string.ascii_uppercase)
    print(f"\nI am sensing a name starting with '\033[1m{letter}\033[0m'...")
