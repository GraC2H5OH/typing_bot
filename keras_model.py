import pytesseract
import cv2

def model(file):
    pytesseract.pytesseract.tesseract_cmd = 'D:\\Tesseract-OCR\\tesseract.exe'
    img = cv2.imread(file)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    text=pytesseract.image_to_string(img)
    return text[: -1]
