# Remove-Photo-Background-using-TensorFlow
In this program, we are using image segmentation to remove background from photos. For this, we are using a DeepLabV3+ trained on the human image segmentation dataset.

## DeepLabV3+
- Dataset:  [Person Segmentation](https://www.kaggle.com/nikhilroxtomar/person-segmentation/download)
- Weight file: [model.h5](https://drive.google.com/file/d/17QKxSIBFhyJoDps93-sCVHnVV6UWS1sG/view?usp=sharing)

## Results
Here are some of the images, where the background is removed and changed to red.
Original Image             |  Processed Image 
:-------------------------:|:-------------------------:
![](images/picture.jpg)  |  ![](remove_bg/picture.png)
![](images/beyonceandjay-z-Mikecoppola-c59229db80174b3290431f66eea3d8ff.jpg)  |  ![](remove_bg/beyonceandjay-z-Mikecoppola-c59229db80174b3290431f66eea3d8ff.png)
