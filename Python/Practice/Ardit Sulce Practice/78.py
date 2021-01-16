import random

character = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
chosen = random.sample(character, 6)
password = "".join(chosen)
print(password)
