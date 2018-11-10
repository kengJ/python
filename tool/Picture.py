from PIL import Image
import pytesseract

def toString(uri):
    image = Image.open(uri)
    # 指定路径
    tessdata_dir_config = '--tessdata-dir "D:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
    imtext = pytesseract.image_to_string(image,lang='chi_sim',config=tessdata_dir_config)
    return imtext
