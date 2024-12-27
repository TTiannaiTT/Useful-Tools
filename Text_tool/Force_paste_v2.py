import ctypes
from time import sleep

# 目前仅支持英文
# 定义一些常量
PUL = ctypes.POINTER(ctypes.c_ulong)

class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# 键盘输入相关函数
def press_key(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def release_key(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def type_string(input_string):
    # 字符到虚拟键码的简单映射表（可以根据需要扩展）
    char_to_keycode = {
        'a': 0x1E, 'b': 0x30, 'c': 0x2E, 'd': 0x20, 'e': 0x12,
        'f': 0x21, 'g': 0x22, 'h': 0x23, 'i': 0x17, 'j': 0x24,
        'k': 0x25, 'l': 0x26, 'm': 0x32, 'n': 0x31, 'o': 0x18,
        'p': 0x19, 'q': 0x10, 'r': 0x13, 's': 0x1F, 't': 0x14,
        'u': 0x16, 'v': 0x2F, 'w': 0x11, 'x': 0x2D, 'y': 0x15,
        'z': 0x2C, ' ': 0x39, '0': 0x0B, '1': 0x02, '2': 0x03,
        '3': 0x04, '4': 0x05, '5': 0x06, '6': 0x07, '7': 0x08,
        '8': 0x09, '9': 0x0A,
    }

    for char in input_string:
        if char.lower() in char_to_keycode:
            keycode = char_to_keycode[char.lower()]
            press_key(keycode)
            release_key(keycode)
            sleep(0.05)  # 添加延时，模拟正常打字速度

# 示例使用
def main():
    sleep(2)  # 等待2秒以便切换到目标窗口
    type_string("hello world!")

if __name__ == "__main__":
    main()
