import pyautogui as pag
import numpy as np
import mss, cv2

agree_btn_pos = {'x': 956, 'y':732, 'width':200, 'height':30}
chat_input_pos = {'x':434, 'y':860, 'width':314, 'height':25}

agrBtn = [956, 732]
chtBtn = [434, 860]

# bluestacks 좌표
# 아이콘 위치
agree_pos = {'left': 963, 'top': 733, 'width': 150, 'height': 30}
chat_pos = {'left': 434, 'top': 860, 'width': 240, 'height': 25}

# 버튼 위치
left_button = [129, 1321]
right_button = [696, 1328]

with mss.mss() as sct:
    left_img = np.array(sct.grab(agree_pos))[:,:,:3]
    right_img = np.array(sct.grab(chat_pos))[:,:,:3]

    cv2.imshow('left_img',left_img)
    cv2.imshow('right_img',right_img)
    cv2.waitKey(0)

# while True:
#     x, y = pag.position()
#     position_str = 'X: ' + str(x) + ' Y: ' + str(y)
#     print(position_str)