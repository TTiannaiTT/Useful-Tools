import pyautogui
import time
import pyperclip


def type_Eng(text):
    print("Waiting for 2 seconds...")
    time.sleep(2)
    print("Starting to type text...")
    pyautogui.typewrite(text, interval=0.1)
    print("Typing completed")

def type_text(text):
    print("等待2秒...")
    time.sleep(2)
    print("开始输入文本...")
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')
    print("输入完成")

if __name__ == "__main__":
    text_to_type = "试试"
    type_text(text_to_type)

    # text_to_type = "This is the target."
    # type_Eng(text_to_type)
