import customtkinter
from AppUtilities.utilities import Utilities

class Store():
    def StartDrag(self,event):
            global x,y
            x = event.x
            y = event.y
    def MoveWindow(self,event):
        new_x = (self.root.winfo_x() + event.x) - x
        new_y = (self.root.winfo_y() + event.y) - y
        self.root.geometry(f"+{new_x}+{new_y}")
    def LoadIcons(self):
        self.steamicon = customtkinter.CTkLabel(self.root,height=18,width=18,image=customtkinter.CTkImage(Utilities.GetImages("https://img.icons8.com/external-those-icons-lineal-color-those-icons/24/external-Steam-social-media-those-icons-lineal-color-those-icons.png"), size=(18, 18)),text="",bg_color="#171d25").place(x=9,y=9)
        self.closebutton = customtkinter.CTkLabel(self.root,height=18,width=18,image=customtkinter.CTkImage(Utilities.GetImages("https://img.icons8.com/material-two-tone/24/delete-sign.png"), size=(18, 18)),text="",bg_color="#171d25")
        self.fullscreenbutton = customtkinter.CTkLabel(self.root,height=18,width=18,image=customtkinter.CTkImage(Utilities.GetImages("https://img.icons8.com/ios/50/full-screen--v1.png"), size=(18, 18)),text="",bg_color="#171d25").place(x=945,y=5)
        self.fullscreenbutton = customtkinter.CTkLabel(self.root,height=18,width=18,image=customtkinter.CTkImage(Utilities.GetImages("https://img.icons8.com/ios-glyphs/30/horizontal-line.png"), size=(18, 18)),text="",bg_color="#171d25").place(x=910,y=5)
        #user
        self.userphoto = customtkinter.CTkLabel(self.root,height=25,width=25,image=customtkinter.CTkImage(Utilities.GetImages("https://th.bing.com/th/id/OIP.MaDrjtmPQGzKiLHrHEPfFAHaHa?rs=1&pid=ImgDetMain"), size=(25, 25)),text="",bg_color="#171d25").place(x=745,y=5)
        self.userbackground = customtkinter.CTkFrame(self.root,height=25,width=120,bg_color="#272d37",fg_color="#272d37").place(x=770,y=5)
        self.username = customtkinter.CTkLabel(self.root,text="Default",height=25,font=("Motiva Sans",14),bg_color="#272d37",text_color="#4cb3fe").place(x=773,y=5)
        #user
        self.closebutton.bind("<ButtonPress-1>",exit)
        self.closebutton.place(x=975,y=5)
    def LoadTexts(self):
        background = customtkinter.CTkFrame(self.root,height=1000,width=1000,bg_color="#171d25",fg_color="#171d25")
        title_bar = customtkinter.CTkFrame(self.root,height=50,width=1000,bg_color="#171d25",fg_color="#171d25")
        title_bar.bind("<ButtonPress-1>",self.StartDrag)
        title_bar.bind("<B1-Motion>",self.MoveWindow)

        steamText = customtkinter.CTkLabel(self.root,text="Steam",font=("Motiva Sans",13),bg_color="#171d25",text_color="#858c95")
        seeText = customtkinter.CTkLabel(self.root,text=Utilities.Translations("bar",1),font=("Motiva Sans",13),bg_color="#171d25",text_color="#858c95")
        friendsText = customtkinter.CTkLabel(self.root,text=Utilities.Translations("bar",2),font=("Motiva Sans",13),bg_color="#171d25",text_color="#858c95")
        gamesText = customtkinter.CTkLabel(self.root,text=Utilities.Translations("bar",3),font=("Motiva Sans",13),bg_color="#171d25",text_color="#858c95")
        helpText = customtkinter.CTkLabel(self.root,text=Utilities.Translations("bar",4),font=("Motiva Sans",13),bg_color="#171d25",text_color="#858c95")

        background.place(x=0,y=0)
        title_bar.place(x=0,y=0)
        steamText.place(x=35,y=4)
        seeText.place(x=100,y=4)
        friendsText.place(x=140,y=4)
        gamesText.place(x=200,y=4)
        helpText.place(x=255,y=4)
    def __init__(self):
        self.hasstyle = False
        self.root = customtkinter.CTk()
        self.root.geometry("1000x600")
        self.root.update_idletasks()
        self.root.withdraw()
        self.root.overrideredirect(True)
        self.root.title('Steam')
        self.root.update_idletasks()
        self.LoadTexts()
        self.LoadIcons()
        Utilities.BottomIcon(self.root,self.hasstyle)
        self.root.mainloop()

Store()
