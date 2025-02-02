
import pyautogui
import tkinter

class Macro:
    def __init__(self):
        self.recorder = Recorder()
    



class Recorder:
    def __init__(self):
        self.cmd = []
        self.tk = tkinter.Tk()


    def key_down(e):
        global key
        key=e.keycode
        print(f"key:{key}")


    def main(self):
        self.tk.title('get key code ')
        #실시간 키 입력
        self.tk.bind("<KeyPress>", self.key_down)
    
        self.tk.mainloop()



class Recorder:
    def __init__(self):
        pass