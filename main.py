import random
dlina = 11
simvole="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
password = "".join(random.sample(simvole,dlina))
print(password)
