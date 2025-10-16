# folosind fișierul "temp_sensor_data.csv.gz"
#
# încărcați-l folosind modulele gzip, și csv
#
# într-o funcție generator
#
# care face yield unei tuple de forma
# (time, avg)
# unde time este minutul 
# și avg este media fiecărui minut
#
# folosiți modulul datetime.time
# pentru a procesa prima coloană

import gzip
import csv
from datetime import time

SENSOR_DATA_FILE = "data/temp_sensor_data.csv.gz"

def gendata_per_minute(iterable):
    batch = []
    prev_ts = None

    for ts, value in iterable:
        # converting into time:
        # v1: brute force
        #time(*[int(v) for v in ts.split(':')])

        # v2: we know about map
        #time(*map(int, ts.split(':')))

        # v3: we know more
        curr_ts = time.fromisoformat(ts).replace(second=0)

        if prev_ts is not None and prev_ts != curr_ts:
            # this is a new batch
            yield prev_ts, sum(batch) / len(batch)
            batch.clear()

        batch.append(float(value))
        prev_ts = curr_ts

def average_sensor_data(fname):
    fp = gzip.open(fname, 'rt')
    reader = csv.reader(fp)

    # skip header
    next(reader)
    
    gen = gendata_per_minute(reader)

    return gen


# test it
if __name__ == "__main__":
    print("testing data source")
    for idx, (ts, value) in enumerate(average_sensor_data(SENSOR_DATA_FILE)):
        print(f"{ts.hour}:{ts.minute:02d} {value:.2f}")
        if idx > 10:
            break
