import numpy as np
import pydicom  # Lib
from PIL import Image

path = "./4e3a578fe535ea4f5258d3f7f4419db8.dicom"  # import image .dicom/.dcm
im = pydicom.dcmread(path)  # read image by dycom lib

im = im.pixel_array.astype(float)  # change type image

rescaled_image = (np.maximum(im, 0)/im.max())*255  # float pixels
final_image = np.uint8(rescaled_image)  # interger pixels

final_image = Image.fromarray(final_image)
final_image.show()  # Show Image after convert .dicom to type image
final_image.save("new_image.png")  # save Image as PNG or JPG
