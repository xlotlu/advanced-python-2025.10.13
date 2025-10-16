# requests_and_streaming_csv

import requests
from time import sleep
from morning_iterators import gendata_per_minute


URL = 'http://localhost:8081'




def average_sensor_data(url):
    resp = requests.get(url, stream=True)

    it = resp.iter_lines(decode_unicode=True)

    reader = csv.reader(it)

    # skip header
    next(reader)

    gen = gendata_per_minute(reader)

    return gen



# test it
if __name__ == "__main__":
    print("testing data source")
    for idx, (ts, value) in enumerate(average_sensor_data(URL)):
        print(f"{ts.hour}:{ts.minute:02d} {value:.2f}")
        if idx > 10:
            break




