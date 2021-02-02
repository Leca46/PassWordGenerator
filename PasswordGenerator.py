import random

lowen = "abcdefghijklmnopqrstuvwxyz"
uppen = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{]();/,_-"

all = lowen + uppen + numbers + symbols

length = 16
password = "".join(random.sample(all,length))
print(password)
