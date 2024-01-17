from ast import Load
from logging import root
from AppWindows.Community import Community
from AppWindows.Library import Library
from AppWindows.Store import Store
from AppWindows.UserProfile import UserProfile
from AppGraphics.Graphics import Graphics
from AppUtilities.Utilities import Utilities
import customtkinter
from tkinter.font import Font
from tkinter import Tk, Label
from PIL import Image
import tkinter
from AppUtilities.Utilities import Utilities
import customtkinter
import json
from AppUtilities.WidgetCount import UsedWidgets
from AppGraphics.OnlineAlocated import Images
class Main():
    class Auto():
        Iter = 0
    def FirstCheck(self):
        if Main.Auto.Iter == 0:
            self.storestat = Store()
            self.librarystat = Library()
            self.communitystat = Community()
            self.userprofilestat = UserProfile(self.root)
            self.background = customtkinter.CTkFrame(self.root,height=1000,width=1000,bg_color="#171d25",fg_color="#171d25")
            self.background.place(x=0,y=0) 
            Images()     
        Main.Auto.Iter += 1

    def ClearColors(self):
        self.store.configure(fg="white" if not self.storestat.GetStatus() else "#1891e7")
        self.library.configure(fg="white" if not self.librarystat.GetStatus() else "#1891e7")
        self.community.configure(fg="white" if not self.communitystat.GetStatus() else "#1891e7")
        self.userprofile.configure(fg="white" if not self.userprofilestat.GetStatus() else "#1891e7")   

        if self.storestat.GetStatus():
            Utilities.Positions(1,self.tabhover)
        elif self.librarystat.GetStatus():
            Utilities.Positions(2,self.tabhover)
        elif self.communitystat.GetStatus():
            Utilities.Positions(3,self.tabhover)
        elif self.userprofilestat.GetStatus():
            self.tabhover.place_forget()
    def CheckEntry(self,event,obj):
        if len(UsedWidgets.current) >= 1:
            for widgets in UsedWidgets.current:
                widgets.place_forget()
        self.storestat = Store()
        self.librarystat = Library()
        self.communitystat = Community()
        self.userprofilestat = UserProfile(self.root)
        self.userprofilestat.ClearScreen()
        if obj == "Store":
            self.storestat.StartFrame(self.root,self.background)
        elif obj == "Library":
            self.librarystat.StartFrame(self.root,self.background)
        elif obj == "Community":
            self.communitystat.StartFrame(self.root,self.background)
        elif obj == "UserProfile":
            self.userprofilestat.StartFrame(self.root,self.background)
        self.ClearColors()
    def StartDrag(self,event):
            global x,y
            x = event.x
            y = event.y

    def MoveWindow(self,event):
        new_x = (self.root.winfo_x() + event.x) - x
        new_y = (self.root.winfo_y() + event.y) - y
        self.root.geometry(f"+{new_x}+{new_y}")

    def LoadTopBar(self):
        bold_font = Font(family="Motiva Sans", size=14, weight="bold")

        title_bar = customtkinter.CTkFrame(self.root,height=50,width=1000,bg_color="#171d25",fg_color="#171d25")
        title_bar.bind("<ButtonPress-1>",self.StartDrag)
        title_bar.bind("<B1-Motion>",self.MoveWindow)

        self.store = tkinter.Label(self.root, text=Utilities.Translations("bar",5).upper(), font=bold_font, bg="#171d25", fg="white" if not self.storestat.GetStatus() else "#1891e7")
        self.library = tkinter.Label(self.root,text=Utilities.Translations("bar",6).upper(),font=bold_font,bg="#171d25",fg="white" if not self.librarystat.GetStatus() else "#1891e7")
        self.community = tkinter.Label(self.root,text=Utilities.Translations("bar",7).upper(),font=bold_font,bg="#171d25",fg="white" if not self.communitystat.GetStatus() else "#1891e7")
        self.userprofile = tkinter.Label(self.root,text=Utilities.Info("username").upper(),font=bold_font,bg="#171d25",fg="white" if not self.userprofilestat.GetStatus() else "#1891e7")
        self.tabhover = customtkinter.CTkFrame(self.root,height=4,width=67,bg_color="#1891e7",fg_color="#1891e7")

        title_bar.place(x=0,y=0)

        self.store.bind("<ButtonPress-1>",lambda event,obj="Store": self.CheckEntry(event, obj))
        self.library.bind("<ButtonPress-1>",lambda event, obj="Library": self.CheckEntry(event, obj))
        self.community.bind("<ButtonPress-1>",lambda event, obj="Community": self.CheckEntry(event, obj))
        self.userprofile.bind("<ButtonPress-1>",lambda event, obj="UserProfile": self.CheckEntry(event, obj))

        self.store.place(x=90,y=33)
        self.library.place(x=160,y=33) if Utilities.Info("language") == "portuguese" else self.library.place(x=185,y=33)
        self.community.place(x=295,y=33)
        self.userprofile.place(x=445,y=33)

        self.storestat.StartFrame(self.root,self.background)

        self.ClearColors()

    def __init__(self):
        self.hasstyle = False

        self.root = customtkinter.CTk()
        self.FirstCheck()

        self.root.geometry("1000x600")
        self.root.title('Steam')
        self.root.overrideredirect(True)
        self.LoadTopBar()
        Graphics.TopBarTexts(self.root)
        Graphics.LoadIcons(self.root)
        Utilities.BottomIcon(self.root,self.hasstyle)
        self.root.mainloop()

Main()