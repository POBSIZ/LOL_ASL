import pyautogui as pag
import numpy as np
import mss, cv2

agree_btn_pos = {'x': 956, 'y':732, 'width':200, 'height':30}
chat_input_pos = {'x':434, 'y':860, 'width':314, 'height':25}

agrBtn = [956, 732]
chtBtn = [434, 860]

while True:
    x, y = pag.position()
    position_str ='x: ' + str(x) + ' y: ' + str(y)
    print(position_str)