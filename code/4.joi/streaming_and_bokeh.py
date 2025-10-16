# streaming_and_bokeh

from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource, Range1d

from time import sleep
import csv
import threading
import requests
from datetime import time
from collections import deque


URL = "http://localhost:8081"
ROLLOVER = 60 * 60 * 6
SLEEP = .001
SMOOTHING = 60

def read_data():
    with requests.get(URL, stream=True) as resp:
        it = resp.iter_lines(decode_unicode=True)
        reader = csv.reader(it)

        # skip header
        next(reader)

        data = deque(maxlen=SMOOTHING)

        for t, v in reader:
            t = time.fromisoformat(t)
            v = float(v)

            data.append(v)

            avg = sum(data) / len(data)

            doc.add_next_tick_callback(
                lambda: source.stream(
                    dict(time=[t], value=[avg]),
                    rollover=ROLLOVER
                )
            )

            sleep(SLEEP)


# the bokeh stuff
doc = curdoc()

source = ColumnDataSource(data=dict(time=[], value=[]))
plot = figure(
    title="Streaming sensor data",
    
    x_axis_label="Time",
    y_axis_label="Value",
    
    x_axis_type="datetime",
    #y_range = Range1d(start=10, end=30),
    
    sizing_mode="stretch_width",
)

plot.line('time', 'value', source=source, line_width=2)

doc.add_root(plot)
# /end the bokeh stuff


thread = threading.Thread(target=read_data, daemon=True)
thread.start()
# aici continuă execuția

print("»»» now running bokeh! «««")