import customtkinter
from AppGraphics.Graphics import Graphics
class Library():
    def StartFrame(self,root,bg):
        bg.configure(fg_color="#171d25")
        self.libraryopen = True
    def __init__(self):
        self.libraryopen = False
        try:
            self.mainFrame.destroy()
        except:pass
    def GetStatus(self):
        return self.libraryopen