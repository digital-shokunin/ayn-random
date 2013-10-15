from aynrandom import aynrandom, genprime

__author__ = 'David Mitchell'


for i in range(1, 100):
    number = aynrandom(1, 50000)
    if number == None:
        print "NONE"
    elif genprime.isPrime(number):
        print "Is prime"
    else:
        print "NOT PRIME"
