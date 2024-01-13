import customtkinter
from AppGraphics.Graphics import Graphics
class UserProfile():
    def StartFrame(self,root):
        self.mainFrame = customtkinter.CTkScrollableFrame(root,1000,550,bg_color="grey").place(x=0,y=65)
        self.userprofileopen = True
    def __init__(self):
        self.userprofileopen = False
        try:
            self.mainFrame.destroy()
        except:pass
    def GetStatus(self):
        return self.userprofileopen