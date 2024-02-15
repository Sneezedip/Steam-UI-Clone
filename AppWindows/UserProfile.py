import tkinter
import customtkinter
from tkinter.font import Font
from AppGraphics.Graphics import Graphics
from AppUtilities.Utilities import Utilities
from AppUtilities.WidgetCount import UsedWidgets
from AppGraphics.OnlineAlocated import Images
class UserProfile():
    def StartFrame(self,root):
        UsedWidgets.ClearWidgets()
        self.username.place(x=220,y=80);UsedWidgets.current.append(self.username)
        self.userphoto.place(x=30,y=80);UsedWidgets.current.append(self.userphoto)
        self.c.place(x=699,y=39);UsedWidgets.current.append(self.c)
        self.userlevelLabel.place(x=670,y=85);UsedWidgets.current.append(self.userlevelLabel)
        self.userlevel.place(x=745,y=85);UsedWidgets.current.append(self.userlevel)
        self.flag.place(x=225,y=120);UsedWidgets.current.append(self.flag)
        self.flaglabel.place(x=245,y=117);UsedWidgets.current.append(self.flaglabel)
        self.editprofileButton.place(x=670,y=200);UsedWidgets.current.append(self.editprofileButton)
        self.userprofileopen = True
    def __init__(self,root):
        bold_font = Font(family="Motiva Sans", size=14, weight="bold")
        self.c = customtkinter.CTkCanvas(root,height=100,background="#171d25",borderwidth=0,highlightbackground="#171d25",highlightthickness=0,insertborderwidth=0)
        self.circle = self.c.create_oval(40,40,80,80,width=1.5,outline=Graphics.GetLevelColor())
        self.userphoto = customtkinter.CTkLabel(root,height=150,width=150,image=customtkinter.CTkImage(Images.userphoto, size=(150, 150)),text="",bg_color="#171d25")
        self.username = tkinter.Label(root, text=Utilities.Info("username").capitalize(), font=Font(family="Motiva Sans",size=20), bg="#171d25", fg="white")
        self.userlevelLabel = tkinter.Label(root, text=Utilities.Translations("userprofile",1), font=Font(family="Motiva Sans",size=18), bg="#171d25", fg="white")
        self.userlevel = tkinter.Label(root, text=Utilities.Info("level"), font=bold_font, bg="#171d25", fg="white")
        self.flag = customtkinter.CTkLabel(root,height=16,width=16,image=customtkinter.CTkImage(Images.USEDFLAG, size=(16, 16)),text="",bg_color="#171d25")
        self.flaglabel = tkinter.Label(root, text=Images.LABEL, font=Font(family="Motiva Sans",size=10), bg="#171d25", fg="white")


        self.editprofileButton = customtkinter.CTkButton(root,text=Utilities.Translations("userprofile",2),font=("Motiva Sans",14),bg_color="#171d25",width=40,height=30,fg_color="#272d37",hover_color="#3f495a",command= lambda r=root : self.OpenProfileEditor(r))

        self.userprofileopen = False

    def GetStatus(self):
        return self.userprofileopen
    def OpenProfileEditor(self,root):
        UsedWidgets.ClearWidgets()

        self.closebutton = customtkinter.CTkButton(root,height=50,width=80,text="Save",bg_color="#171d25",command= lambda r=root:self.SaveChanges(r))
        self.changeusernamelabel = customtkinter.CTkLabel(root,text="Username",bg_color="#171d25",fg_color="#171d25",text_color="white",font=("Arial",16,"bold"))
        self.changeusername = customtkinter.CTkEntry(root,width=100,height=35,corner_radius=5,placeholder_text=Utilities.Info("username"),bg_color="#171d25",fg_color="#171d25",text_color="White")
        
        self.changeusernamelabel.place(x=150,y=80);UsedWidgets.current.append(self.changeusernamelabel)
        self.changeusername.place(x=240,y=80);UsedWidgets.current.append(self.changeusername)
        self.closebutton.place(x=220,y=200);UsedWidgets.current.append(self.closebutton)
        
    def SaveChanges(self,root):
        self.changes = []
        with open("AppConfig/app.cfg","r") as fileread:
            for line in fileread.readlines():
                if str(line.strip()) == "username="+Utilities.Info("username"):
                    self.changes.append("username="+self.changeusername.get()+"\n")
                else:
                    self.changes.append(str(line.strip()+"\n"))
        with open("AppConfig/app.cfg","w")  as file:
            for change in self.changes:
                file.write(str(change))
            
        self.StartFrame(root)
    def ClearScreen(self):
        self.username.place_forget()