# Eric Jordan, Sharo Hawrami, Ollie Barwise
# Date: 04/10/19
# Class: Discrete Mathematics

import math as m

pc = 0
number = 1000000000
number = float(number)

while pc < 25:
    def prime_finder(n):
        if n % 2 == 0 and n > 2:
            return False
        else:
            return all(n % i for i in range(3, int(m.sqrt(n)) + 1, 2))

    number_truth = (prime_finder(number))  # prints first 25 confirmed primes
    if number_truth == True:
        print (number)

    if prime_finder(number) == True:
        pc += 1
    else:
        pc

    number += 1
    # print(pc)

print(pc)

prime_guess = float((2000000000 / m.log(20000000000)) - (1000000000 / m.log(10000000000)))
prime_guess = 45131377
print(prime_guess)


