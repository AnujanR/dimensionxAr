import os
from io import BytesIO

from rembg import remove
from PIL import Image
import subprocess
from collections import Counter
from sklearn.cluster import KMeans
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
import cv2
from tqdm.auto import tqdm


def colorExtractor(image_path):
    try:
        img_name = '.'+image_path
        raw_img = cv2.imread(img_name)
        raw_img = cv2.cvtColor(raw_img, cv2.COLOR_BGR2RGB)

        img = cv2.resize(raw_img, (900, 600), interpolation=cv2.INTER_AREA)
        img = img.reshape(img.shape[0] * img.shape[1], 3)

        clf = KMeans(n_clusters=5, n_init=3)
        color_labels = clf.fit_predict(img)
        center_colors = clf.cluster_centers_

        counter = Counter(color_labels)

        ordered_colors = [center_colors[i] for i in counter.keys()]
        hex_colors = [rgb_to_hex(ordered_colors[i]) for i in counter.keys()]

        colors = [counter[i] for i in counter.keys()]

        list_precent = [int(i) for i in list(colors)]
        text_c = [c + ' ' + str(round(p * 100 / sum(list_precent), 1)) + '%' for c, p in zip(hex_colors, list_precent)]

        return text_c,True

    except:
        print("Error in Colour Extraction!!")
        return '',False




def rgb_to_hex(rgb_color):
    hex_color="#"
    for i in rgb_color:
        i=int(i)
        hex_color+=("{:02x}".format(i))
    return hex_color