import customtkinter
class Store():
    def StartFrame(self,root,bg):
        bg.configure(fg_color="#171d25")
        self.storeopen = True
    def __init__(self):
        self.storeopen = False
        try:
            self.mainFrame.destroy()
        except:pass
    def GetStatus(self):
        return self.storeopen