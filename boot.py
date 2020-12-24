import subprocess
import pyautogui
import time
import os
import pandas as pd
from datetime import datetime


def sing_in(meeting_id, password):
    # Opens The Zoom App
    subprocess.Popen("C:\\Users\\Administrator\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
    print('Done')
    time.sleep(10)

    # Clicks For Safety.
    pyautogui.click(638, 343)

    # Clicks On The Join Button.
    join_btn = pyautogui.locateCenterOnScreen('join_btn.PNG')
    pyautogui.click(join_btn)
    time.sleep(2)

    # Double Click on meeting Box.
    enter_meeting = pyautogui.doubleClick(571, 330)
    pyautogui.click(enter_meeting)
    time.sleep(2)
    pyautogui.write(meeting_id)

    # Clicks on the box.
    box = pyautogui.locateCenterOnScreen('box_btn.PNG')
    pyautogui.click(box)
    time.sleep(2)

    # Clicks On Join.
    join = pyautogui.locateCenterOnScreen('join.PNG')
    pyautogui.click(join)
    time.sleep(7)

    # Enters the password.
    pyautogui.doubleClick(613, 331)
    time.sleep(2)
    pyautogui.write(password)

    # Clicks the join meeting button.
    join_meeting = pyautogui.locateCenterOnScreen('join_meeting_after_pass.PNG')
    pyautogui.click(join_meeting)
    time.sleep(5)


df = pd.read_csv('timings.csv')

while True:
    now = datetime.now().strftime("%H:%M")
    if now in str(df['timings']):
        row = df.loc[df['timings'] == now]
        m_id = str(row.iloc[0, 1])
        m_pwsd = str(row.iloc[0, 2])

        sing_in(m_id, m_pwsd)
        time.sleep(40)
        print('Singed in...')
        time.sleep(60)
        os.system('taskkill /f /im Zoom.exe')
