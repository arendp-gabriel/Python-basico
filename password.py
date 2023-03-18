import random
lower: str = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = '0123456789'
symbol = '!@#$%^&*().'

string = lower + upper + numbers + symbol
length = 16
password = "".join(random.sample(string,length))
print("Sua senha é: " + password)
