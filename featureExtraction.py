import os
from tqdm import tqdm
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from PIL import Image

Image.MAX_IMAGE_PIXELS = None ## -> This is for removing the maximum pixel pillow limitaions on initial image read

results = list()

for file_name in tqdm(os.listdir('images')):
    if file_name.endswith('.jpg'):
        img_url = os.path.join('images', file_name)

        with Image.open(img_url) as img:
            img = img.convert('RGB')
            img = img.resize((512,512))
            imgArr = np.asarray(img)

            mean_color = imgArr.mean(axis=(0,1))
            brightness = imgArr.mean()

            img_props = {
                'file': file_name,
                'brightness': brightness,
                'mean_red': float(mean_color[0]),
                'mean_green': float(mean_color[1]),
                'mean_blue': float(mean_color[2])
            }

            results.append(img_props)

## to do: add more functions later

df = pd.DataFrame(results)
df.to_csv("img_features.csv", index=False)
