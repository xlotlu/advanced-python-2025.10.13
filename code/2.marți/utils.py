import string
import unicodedata


CHARACTERS = string.ascii_letters + string.digits


def generate_id(str):
    """
    înlocuiește caracterele non-alfanumerice cu '-'
    și înlocuiește diacriticele.
    """

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

    return "".join(out).lower()