from aynrandom import aynrandom, genprime

__author__ = 'David Mitchell'


for i in range(1, 100):
    number = aynrandom(1, 50000)
    if genprime.isPrime(number):
        print "Is prime: " + str(number)
    else:
        print "NOT PRIME: " + str(number)
