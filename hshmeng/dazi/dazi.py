import pyautogui
import time

print("打字(文字内容, 打字速度(字每分钟), 等待时间(秒)")
print("需要安装pip install pyautogui")

def dazi(text, wpm, sleep):
    # 计算每个字符之间的延迟时间（秒）
    delay = 60 / (wpm * 5)  # 假设每个单词平均有5个字符

    # 等待5秒以便你有时间切换到目标窗口
    time.sleep(sleep)

    for char in text:
        pyautogui.typewrite(char)
        time.sleep(delay)

