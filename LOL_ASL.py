import pyautogui as pag
import time
import pyperclip

# 아이콘 위치
chat_pos = {'left': 434, 'top': 860, 'width': 240, 'height': 25}

# 버튼 위치
left_button = [129, 1321]
right_button = [696, 1328]

# while True:
#     x, y = pag.position()
#     position_str = 'X: ' + str(x) + ' Y: ' + str(y)
#     print(position_str)

while True:
    # pyperclip.copy("110441609111 신한\n12,100원")
    pyperclip.copy("NO")
    pag.hotkey("ctrl", "v")
    time.sleep(0.01)
    pag.typewrite('\n')
