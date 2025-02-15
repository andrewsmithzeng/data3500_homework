import pyautogui
import time
import os
from datetime import datetime

# ✅ 设定截图保存文件夹
screenshot_folder = "screenshots-chn+eng"
if not os.path.exists(screenshot_folder):
    os.makedirs(screenshot_folder)

# ✅ 设定截图区域（你提供的参数）
left_top_x = 1726
left_top_y = 28
width = 1668
height = 1341

# ✅ “下一题”按钮坐标
next_button_x = 3219
next_button_y = 1346

# ✅ 设定截图次数
num_screenshots = 150

for i in range(num_screenshots):
    print(f"正在截图 {i + 1}/{num_screenshots} ...")

    # 📌 只截取题目区域
    screenshot_path = os.path.join(screenshot_folder, f"screenshot_{i+1}.png")
    screenshot = pyautogui.screenshot(region=(left_top_x, left_top_y, width, height))
    screenshot.save(screenshot_path)

    print(f"✅ 截图 {i + 1} 已保存: {screenshot_path}")

    # 📌 点击 "下一题" 按钮
    pyautogui.click(next_button_x, next_button_y)

    # 📌 等待加载（可适当调整）
    time.sleep(2)

print("🎉 所有截图完成！")
