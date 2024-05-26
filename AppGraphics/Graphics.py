import customtkinter
from PIL import Image
from AppUtilities.Utilities import Utilities
from AppUtilities.StaticValues import Static

class Graphics():
    def LoadIcons(root):
        steamicon = customtkinter.CTkLabel(root,height=18,width=18,image=customtkinter.CTkImage(Utilities.GetImages("https://img.icons8.com/external-those-icons-lineal-color-those-icons/24/external-Steam-social-media-those-icons-lineal-color-those-icons.png"), size=(18, 18)),text="",bg_color="#171d25").grid(column=0,row=0,padx=15)
        closebutton = customtkinter.CTkLabel(root,height=18,width=18,image=customtkinter.CTkImage(Utilities.GetImages("https://cdn-icons-png.flaticon.com/512/10728/10728089.png"), size=(18, 18)),text="",bg_color="#171d25")
        fullscreenbutton = customtkinter.CTkLabel(root,height=18,width=18,image=customtkinter.CTkImage(Utilities.GetImages("https://img.icons8.com/external-dreamstale-lineal-dreamstale/32/external-expand-arrows-dreamstale-lineal-dreamstale-6.png"), size=(18, 18)),text="",bg_color="#171d25").place(x=945,y=5)
        minimizebutton = customtkinter.CTkLabel(root,height=18,width=18,image=customtkinter.CTkImage(Utilities.GetImages("https://img.icons8.com/ios-filled/50/737373/minus-math.png"), size=(18, 18)),text="",bg_color="#171d25").place(x=910,y=5)

        leftarrow = customtkinter.CTkLabel(root,height=18,width=18,image=customtkinter.CTkImage(Utilities.GetImages("https://img.icons8.com/cotton/64/forward.png").transpose(Image.FLIP_LEFT_RIGHT), size=(25, 25)),text="",bg_color="#171d25").place(x=10,y=35)
        rightarrow = customtkinter.CTkLabel(root,height=18,width=18,image=customtkinter.CTkImage(Utilities.GetImages("https://img.icons8.com/cotton/64/forward.png"), size=(25, 25)),text="",bg_color="#171d25").place(x=40,y=35)
        #user
        userphoto = customtkinter.CTkLabel(root,height=25,width=25,image=customtkinter.CTkImage(Utilities.GetImages("https://th.bing.com/th/id/OIP.MaDrjtmPQGzKiLHrHEPfFAHaHa?rs=1&pid=ImgDetMain"), size=(25, 25)),text="",bg_color="#171d25").place(x=745,y=5)
        userbackground = customtkinter.CTkFrame(root,height=25,width=120,bg_color="#272d37",fg_color="#272d37").place(x=770,y=5)
        Static.username = customtkinter.CTkLabel(root,text=Utilities.Info("username"),height=25,font=("Motiva Sans",12),bg_color="#272d37",text_color="#4cb3fe")
        balance = customtkinter.CTkLabel(root,text=Utilities.Info("balance")+"$",height=25,font=("Motiva Sans",12),bg_color="#272d37",text_color="#67767e").place(x=840,y=5)
        #user
        closebutton.bind("<ButtonPress-1>",exit)
        Static.username.place(x=775,y=5)
        closebutton.place(x=975,y=5)
    def TopBarTexts(root):
        topbartexts = []
        #top bar#
        steamText = customtkinter.CTkLabel(root,text="Steam",font=("Motiva Sans",13),bg_color="#171d25",text_color="#858c95")
        viewText = customtkinter.CTkLabel(root,text=Utilities.Translations("bar",1),font=("Motiva Sans",13),bg_color="#171d25",text_color="#858c95");topbartexts.append(viewText)
        friendsText = customtkinter.CTkLabel(root,text=Utilities.Translations("bar",2),font=("Motiva Sans",13),bg_color="#171d25",text_color="#858c95");topbartexts.append(friendsText)
        gamesText = customtkinter.CTkLabel(root,text=Utilities.Translations("bar",3),font=("Motiva Sans",13),bg_color="#171d25",text_color="#858c95");topbartexts.append(gamesText)
        helpText = customtkinter.CTkLabel(root,text=Utilities.Translations("bar",4),font=("Motiva Sans",13),bg_color="#171d25",text_color="#858c95");topbartexts.append(helpText)
        #top bar#

        for texts in topbartexts:
            try:
                texts.bind("<Enter>", lambda event: ChangeEvent_Enter(event))  #Fix for -fg errors! V.1.1.8
                texts.bind("<Leave>", lambda event: ChangeEvent_Leave(event))  #Fix for -fg errors! V.1.1.8
            except:pass

        steamText.grid(column=1,row=0,padx=5,pady=2)
        viewText.grid(column=2,row=0,padx=10,pady=2)
        friendsText.grid(column=3,row=0,padx=10,pady=2)
        gamesText.grid(column=4,row=0,padx=10,pady=2)
        helpText.grid(column=5,row=0,padx=10,pady=2)

        #Fix for -fg errors! V.1.1.8
        def ChangeEvent_Enter(event):
            try: event.widget.config(fg="white")
            except: pass
        def ChangeEvent_Leave(event):
            try: event.widget.config(fg="#858c95")
            except: pass
    def GetLevelColor():
        level = int(Utilities.Info("level"))
        if level >= 0 and level <= 9:
            return "grey"
        elif level >= 10 and level <= 19:
            return "red"
        elif level >= 20 and level <= 29:
            return "orange"
        elif level >= 30 and level <= 39:
            return "yellow"
        elif level >= 40 and level <= 49:
            return "green"
        elif level >= 50 and level <= 59:
            return "blue"
        elif level >= 60 and level <= 69:
            return "purple"
        else:
            return "grey"
        
        