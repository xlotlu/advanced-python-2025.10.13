# iterators

iterable = ["aa", "bb", "cc"]

# un for ...
for elem in iterable:
    print(elem)

# ... este echivalent cu:
_it = iter(iterable)

while True:
    try:
        elem = next(_it)
    except StopIteration:
        break
    
    print(elem)



# un iterator scris cu clase
# implementează metodele....

class MyIterator:
    def __iter__(self):
        return self

    def __next__(self):
        raise StopIteration


# scrieți un iterator class-based
# care se inițializează cu numerele `min` și `max`
#
# și când este iterat, returnează un număr random
# între `min` și `max`
# la nesfârșit

from random import randint

class RandIterator:
    def __init__(self, min_val, max_val):
        self.min = min_val
        self.max = max_val
    
    def __iter__(self):
        return self

    def __next__(self):
        return randint(self.min, self.max)
        #raise StopIteration

from time import sleep
counter = 5
for elem in RandIterator(5, 10):
    print(elem)
    sleep(.5)
    counter -= 1

    if not counter:
        break


for idx, elem in enumerate(RandIterator(5, 10)):
    print(elem)
    sleep(.5)

    if idx >= 4:
        break


# modificați iteratorul de mai sus
# pentru a primi parametrul opțional `count`


class RandIterator:
    def __init__(self, min_val, max_val, count=None):
        self.min = min_val
        self.max = max_val

        self.count = count
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.count is None:
            return randint(self.min, self.max)
        
        # else, this is numeric
        elif self.count:
            self.count -= 1
            return randint(self.min, self.max)
        
        else:
            raise StopIteration


# function-based iterators

def funciter():
    # » STOP 1 «

    print("am intrat în func")
    yield "A"
    # » STOP 2 «

    print("am returnat A, continui")
    yield "B"
    # » STOP 3 «

    print("am returnat B, continui")
    yield "C"
    # » STOP 4 «

    print("am returnat C, termin execuția")
    # » HARD EXIT «



# scrieți un function-based iterator
# ce primind o listă de numere
# generează pătratul acestora

def gensquares(numlist):
    for num in numlist:
        yield num ** 2

for x in gensquares(range(6)):
    print(x)