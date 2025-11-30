import pyautogui
import time
import pyperclip
from openai import OpenAI


client=OpenAI(
    api_key="put your own api key",
)

def is_last_msg_from_sender(chat_log,sender_name="Rahul"):
    messages=chat_log.strip().split("\2025]")[-1]
    if sender_name in messages:
        return True
    return False

pyautogui=Click(1639,1412)
time.sleep(2)

while True:
    
    pyautogui.moveTo(1026,244)
    pyautogui.dragTo(1131,1321,duration=1.0,button="left")

    pyautogui.hotkey('ctrl','c')
    time.sleep(2)
    pyautogui.click(994,281)

    chat_history=pyperclip.paste()

    print(chat_history)

    if is_last_msg_from_sender(chat_history):
        completion=client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role":"system","content":"you are a person named piyush who speaks hindi as well as english .You are from India and you are a coder."
                "You analyze chat history and respond like piyush.output should be the next chat response (text message only)"},
                {"role":"user","content":chat_history}
            ]
        )

        response= completion.choices[0].message.content
        pyperclip.copy(response)

        pyautogui.click(1008,1328)
        time.sleep(1)

        pyautogui.hotkey('ctrl','v')
        time.sleep(1)

        pyautogui.press('enter')
