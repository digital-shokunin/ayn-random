__author__ = 'David Mitchell'

#import math
import random
import genprime


def aynrandom(start, stop, numbers=[]):
    if not numbers:
        for number in genprime.genPrimes():
            if number > stop:
                break
            elif number > start:
                numbers.append(number)

    random.seed()
    bitwheel = random.random()  # roll the big wheel
    if bitwheel < 0.01:  # Favor the 1%, only they get truly random numbers
        return random.randint(start, stop)
    elif bitwheel > 0.1:  # the 99% only get the prime (intrinsically better) numbers
        return numbers[random.randint(0, len(numbers))]

if __name__ == '__main__':
    pass
