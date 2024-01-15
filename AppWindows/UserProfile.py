import tkinter
import customtkinter
from tkinter.font import Font
from AppGraphics.Graphics import Graphics
from AppUtilities.Utilities import Utilities
from AppUtilities.WidgetCount import UsedWidgets
class UserProfile():
    def StartFrame(self,root,bg):
        bg.configure(fg_color="#171d25")
        self.username.place(x=300,y=150)
        self.userphoto.place(x=250,y=150)
        UsedWidgets.current.append(self.username)
        UsedWidgets.current.append(self.userphoto)
        self.userprofileopen = True
    def __init__(self,root):
        bold_font = Font(family="Motiva Sans", size=14, weight="bold")
        self.userphoto = customtkinter.CTkLabel(root,height=50,width=50,image=customtkinter.CTkImage(Utilities.GetImages("https://th.bing.com/th/id/OIP.MaDrjtmPQGzKiLHrHEPfFAHaHa?rs=1&pid=ImgDetMain"), size=(50, 50)),text="",bg_color="#171d25")
        self.username = tkinter.Label(root, text=Utilities.Info("username").capitalize(), font=bold_font, bg="#171d25", fg="white")
        self.userprofileopen = False

    def GetStatus(self):
        return self.userprofileopen
    def ClearScreen(self):
        self.username.place_forget()