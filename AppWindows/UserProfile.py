import tkinter
import customtkinter
from tkinter.font import Font
from AppGraphics.Graphics import Graphics
from AppUtilities.Utilities import Utilities
from AppUtilities.WidgetCount import UsedWidgets
from AppGraphics.OnlineAlocated import Images
class UserProfile():
    def StartFrame(self,root,bg):
        bg.configure(fg_color="#171d25")
        self.username.place(x=220,y=80)
        self.userphoto.place(x=30,y=80)
        UsedWidgets.current.append(self.username)
        UsedWidgets.current.append(self.userphoto)
        self.userprofileopen = True
    def __init__(self,root):
        bold_font = Font(family="Motiva Sans", size=14, weight="bold")
        self.userphoto = customtkinter.CTkLabel(root,height=150,width=150,image=customtkinter.CTkImage(Images.userphoto, size=(150, 150)),text="",bg_color="#171d25")
        self.username = tkinter.Label(root, text=Utilities.Info("username").capitalize(), font=Font(family="Motiva Sans",size=20), bg="#171d25", fg="white")
        self.userprofileopen = False

    def GetStatus(self):
        return self.userprofileopen
    def ClearScreen(self):
        self.username.place_forget()