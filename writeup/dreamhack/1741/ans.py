import os
import cv2

BASE_PATH = os.path.dirname(__file__)

image = cv2.imread(f"{BASE_PATH}/pixel.png")

letter = ""
for r in image[11:14:2]:
    char = 0
    for idx, c in enumerate(r[15:36]):
        char = (char << 1) + (1 if c[0] == 0 else 0)
        if char.bit_length() == 7:
            letter += chr(char)
            char = 0

print("letter{" + letter + "}")
