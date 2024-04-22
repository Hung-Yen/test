import tkinter as tk

# 創建主視窗
root = tk.Tk()
root.title("Hello, World!")  # 視窗標題

# 創建標籤，顯示 "Hello, World!"
label = tk.Label(root, text="Hello, World!", padx=20, pady=20)
label.pack()

# 啟動主迴圈
root.mainloop()
