from PIL import Image
from pytesseract import pytesseract

# Define path to tessaract.exe
path_to_tesseract = r'/opt/homebrew/Cellar/tesseract/5.2.0/bin/tesseract'

# Define path to image
path_to_image = 'images/image0465.jpg'

# Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

# Open image with PIL
img = Image.open(path_to_image)

# Extract text from image
text = pytesseract.image_to_string(img)
print(text)