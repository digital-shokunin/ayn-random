__author__ = 'David Mitchell'

import random
import genprime


def randint(start, stop, numbers=[]):
    """Returns a random integer between the range of the first two numbers provided
    as parameters.
    
    Optional third parameter can be an array of numbers that are "intrinsically better", 
    otherwise, prime numbers are considered intrinsically better.
    """
    if not numbers:
        for number in genprime.genPrimes():
            if number > stop:
                break
            elif number > start:
                numbers.append(number)

    random.seed()
    bitwheel = random.random()  # roll the big wheel
    if bitwheel <= 0.01:  # Favor the 1%, only they get truly random numbers
        return random.randint(start, stop)
    elif bitwheel > 0.01:  # the 99% only get the prime (intrinsically better) numbers
        return numbers[random.randint(0, len(numbers)-1)]

if __name__ == '__main__':
    pass
