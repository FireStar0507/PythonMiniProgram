import pyautogui
import random
import time
import sys

step = (50,101)
steptime = (0.5,1.5)
waitime = (2,4)

try:
    screen_width, screen_height = pyautogui.size()
    while True:
        # 随机选择方向
        direction = random.choice(['up', 'down', 'left', 'right'])

        # 随机游走距离
        distance = random.randint(*step)

        current_x, current_y = pyautogui.position()

        if direction == 'up':
            new_y = current_y - distance
            if new_y < 0:
                new_y = screen_height + new_y
            pyautogui.moveTo(current_x, new_y, duration=(random.uniform(*steptime)))
        elif direction == 'down':
            new_y = current_y + distance
            if new_y >= screen_height:
                new_y = new_y - screen_height
            pyautogui.moveTo(current_x, new_y, duration=(random.uniform(*steptime)))
        elif direction == 'left':
            new_x = current_x - distance
            if new_x < 0:
                new_x = screen_width + new_x
            pyautogui.moveTo(new_x, current_y, duration=(random.uniform(*steptime)))
        elif direction == 'right':
            new_x = current_x + distance
            if new_x >= screen_width:
                new_x = new_x - screen_width
            pyautogui.moveTo(new_x, current_y, duration=(random.uniform(*steptime)))

        print(f"{direction}")

        # 随机等待时间
        time.sleep(random.uniform(*waitime))
except KeyboardInterrupt:
    print("程序已停止。")
