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
class Main():
    def StartDrag(self,event):
            global x,y
            x = event.x
            y = event.y

    def MoveWindow(self,event):
        new_x = (self.root.winfo_x() + event.x) - x
        new_y = (self.root.winfo_y() + event.y) - y
        self.root.geometry(f"+{new_x}+{new_y}")

    def LoadTopBar(self):
        self.storestat.StartFrame(self.root)
        bold_font = Font(family="Motiva Sans", size=14, weight="bold")

        background = customtkinter.CTkFrame(self.root,height=1000,width=1000,bg_color="#171d25",fg_color="#171d25")
        title_bar = customtkinter.CTkFrame(self.root,height=50,width=1000,bg_color="#171d25",fg_color="#171d25")
        title_bar.bind("<ButtonPress-1>",self.StartDrag)
        title_bar.bind("<B1-Motion>",self.MoveWindow)

        store = tkinter.Label(self.root, text=Utilities.Translations("bar",5).upper(), font=bold_font, bg="#171d25", fg="white" if not self.storestat.GetStatus() else "#1891e7")
        library = tkinter.Label(self.root,text=Utilities.Translations("bar",6).upper(),font=bold_font,bg="#171d25",fg="white" if not self.librarystat.GetStatus() else "#1891e7")
        community = tkinter.Label(self.root,text=Utilities.Translations("bar",7).upper(),font=bold_font,bg="#171d25",fg="white" if not self.communitystat.GetStatus() else "#1891e7")
        userprofile = tkinter.Label(self.root,text=Utilities.Info("username").upper(),font=bold_font,bg="#171d25",fg="white" if not self.userprofilestat.GetStatus() else "#1891e7")
        tabhover = customtkinter.CTkFrame(self.root,height=4,width=67,bg_color="#1891e7",fg_color="#1891e7")

        background.place(x=0,y=0)
        title_bar.place(x=0,y=0)
        store.place(x=90,y=33)
        library.place(x=160,y=33) if Utilities.Info("language") == "portuguese" else library.place(x=185,y=33)
        community.place(x=295,y=33)
        userprofile.place(x=445,y=33)

        if self.storestat.GetStatus():
            Utilities.Positions(1,tabhover)
        elif self.librarystat.GetStatus():
            Utilities.Positions(2,tabhover)
        elif self.communitystat.GetStatus():
            Utilities.Positions(3,tabhover)
        elif self.userprofilestat.GetStatus():
            tabhover.destroy()

    def __init__(self):

        self.librarystat = Library()
        self.storestat = Store()
        self.communitystat = Community()
        self.userprofilestat = UserProfile()

        self.hasstyle = False

        self.root = customtkinter.CTk()

        self.root.geometry("1000x600")
        self.root.title('Steam')
        self.root.update_idletasks()
        self.root.withdraw()
        self.root.overrideredirect(True)
        self.root.update_idletasks()
        self.LoadTopBar()
        Graphics.TopBarTexts(self.root)
        Graphics.LoadIcons(self.root)
        Utilities.BottomIcon(self.root,self.hasstyle)
        self.root.mainloop()

Main()