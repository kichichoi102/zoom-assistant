import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime

# define a function to locate and click button found in imgs
def clickBtn(dire):
    pyautogui.locateOnScreen(dire)
    pyautogui.moveTo(dire)
    pyautogui.click()

def sign_in(meetingid, pswd):
    #opening up the zoom app
    subprocess.call(["C:\\Users\\Daniel\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"])
    
    time.sleep(1)

    # Join the meeting
    clickBtn("C:\\Users\\Daniel\\Desktop\\Not_a_zoom_bot\\img\\join_button.png")

    time.sleep(1)

    # Write meeting id
    pyautogui.write(meetingid)

    # Disable both camera and mic
    media_btn = pyautogui.locateAllOnScreen("C:\\Users\\Daniel\\Desktop\\Not_a_zoom_bot\\img\\media_button.png")
    for btn in media_btn:
        pyautogui.moveTo(btn)
        pyautogui.click()
    
    time.sleep(1)

    # Join the Call
    clickBtn("C:\\Users\\Daniel\\Desktop\\Not_a_zoom_bot\\img\\join_button_2.png")

    time.sleep(1)

    # Write Password
    if pswd == 0:
        pass
    else:
        pyautogui.write(pswd)
        pyautogui.press('enter')

    print("signed in ", meetingid)
    

# Signing out
def sign_out():
    
    #Press end button
    clickBtn("C:\\Users\\Daniel\\Desktop\\Not_a_zoom_bot\\img\\end_button.png")

    #Leave meeting
    clickBtn("C:\\Users\\Daniel\\Desktop\\Not_a_zoom_bot\\img\\leave_button.png")

    print("signed out")

# Reading the schedule csv
df = pd.read_csv("Desktop/Not_a_zoom_bot/Schedule.csv")


while True:
    # Check current time
    now = datetime.now().strftime("%w,%H:%M")
    if now in str(df['Start']):
        
        # If current time == time for class, call the sign_in function
        row = df.loc[df['Start'] == now]
        m_id = str(row.iloc[0,1])
        m_pswd = str(row.iloc[0,2])

        sign_in(m_id, m_pswd)

    # If current time == time for end class, call the sign_out function
    if now in str(df['End']):
        row = df.loc[df['End'] == now]

        sign_out()
        

