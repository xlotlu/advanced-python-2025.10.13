# scrieți un context manager
# `timeit()`
# care să facă print cu timpul de execuție
# dintre `__enter__` și `__exit__`

from datetime import datetime

class timeit:
    def __enter__(self):
        self.start = datetime.now()

    def __exit__(self, exc_type, exc_value, traceback):
        diff = datetime.now() - self.start
        print(f"durată: {diff.seconds}.{diff.microseconds}")


from time import sleep

with timeit():
    print("dorm un pic")
    sleep(1.1)
    print("gata")



# The following code creates a database connection, creates a table and inserts some rows:

import sqlite3

con = sqlite3.connect("tutorial.db") #  aceasta se va rula la __init__

cur = con.cursor()
cur.execute("CREATE TABLE movie(title, year, score)")
cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")
con.commit()
res = cur.execute("SELECT score FROM movie")
print(res.fetchall())

con.close()  # aceasta se va rula la __exit__

# Create a context manager to handle a database connection.
# [!!] The context manager will return the connection object on setup
# and will close the connection on teardown.
#
# Make it get a positional argument: `dbfile`

class MyConnection:
    def __init__(self, conn_file):
        self.conn_file = conn_file

    def __enter__(self):
        self.con = sqlite3.connect(self.conn_file)
        return self.con
        
    def __exit__(self, exc_type, exc_value, traceback):
        self.con.close()

with MyConnection("my.db") as con:
    cur = con.cursor()
    cur.execute("CREATE TABLE movie(title, year, score)")
    cur.execute("""
        INSERT INTO movie VALUES
            ('Monty Python and the Holy Grail', 1975, 8.2),
            ('And Now for Something Completely Different', 1971, 7.5)
    """)
    con.commit()
    res = cur.execute("SELECT score FROM movie")
    print(res.fetchall())

# Concepte importante:
# 1. context manager-ul este o clasă, deci, dacă primește parametri,
#    aceștia se aplică la __init__()
# 2. metoda __enter__() returnează variabila pentru "manager() as variabila".

