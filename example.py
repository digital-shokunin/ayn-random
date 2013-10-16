from aynrandom import aynrandom, genprime

__author__ = 'David Mitchell'


for i in range(1, 100):
    number = aynrandom.randint(1, 50000)
    if genprime.isPrime(number):
        print "Prime: " + str(number)
    else:
        print "NOT Prime: " + str(number)

#Pick the numbers you think are better
better_numbers = [13, 7, 42, 69, 9000]
for i in range(1, 100):
    number = aynrandom.randint(1, 50000, better_numbers)
    print number