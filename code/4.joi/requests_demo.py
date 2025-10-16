# requests

import requests

"""
# se folosește (și ca) context manager
resp = requests.get('https://www.google.com')
resp.content # <-- bytes
resp.text    # <-- str

resp.json()  # <-- when the response is json

# iterator, needs stream=True on the request
resp.iter_lines(decode_unicode=True)
resp.iter_content()
"""

# având un fișier binar via http,
# obțineți-l și scrieți-l pe disc.

# folosiți context manager atât pentru request, cât și pentru fișier.

URL = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Lake_Willoughby_October_2021_003.jpg/1280px-Lake_Willoughby_October_2021_003.jpg"
OUTPUT = "file.jpg"

user_agent = 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36'

"""
with requests.get(URL,
                  headers = {'User-Agent': user_agent}
                  ) as resp:
    if resp.status_code != 200:
        print("this was an error")

    resp.raise_for_status()

    with open(OUTPUT, 'wb') as f:
        f.write(resp.content) # bytes
"""

# codul de mai sus citește tot content-ul în memorie

# alternativă:
"""
with requests.get(URL,
                  stream=True, # <-- !
                  headers = {'User-Agent': user_agent}
                  ) as resp:
    
    resp.raise_for_status()

    with open(OUTPUT, 'wb') as f:
        # now we can iterate through the binary response
        for chunk in resp.iter_content():
            f.write(chunk)
"""

# să obținem numele fișierului
import os.path
import urllib.parse



# scrieți o funcție `get_file(url)`
# ce primind ca parametru url-ul
# scrie fișierul pe disc. (cu numele lui corect)
def fetch_file(url):
    rez = urllib.parse.urlparse(url)
    base, fname = os.path.split(rez.path)

    with requests.get(url,
                    stream=True, # <-- !
                    headers = {'User-Agent': user_agent}
                    ) as resp:
    
        resp.raise_for_status()

        with open(fname, 'wb') as f:
            # now we can iterate through the binary response
            for chunk in resp.iter_content():
                f.write(chunk)

# o funcție care copiază un fișier în altul
# (primește argumente path-urile respective)
def cp_file(src, target):
    with open(src, 'rb') as sfp, \
         open(target, 'wb') as tfp:

        """
        while True:
            chunk = sfp.read(4096)
            if not chunk:
                break
            tfp.write(chunk)
        """

        while chunk := sfp.read(4096):
            tfp.write(chunk)




# funcție.
# citim json de pe rețea.
# returnăm rezultatul (ca datatype de python)

URL = "https://jsonplaceholder.typicode.com/todos"

def fetch_json(url):
    with requests.get(url) as resp:
        resp.raise_for_status()
        return resp.json()

# fetch_json(URL)
