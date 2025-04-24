import math


pi_value = (math.pi)

#print(math.pi)

#x = input("how many decimal places do you want pi to be?")
#x = int(x)
#pi_value = round(pi_value, x)   
#print(f"pi to {x} decimal places is {pi_value}")

#  the code above is just what happens when i press tab without typing anything myself
#  the code below is what i typed myself
# i want to be able to t oround pi to n decimal places, where n is a number i input
#  the code below is what i typed myself  


def pi_to_n_decimal_places(n):
    pi_value = round(math.pi, n)
    return pi_value

n = int(input("Enter the number of decimal places for pi: "))
pi_value = pi_to_n_decimal_places(n)
print(f"Pi to {n} decimal places is: {pi_value}")
