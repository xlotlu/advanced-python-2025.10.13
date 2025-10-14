# scrieți funcția generate_id(name):
#
# 1. va transforma fiecare caracter care nu este
# literă sau număr în '-'
# folosiți string.ascii_letters și string.digits
#
# 2. transformați diacriticele în litera de bază
#    1. un caracter cu diacritice are ord() > 127.
#    2. unicodedata.decomposition va returna un string
#       format din 2 numere hexadecimale.
#       chr(int(num, 16)) # va returna caracterul
# 3. liniuțele multiple să fie unicizate
# 4. lowercase

# strategie?
# stringul este iterabil după caracter

import string

CHARACTERS = string.ascii_letters + string.digits

def generate_id(str):
    stripped = [
        c if c in CHARACTERS else '-'
        for c in str
    ]

    out = []
    prev = ""
    for c in stripped:
        if c == '-' and prev == '-':
            continue
        else:
            out.append(c)
        prev = c

    return "".join(out).strip('-')


def generate_id1(str):
    out = []
    prev = ""

    for c in str:
        if c not in CHARACTERS:
            if prev == '-':
                continue
            else:
                c = '-'

        out.append(c)
        prev = c

    return "".join(out).strip('-')



def generate_id2(str):
    str_with_blanks = "".join(
        c if c.isalnum() else ' '
        for c in str
    )

    return "-".join(
        str_with_blanks.split() # unicizează spații
    )
    
s = "Țesătură de plajă #12!"
#print(generate_id1(s))
#print(generate_id2(s))


def generate_id(str):
    out = []
    prev = ""

    for c in str:
        if ord(c) > 127:
            dec = unicodedata.decomposition(c)
            
            # dec = '0061 0306'
            # dec = '<compat> 0020 030A'

            if not dec:
                c = '-'
            else:
                hexord = dec.split(" ")[-2]
                c = chr(int(hexord, 16))

        if c not in CHARACTERS:
            c = '-'

        if c == '-' and prev == '-':
            continue

        out.append(c)
        prev = c

    # do strip right on the list
    for idx in 0, -1:
        if out[idx] == '-':
            del out[idx]

    return "".join(out)

s = "˚Țesătură de plajă #12€!"
print(generate_id(s))