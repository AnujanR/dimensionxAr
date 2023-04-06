import os
from io import BytesIO

from rembg import remove
from PIL import Image
import subprocess

import torch
from tqdm.auto import tqdm


def removeBg(image_data,output_dir):
    try:
        # Open the image using Pillow
        image = Image.open(BytesIO(image_data.read()))

        #remove background
        input = image
        removed_bg = remove(input)

        # Create a new white background image with the same size as the original image
        background = Image.new('RGB', removed_bg.size, (255, 255, 255))

        # Paste the original image onto the white background
        background.paste(removed_bg, mask=removed_bg.convert('RGBA'))

        # Save the image with the white background
        background.save(output_dir+f'{str(image_data).split(".")[0]}.png')

        return background,True

    except:
        print("Error in removing Background!!")
        return '',False

def generate_point_clouds(imgname):
    # Save the current working directory
    parent_directory_path = os.getcwd()

    # Change to the subdirectory
    directory_path = os.path.abspath('Point3dGenerator/libraries/pointe/')
    os.chdir(directory_path)

    # Define the command to generate point clouds
    process = subprocess.Popen(['python', 'execute.py','--imgpath','../../Dataset/'+str(imgname).split('.')[0]+".png",'--out','../../Dataset/'+str(imgname).split('.')[0]+".ply"], stdout=subprocess.PIPE)
    result, error = process.communicate()

    # Check if the command was successful
    if process.returncode == 0:
        print('Point Clouds Generated successfully.')
    else:
        print('Error: ', result.stderr.decode('utf-8'))

    # Change back to the parent directory
    os.chdir(parent_directory_path)
