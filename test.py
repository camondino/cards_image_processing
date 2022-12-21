import PIL
import pytesseract
import cv2
import numpy as np
import matplotlib.pyplot as plt

def preprocessing_image(img):
    #Resize image 
    #img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

    # convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.multiply(gray, 1.5)
    
    # blur remove noise
    blured1 = cv2.medianBlur(gray,3)
    blured2 = cv2.medianBlur(gray,51)
    divided = np.ma.divide(blured1, blured2).data
    normed = np.uint8(255*divided/divided.max())
    
    # Threshold image
    th, threshed = cv2.threshold(normed, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)
    
    return threshed

#Custom function to show open cv image on notebook.
def display_img(cvImg):
    cvImg = cv2.cvtColor(cvImg, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(10,8))
    plt.imshow(cvImg)
    plt.axis('off')
    plt.show()


# Open the file as an image
image_file = PIL.Image.open("images/card.jpeg")

testPreprocess = preprocessing_image(image_file)
display_img(testPreprocess)


# image_file.show()

# Use tesseract to extract the text from the image
string_contents = pytesseract.image_to_string(image_file, lang='eng')

# Print the contents to the console
print("The contents says: ")
print(string_contents)