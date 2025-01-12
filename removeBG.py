from rembg import remove 
from PIL import Image

## Path for input and output image
input_img = 'programmer-filter.png'
output_img = 'programmer-filter-nbg.png'

## loading and removing background
inp = Image.open(input_img)
output = remove(inp)

## Saving background removed image to same location as input image
output.save(output_img)