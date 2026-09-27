import time
import requests

urls = ["http://example.com"] * 5

def download_sequencial(urls):
    for url in urls:
        requests.get(url)

start = time.time()
download_sequencial(urls)
print(f"Tempo Sequencial: {time.time() - start:.2f} segundos")