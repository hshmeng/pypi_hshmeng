import pyautogui
import time

def dazi(text, wpm):
    # 计算每个字符之间的延迟时间（秒）
    delay = 60 / (wpm * 5)  # 假设每个单词平均有5个字符

    # 等待5秒以便你有时间切换到目标窗口
    time.sleep(5)

    for char in text:
        pyautogui.typewrite(char)
        time.sleep(delay)