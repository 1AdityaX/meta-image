from PIL.ExifTags import TAGS
from PIL import Image
import os

imagename = "image2.jpg"
imagen = os.path.abspath(imagename)
print(imagen)
image = Image.open(imagen)

exifdata = image.getexif()

for tag_id in exifdata:
    tag = TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id) 
    if isinstance(data, bytes):
        data = data.decode()
    print(f"{tag:25}: {data}")
    
