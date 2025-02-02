import tkinter
import pandas as pd


class FileManager:
    def __init__(self):
        pass
    


class Recorder:
    def __init__(self):
        self.cmd=[]
        self.tk = tkinter.Tk()
        self.key = 0
        # self.flag = 0#0:none 1:record 2:execute
        self.toggle_record=False
        self.toggle_exe = False
        self.onInput = False

        self.tk.title("Macro")
        self.tk.bind("<KeyPress>",self.key_down)
        self.tk.bind("<KeyRelease>",self.key_up)

        self.tk.bind("<Button-1>",self.button_1)#마우스 왼쪽
        self.tk.bind("<Button-2>",self.button_2)#마우스 중간
        self.tk.bind("<Button-3>",self.button_3)#마우스 오른쪽
        self.tk.bind("<Button-4>",self.button_4)#휠 업
        self.tk.bind("<Button-5>",self.button_5)#휠 다운

        


        #캔버스
        self.canvas = tkinter.Canvas(width=800, height=600)
        self.canvas.pack()
        #텍스트 출력
        self.label = tkinter.Label(font=("Times New Roman", 80))
        self.label.pack()
        self.gram = {'down':'▼', 'up':'▲', 'mlb':'◁', 'mrb':'▷', 'move':'◈', 'scroll':'↕'}



    def key_down(self,e):
        self.key = e.keysym # 눌려진 키 이름을 key에 대입
        self.onInput=True
    def key_up(self, e):
        self.key = e.keysym
        self.onInput = True
    def button_1(self,e):
        pass


    def main_loop(self):
        if(self.onInput==True):
            #시작/정지
            if self.key=="Up":
                self.toggle_exe=False
                if self.toggle_record==True: self.toggle_record=False
                else : self.toggle_record=True
                return
            elif self.key=="Down":
                self.toggle_record=False
                if self.toggle_exe==True:self.toggle_exe=False
                else : self.toggle_exe=True
                return


            if(self.toggle_record==True):
                self.cmd.append(str(self.key)+'▽,')

            self.label['text']=self.cmd
            self.onInput=False


    def main(self):
        # if(self.flag==1):
        #     self.record()
        # elif(self.flag==1):
        #     self.execute()
        # self.tk.after(100,self.main())#저장되는 ms에 100초 나누기 해야 함.
        
        self.main_loop()
        
        self.tk.mainloop()

        
        pass


rec = Recorder()
rec.main()