# !CONCEPT _1_!
# o funcție este un obiect.
# deci poate fi pasată ca argument unei alte funcții.


# !CONCEPT _2_!
# o funcție poate fi definită în altă funcție.
#
# deci poate fi (și) returnată


"""
un decorator este o funcție
ce primește ca argument o altă funcție
și returnează o nouă funcție, "decorată".
"""

# !CONCEPT _3_!
# numele unei funcții este o variabilă
# (în afara atributului său intern __name__).
#
# deci poate fi asignată mai multor variabile


# CONCEPT lateral important:
# în Python toate variabilele sunt pointere


# !CONCEPT _3_! bis !
# corolar:
# "numele" unei funcții poate fi asignat
# altui obiect


# !CONCEPT _4_!
# hai să înlocuim in-place
# o funcție cu varianta sa decorată

import random
from functools import cache

def myfunc():
    return random(1000)
myfunc = cache(myfunc)


# !CONCEPT _5_!
# hai să facem syntactic sugar la acest mecanism
@cache
def myfunc():
    return random(1000)
