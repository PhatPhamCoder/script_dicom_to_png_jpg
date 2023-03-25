import numpy as np
import pydicom  # Lib
from PIL import Image
import os

# path = "./Database/00e4ba50f379a0f2b8bebba3f8460807.dicom"
# im = pydicom.dcmread(path)  # read image by dycom lib

# im = im.pixel_array.astype(float)  # change type image

# rescaled_image = (np.maximum(im, 0)/im.max())*255  # float pixels
# final_image = np.uint8(rescaled_image)  # interger pixels

# final_image = Image.fromarray(final_image)
# final_image.show()  # Show Image after convert .dicom to type image
# final_image.save("new_image.png")  # save Image as PNG or JPG


def get_names(path):
    names = []
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            _, ext = os.path.splitext(filename)
            if ext in ['.dicom']:
                names.append(filename)

    return names


# print("Check get name", get_names("Database"))

def convert_dicom_jpg(name):
    path = "Database/"+name

    im = pydicom.dcmread(path)  # read image by dycom lib

    im = im.pixel_array.astype(float)  # change type image

    rescaled_image = (np.maximum(im, 0)/im.max())*255  # float pixels
    final_image = np.uint8(rescaled_image)  # interger pixels

    final_image = Image.fromarray(final_image)

    return final_image


names = get_names("Database")
for name in names:
    image = convert_dicom_jpg(name)
    image.save(name+".png")
