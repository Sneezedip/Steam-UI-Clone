import tkinter
import customtkinter
from tkinter.font import Font
from AppGraphics.Graphics import Graphics
from AppUtilities.Utilities import Utilities
from AppUtilities.WidgetCount import UsedWidgets
from AppGraphics.OnlineAlocated import Images
from AppUtilities.EditorUtilities import Editor
from AppUtilities.StaticValues import Static
class UserProfile():
    def StartFrame(self,root):
        UsedWidgets.ClearWidgets()
        self.username.grid(column=3,row=4,padx=30,pady=30,sticky="w",columnspan=3);UsedWidgets.current.append(self.username)
        self.userphoto.configure(height=150,width=150,image=customtkinter.CTkImage(Images.userphoto, size=(150, 150)));self.userphoto.place(x=30,y=80);UsedWidgets.current.append(self.userphoto)
        self.c.place(x=699,y=39);UsedWidgets.current.append(self.c)
        self.userlevelLabel.place(x=670,y=85);UsedWidgets.current.append(self.userlevelLabel)
        self.userlevel.place(x=745,y=85);UsedWidgets.current.append(self.userlevel)
        self.description.place(x=220,y=100);UsedWidgets.current.append(self.description)
        self.flag.grid(column=3,row=5);UsedWidgets.current.append(self.flag)
        # self.flaglabel.grid(column=3,row=5,padx=5);UsedWidgets.current.append(self.flaglabel)
        self.editprofileButton.place(x=670,y=200);UsedWidgets.current.append(self.editprofileButton)

        self.userprofileopen = True
    def __init__(self,root):
        bold_font = Font(family="Motiva Sans", size=14, weight="bold")
        self.userbackground = customtkinter.CTkFrame(root,height=125,width=950,bg_color="#272d37",fg_color="#272d37")

        self.description = customtkinter.CTkEntry(root,width=400,height=160,fg_color="#171d25",bg_color="#171d25",border_color="#171d25",text_color="white")
        self.description.insert(0,Utilities.Info("description"))
        self.description.configure(state="disabled")

        self.c = customtkinter.CTkCanvas(root,height=100,background="#171d25",borderwidth=0,highlightbackground="#171d25",highlightthickness=0,insertborderwidth=0)
        self.circle = self.c.create_oval(40,40,80,80,width=1.5,outline=Graphics.GetLevelColor())
        self.userphoto = customtkinter.CTkLabel(root,height=150,width=150,image=customtkinter.CTkImage(Images.userphoto, size=(150, 150)),text="",bg_color="#171d25")
        self.username = tkinter.Label(root, text=Utilities.Info("username"), font=Font(family="Motiva Sans",size=20), bg="#171d25", fg="white")
        self.userlevelLabel = tkinter.Label(root, text=Utilities.Translations("userprofile",1), font=Font(family="Motiva Sans",size=18), bg="#171d25", fg="white")
        self.userlevel = tkinter.Label(root, text=Utilities.Info("level"), font=bold_font, bg="#171d25", fg="white")
        self.flag = customtkinter.CTkLabel(root,height=16,width=16,image=customtkinter.CTkImage(Static.USEDFLAG, size=(16, 16)),text="",bg_color="#171d25")
        self.flaglabel = tkinter.Label(root, text=Static.LABEL, font=Font(family="Motiva Sans",size=10), bg="#171d25", fg="white")



        self.editprofileButton = customtkinter.CTkButton(root,text=Utilities.Translations("userprofile",2),font=("Motiva Sans",14),bg_color="#171d25",width=40,height=30,fg_color="#272d37",hover_color="#3f495a",command= lambda r=root : self.OpenProfileEditor(r))

        self.userprofileopen = False

    def GetStatus(self):
        return self.userprofileopen
    def OpenProfileEditor(self,root):
        self.selected = None
        UsedWidgets.ClearWidgets()
        self.PROFILEEDITORFRAME = customtkinter.CTkScrollableFrame(root,950,300,fg_color="#171d25",bg_color="#171d25")
        self.PROFILEEDITORFRAME.place(x=25,y=200);UsedWidgets.current.append(self.PROFILEEDITORFRAME)
        self.userphoto.configure(height=75,width=75,image=customtkinter.CTkImage(Images.userphoto, size=(75, 75)))
        self.closebutton = customtkinter.CTkButton(root,height=35,width=175,text="Save",bg_color="#171d25",command= lambda r=root:self.SaveChanges(r))
        self.cancelbutton = customtkinter.CTkButton(root,height=35,width=175,text="Cancel",bg_color="#272d37",fg_color="grey",hover_color="white",command= lambda r=root:self.StartFrame(r))

        self.changeusernamelabel = customtkinter.CTkLabel(root,text=Utilities.Info("username"),bg_color="#272d37",fg_color="#272d37",text_color="white",font=("Arial",22))
        self.changeusernamelabel1 = customtkinter.CTkLabel(self.PROFILEEDITORFRAME,text=Utilities.Translations("userprofile",3),bg_color="#171d25",fg_color="#171d25",text_color="white",font=("Arial",18))
        self.changeusername = customtkinter.CTkEntry(self.PROFILEEDITORFRAME,width=600,height=45,corner_radius=5,placeholder_text=Utilities.Info("username"),bg_color="#171d25",fg_color="#171d25",text_color="White")
        
        self.locationslabel = customtkinter.CTkLabel(self.PROFILEEDITORFRAME,text=Utilities.Translations("userprofile",4),bg_color="#171d25",fg_color="#171d25",text_color="white",font=("Arial",18))
        self.changelocation = customtkinter.CTkComboBox(self.PROFILEEDITORFRAME,width=600,height=45,corner_radius=5,bg_color="#272d37",fg_color="#272d37",text_color="white",font=("Arial",18),values=Static.Countries,state="readonly")

        self.changeDescription_Label = customtkinter.CTkLabel(self.PROFILEEDITORFRAME,text="Description",bg_color="#171d25",fg_color="#171d25",text_color="white",font=("Arial",18))
        self.changeDescription = customtkinter.CTkTextbox(self.PROFILEEDITORFRAME,width=600,height=100,corner_radius=5,bg_color="#171d25",fg_color="grey",text_color="White")

        self.userbackground.place(x=25,y=75);UsedWidgets.current.append(self.userbackground)
        self.userphoto.place(x=50,y=100);UsedWidgets.current.append(self.userphoto)

        self.changeusernamelabel.place(x=150,y=125);UsedWidgets.current.append(self.changeusernamelabel)
        self.changeusernamelabel1.grid(column=1,row=0,padx="5px",pady="5px");UsedWidgets.current.append(self.changeusernamelabel1)
        self.changeusername.insert(0, Utilities.Info("username"));self.changeusername.grid(column=2,row=0,padx="5px",pady="5px");UsedWidgets.current.append(self.changeusername)

        self.locationslabel.grid(column=1,row=1,padx="5px",pady="5px");UsedWidgets.current.append(self.locationslabel)
        self.changelocation.grid(column=2,row=1,padx="5px",pady="5px");UsedWidgets.current.append(self.changelocation);self.changelocation.set(Utilities.Info("country").capitalize())

        self.changeDescription_Label.grid(column=1,row=2,padx="5px",pady="5px");
        self.changeDescription.grid(column=2,row=2,padx="5px",pady="5px");
        self.changeDescription.insert("0.0",Utilities.Info("description"))

        self.cancelbutton.place(x=600,y=550);UsedWidgets.current.append(self.cancelbutton)
        self.closebutton.place(x=800,y=550);UsedWidgets.current.append(self.closebutton)
    def SaveChanges(self,root):  
        Editor.SaveChanges(self.changeusername.get(),self.changelocation.get(),self.changeDescription.get('1.0', customtkinter.END))       
        self.new = UserProfile(root)
        self.new.StartFrame(root)

    def ClearScreen(self):
        self.username.place_forget()