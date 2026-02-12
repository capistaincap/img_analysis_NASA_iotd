import os
import numpy as np
import pandas as pd
import requests as rq
from bs4 import BeautifulSoup as sp
from tqdm import tqdm

os.makedirs('images', exist_ok=True)

host_url = ['https://www.nasa.gov/image-of-the-day/',
            'https://www.nasa.gov/image-of-the-day/page/2/',
            'https://www.nasa.gov/image-of-the-day/page/3/'
            ]
img_list = list()

for i in range(len(host_url)):
    ## Parsing
    unparsed = rq.get(host_url[i])
    parsed = sp(unparsed.text, 'html.parser')

    ## Extracting imgs (returns list of ~ 40 imgs per page)
    container = parsed.find('div', class_='hds-gallery-items')
    imgs = container.find_all('img')

    ## Creating single image dicts and appending them to a master list
    for j in range(len(imgs)):
        src = imgs[j].get('src')
        alt = imgs[j].get('alt')
        individual_img = {
            'src': src,
            'alt': alt
        }
        img_list.append(individual_img)

## Downloading the images to ./images/
for i in tqdm(range(len(img_list))):
    img_url = img_list[i]['src']
    
    try:
        res = rq.get(img_url)
        if res.status_code == 200:
            file_path = f"images/image_{i}.jpg"
            with open (file_path, 'wb') as f:
                f.write(res.content)
        else:
            print("Failed to get url: ", img_url)
    except Exception as e:
        print("Error downlading: ", img_url)