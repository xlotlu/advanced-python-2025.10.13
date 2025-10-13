# scrieți o funcție
# `mul_iter(it, num)`
# ce primește un iterabil și returnează o listă
# de aceeași lungime, cu fiecare element al `it` înmulțit cu `num`

# v1. folosind un obiect de acumulare
def mul_iter(it, num):
    # 0. instanțiem obiectul de acumulare
    out = []
    # 1. iterăm prin obiectul sursă
    for elem in it:
        # 2. facem calculele necesare
        result = elem * num
        # 3. adăugăm rezultatul la acumulator
        out.append(result)

    # la final. returnăm.
    return out


# v2. folosind list comprehension
def mul_iter(it, num):
    return [elem * num for elem in it]


# scrieți o funcție
# `mul_odd_iter(it, num)`
# ce primește un iterabil de numere și returnează o listă
# numai a numerelor impare, cu fiecare element respectiv înmulțit cu `num`

# v1. folosind un obiect de acumulare
def mul_odd_iter(it, num):
    # 0. instanțiem obiectul de acumulare
    out = []
    # 1. iterăm prin obiectul sursă
    for elem in it:
        # 2. filtrăm
        if elem % 2:
            # 3. facem calculele necesare
            result = elem * num
            # 4. adăugăm rezultatul la acumulator
            out.append(result)

    # la final. returnăm.
    return out

# v2. folosind list comprehension
def mul_iter(it, num):
    return [
        elem * num
        for elem in it
        if elem % 2
    ]



# Exercițiu: dat fiind range(ord("!"), ord("~") + 1)
# creați un dicționar unde cheia este caracterul
# (obținut cu chr())
# și valoarea este ordinalul.
#
# folosiți dictionary comprehension
# {k: v for elem in iterable}

d = {chr(i): i for i in range(ord("!"), ord("~") + 1)}

# Exercițiu: folosind dicționarul de mai sus
# creați un dicționar nou, unde valoarea
# din cel vechi devine cheia în cel nou.

inverted = {v: k for k, v in d.items()}


# Exercițiu:
# având lista
cities = ["Arad", "Arad", "București", "Constanța", "București"]
# creați un set cu comprehension
{k for k in cities}