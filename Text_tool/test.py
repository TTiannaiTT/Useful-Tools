import ctypes
from time import sleep

# 定义常量和结构体
PUL = ctypes.POINTER(ctypes.c_ulong)


class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput)]


class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]


# 按键和释放键函数
def press_key(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(hexKeyCode, 0, 0, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def release_key(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(hexKeyCode, 0, 0x0002, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


# 模拟按键输入函数
def type_pinyin(pinyin):
    char_to_keycode = {
        'a': 0x1E, 'b': 0x30, 'c': 0x2E, 'd': 0x20, 'e': 0x12,
        'f': 0x21, 'g': 0x22, 'h': 0x23, 'i': 0x17, 'j': 0x24,
        'k': 0x25, 'l': 0x26, 'm': 0x32, 'n': 0x31, 'o': 0x18,
        'p': 0x19, 'q': 0x10, 'r': 0x13, 's': 0x1F, 't': 0x14,
        'u': 0x16, 'v': 0x2F, 'w': 0x11, 'x': 0x2D, 'y': 0x15,
        'z': 0x2C, ' ': 0x39
    }

    for char in pinyin:
        if char in char_to_keycode:
            keycode = char_to_keycode[char]
            press_key(keycode)
            release_key(keycode)
            sleep(0.05)  # 模拟自然输入的延迟


# 选择候选字函数
def select_candidate(index=1):
    """
    选择输入法候选字。
    :param index: 候选字的序号（1-9）
    """
    if 1 <= index <= 9:
        keycode = 0x02 + (index - 1)  # 虚拟键码：1 -> 0x02, 2 -> 0x03, ..., 9 -> 0x0A
        press_key(keycode)
        release_key(keycode)


# 示例：输入中文
def input_chinese():
    sleep(2)  # 等待用户切换到目标窗口
    type_pinyin("nihao")  # 输入拼音
    select_candidate(1)  # 选择第一个候选字
    type_pinyin("shijie")  # 输入拼音
    select_candidate(1)  # 选择第一个候选字


if __name__ == "__main__":
    input_chinese()
