"""
Image meta data

This program gives you the embedded meta data of the given image

"""

from PIL.ExifTags import TAGS # Nessacary imports
from PIL import Image
import os


def image_osint(image):
    imagen = os.path.abspath(image) #Gets the absolute path of the image
    image = Image.open(imagen) #Opens the image and gives a image object

    exifdata = image.getexif() # Gets the exif data of the image (meta data)

    for tag_id in exifdata: #loops through the exif data
        tag = TAGS.get(tag_id, tag_id) # Gets the data tags
        data = exifdata.get(tag_id)  # Gets the data inside it 
        if isinstance(data, bytes):
            data = data.decode() # decodes the data
        return f"{tag:25}: {data}" #return the meta-data

imagename = "image.jpg" #image path
metadata = image_osint(imagename)
print(metadata)
    
