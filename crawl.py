from urllib.parse import urlparse
from bs4 import BeautifulSoup

def normalize_url(input_url):
    parsed = urlparse(input_url)
    return parsed.hostname + parsed.path.rstrip('/')

#print(normalize_url("http://blog.boot.dev/path/"))

def get_h1_from_html(html):
    pass
