import requests
from pathlib import Path
import os


Path("books").mkdir(parents=True, exist_ok=True)
if not os.path.exists("books"):
    os.makedirs("books")

for id in range(10):
    url = f"https://tululu.org/txt.php?id={id}"

    response = requests.get(url)
    response.raise_for_status() 

    with open(f"books/{id}.txt", 'wb') as file:
        file.write(response.content)