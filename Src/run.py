# run.py
import sys
import os

# 确保能导入同目录下的模块
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from main_gui import MainApplication
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    # 可选：设置窗口图标
    try:
        root.iconbitmap("H2O.ico")
    except:
        pass
    app = MainApplication(root)
    root.mainloop()