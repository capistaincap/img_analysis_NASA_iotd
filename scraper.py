import os
import numpy as np
import pandas as pd
import requests as rq
from bs4 import BeautifulSoup as sp

os.makedirs('images', exist_ok=True)

## Scraping Images
unparsed = rq.get('https://www.nasa.gov/image-of-the-day/')
parsed = sp(unparsed.text, 'html.parser')
container = parsed.find('div', class_='hds-gallery-items')
imgs = container.find_all('img')

img_list = list()

for i in range(len(imgs)):
    src = imgs[i].get('src')
    alt = imgs[i].get('alt')

    img_set = {
        'src': src,
        'alt': alt
    }
    img_list.append(img_set)

## Downloading Images

for i in range(len(img_list)):
    url = img_list[i]['src']

    try:
        res = rq.get(url)

        if res.status_code == 200:
            file_path = f"images/img_{i}.jpg"
            with open (file_path, 'wb') as f:
                f.write(res.content)
        else:
            print("Failed for url ", url)
    except Exception as e:
        print("Error downloading, ", url)

