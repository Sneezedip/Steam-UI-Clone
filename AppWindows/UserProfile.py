import customtkinter
from AppGraphics.Graphics import Graphics
class UserProfile():
    def StartFrame(self,root,bg):
        bg.configure(fg_color="#171d25")
        self.userprofileopen = True
    def __init__(self):
        self.userprofileopen = False
        try:
            self.mainFrame.destroy()
        except:pass
    def GetStatus(self):
        return self.userprofileopen