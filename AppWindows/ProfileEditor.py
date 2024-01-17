from cgitb import text
import tkinter
from tkinter import font
from turtle import bgcolor
import customtkinter
from tkinter.font import Font
from AppGraphics.Graphics import Graphics
from AppUtilities.Utilities import Utilities
from AppUtilities.WidgetCount import UsedWidgets
from AppGraphics.OnlineAlocated import Images
class ProfileEditor():
    def StartFrame(self,root,bg):
        bg.configure(fg_color="#171d25")
        self.username.place(x=220,y=80);UsedWidgets.current.append(self.username)
        self.profileedit = True
    def __init__(self,root):
        bold_font = Font(family="Motiva Sans", size=14, weight="bold")
        self.userphoto = customtkinter.CTkLabel(root,height=150,width=150,image=customtkinter.CTkImage(Images.userphoto, size=(150, 150)),text="",bg_color="#171d25")


        self.profileedit = False

    def GetStatus(self):
        return self.userprofileopen
    def ClearScreen(self):
        self.username.place_forget()