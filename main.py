import random
dlina = 11
simvole="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890"
password = "".join(random.sample(simvole,dlina))
print(password)
