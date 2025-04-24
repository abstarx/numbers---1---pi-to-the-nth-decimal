import math


pi_value = math.pi

print(math.pi)

x = input("how many decimal places do you want pi to be?")
x = int(x)
pi_value = round(pi_value, x)   
print(f"pi to {x} decimal places is {pi_value}")
