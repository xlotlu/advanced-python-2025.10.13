# 1. folosind `class Point`, scrieți un function-based iterator
#    inițializat cu (min_x, max_x, min_y, max_y)
#    ce generează infinit puncte

import random
from point import Point

def pointgen(min_x, max_x, min_y, max_y):
    while True:
        x = random.randint(min_x, max_x)
        y = random.randint(min_y, max_y)
        yield Point(x, y)

# 2. scrieți un generator expression
#    ce primește ca argument iteratorul de mai sus
#    și generează pe baza elementelor distanța lor de la origine.

distances = (
    p.distance_from_origin
    for p in pointgen(1, 100, 1, 100)
)

# 2.1. testați-l iterând cu for în el
#      și folosind enumerate, opriți-vă 
#      după a 10a iterație

for idx, dist in enumerate(distances):
    print(dist)

    if idx > 10:
        break


# 3. scriem un class-based iterator
#    ce procesează în batch-uri.
# 
#    wrapper în jurul lui `distances`
#    
#    și generează average pentru fiecare
#    10 data-point-uri.

"""
current_batch = []
for _ in range(10):
    value = next(distances)
    current_batch.append(value)

yield average(current_batch)
"""

# rezultă un iterator ce returnează un element
# la fiecare 10 elemente ingerate

class BatchAverage:
    def __init__(self, iterable, batch_size=10):
        self.source = iterable
        self.batch_size = batch_size

    def __iter__(self):
        return self

    def __next__(self):
        batch = []

        for idx, elem in enumerate(self.source, start=1):
            batch.append(elem)

            if idx == self.batch_size:
                break

        #print(batch)
        return sum(batch) / len(batch)

        #raise StopIteration

from time import sleep

for idx, elem in enumerate(
       BatchAverage(distances)
):
    print(elem)
    sleep(.1)

    if idx > 20:
        break
