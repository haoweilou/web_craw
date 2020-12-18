import pytesseract
import re
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
import cv2
image = cv2.imread("image2.png")
a = pytesseract.image_to_string(image=image)
output=""
for i in re.findall("[\S]",a):
    output+=i 
print(output)