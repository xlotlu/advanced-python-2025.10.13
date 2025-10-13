print("hello world")

# Ctrl+F5: runs the file.

# Shift+Enter: runs selection.

# pip install ipython


# Exercițiu 1:
#
# dat fiind dataset-ul "sales1.csv",
# procesați-l și construiți un dicționar de forma
#{
#    "item_id": total_quantity_sold,
#    ...
#}

# strategie:
# folosim modulul csv. în el avem `reader()` / `DictReader()`
# ambele primesc ca prim parametru un file pointer

import pprint

import csv
from os import path
from collections import defaultdict

#CSV_FILE = "data/sales1.csv"
CSV_FILE = path.join("data", "sales1.csv")

#fp = open(CSV_FILE)
#fp.close()

# pattern de acumulare
# 1. instanțiem obiectul în care acumulăm
#items_sold = {}

#items_sold = defaultdict(lambda: 0)
items_sold = defaultdict(int)
sales_per_city = defaultdict(int)

with open(CSV_FILE, encoding="utf-8") as fp: # context manager
    dreader = csv.DictReader(fp)

    for row in dreader:
        item_id = row['item_id']
        quantity = int(row['quantity'])
        city = row['city']
        unit_price = float(row['unit_price'])

        ## v1:
        # if item_id in items_sold:
        #     items_sold[item_id] += quantity
        # else:
        #     items_sold[item_id] = quantity

        ## v2:
        # if item_id not in items_sold:
        #     items_sold[item_id] = 0
        # items_sold[item_id] += quantity

        ## v3:
        # try:
        #     total_q = items_sold[item_id]
        # except KeyError:
        #     total_q = 0
        # items_sold[item_id] = total_q + quantity

        items_sold[item_id] += quantity
        sales_per_city[city] += unit_price * quantity

#pprint.pprint(items_sold)
pprint.pprint(sales_per_city)


# Exercițiu 2:
#
# aceleași cerințe,
# obțineți un raport cu vânzările totale per oraș.


#!! encoding: UTF-8 (Asia: posibil UTF-16)