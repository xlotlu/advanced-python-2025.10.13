import os

# v1, os.scandir()

def get_files(dirname, starting_with):
    out = (
        item for item in os.scandir(dirname)
        if item.name.startswith(starting_with)
    )

    out = filter(lambda item: item.name.startswith(starting_with),
                 os.scandir(dirname))
    
    return out


for f in get_files("data/shoppy/sales/", "2025"):
    print(f)


import glob

# v2, glob.glob()
def get_files(dirname, starting_with):
    return glob.glob(f'data/shoppy/sales/{starting_with}*')
                     
for f in get_files("data/shoppy/sales/", "2025"):
    print(f)


# vx, os.walk()
for dname, subdirs, files in os.walk('data'):
    pass

"""
('data', ['shoppy'], ['sales1.csv', 'temp_sensor_data.csv.gz'])

('data/shoppy', ['sales', 'purchases'], ['categories.json', 'items.json', 'locations.json', 'price_changes.csv', 'customers.json'])

('data/shoppy/sales', [], ['2023-10-22.csv', ............... ])

('data/shoppy/purchases', [], ['2023-07.csv', '2025-02.csv', ............])
"""