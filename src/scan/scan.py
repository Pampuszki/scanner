import cv2
import pytesseract


class Scan:
    """Class to scanning and read text from images."""

    def __init__(self) -> None:
        self.a = 5

    def read_image(self, path):
        img = cv2.imread("image.jpg")
        # Adding custom options
        custom_config = r"--oem 3 --psm 6"
        pytesseract.image_to_string(img, config=custom_config)
