import customtkinter
from tkinter.font import Font
from tkinter import Tk, Label
from PIL import Image
import tkinter
from AppUtilities.Utilities import Utilities


class Graphics():
    def LoadIcons(root):
        steamicon = customtkinter.CTkLabel(root,height=18,width=18,image=customtkinter.CTkImage(Utilities.GetImages("https://img.icons8.com/external-those-icons-lineal-color-those-icons/24/external-Steam-social-media-those-icons-lineal-color-those-icons.png"), size=(18, 18)),text="",bg_color="#171d25").place(x=9,y=9)
        closebutton = customtkinter.CTkLabel(root,height=18,width=18,image=customtkinter.CTkImage(Utilities.GetImages("https://cdn-icons-png.flaticon.com/512/10728/10728089.png"), size=(18, 18)),text="",bg_color="#171d25")
        fullscreenbutton = customtkinter.CTkLabel(root,height=18,width=18,image=customtkinter.CTkImage(Utilities.GetImages("https://img.icons8.com/external-dreamstale-lineal-dreamstale/32/external-expand-arrows-dreamstale-lineal-dreamstale-6.png"), size=(18, 18)),text="",bg_color="#171d25").place(x=945,y=5)
        minimizebutton = customtkinter.CTkLabel(root,height=18,width=18,image=customtkinter.CTkImage(Utilities.GetImages("https://img.icons8.com/ios-filled/50/737373/minus-math.png"), size=(18, 18)),text="",bg_color="#171d25").place(x=910,y=5)

        leftarrow = customtkinter.CTkLabel(root,height=18,width=18,image=customtkinter.CTkImage(Utilities.GetImages("https://img.icons8.com/cotton/64/forward.png").transpose(Image.FLIP_LEFT_RIGHT), size=(25, 25)),text="",bg_color="#171d25").place(x=10,y=35)
        rightarrow = customtkinter.CTkLabel(root,height=18,width=18,image=customtkinter.CTkImage(Utilities.GetImages("https://img.icons8.com/cotton/64/forward.png"), size=(25, 25)),text="",bg_color="#171d25").place(x=40,y=35)
        #user
        userphoto = customtkinter.CTkLabel(root,height=25,width=25,image=customtkinter.CTkImage(Utilities.GetImages("https://th.bing.com/th/id/OIP.MaDrjtmPQGzKiLHrHEPfFAHaHa?rs=1&pid=ImgDetMain"), size=(25, 25)),text="",bg_color="#171d25").place(x=745,y=5)
        userbackground = customtkinter.CTkFrame(root,height=25,width=120,bg_color="#272d37",fg_color="#272d37").place(x=770,y=5)
        username = customtkinter.CTkLabel(root,text=Utilities.Info("username"),height=25,font=("Motiva Sans",12),bg_color="#272d37",text_color="#4cb3fe").place(x=775,y=5)
        balance = customtkinter.CTkLabel(root,text=Utilities.Info("balance")+"$",height=25,font=("Motiva Sans",12),bg_color="#272d37",text_color="#67767e").place(x=840,y=5)
        #user
        closebutton.bind("<ButtonPress-1>",exit)
        closebutton.place(x=975,y=5)
    def TopBarTexts(root):
        global tabhover
        #top bar#
        steamText = customtkinter.CTkLabel(root,text="Steam",font=("Motiva Sans",13),bg_color="#171d25",text_color="#858c95")
        viewText = customtkinter.CTkLabel(root,text=Utilities.Translations("bar",1),font=("Motiva Sans",13),bg_color="#171d25",text_color="#858c95")
        friendsText = customtkinter.CTkLabel(root,text=Utilities.Translations("bar",2),font=("Motiva Sans",13),bg_color="#171d25",text_color="#858c95")
        gamesText = customtkinter.CTkLabel(root,text=Utilities.Translations("bar",3),font=("Motiva Sans",13),bg_color="#171d25",text_color="#858c95")
        helpText = customtkinter.CTkLabel(root,text=Utilities.Translations("bar",4),font=("Motiva Sans",13),bg_color="#171d25",text_color="#858c95")
        #top bar#


        tabhover = customtkinter.CTkFrame(root,height=4,width=67,bg_color="#272d37",fg_color="#1891e7")
        #CONFIG HOVERING COLORS
        viewText.bind("<Enter>", lambda event: event.widget.config(fg="white"))
        viewText.bind("<Leave>", lambda event: event.widget.config(fg="#858c95"))
        friendsText.bind("<Enter>", lambda event: event.widget.config(fg="white"))
        friendsText.bind("<Leave>", lambda event: event.widget.config(fg="#858c95"))
        gamesText.bind("<Enter>", lambda event: event.widget.config(fg="white"))
        gamesText.bind("<Leave>", lambda event: event.widget.config(fg="#858c95"))
        helpText.bind("<Enter>", lambda event: event.widget.config(fg="white"))
        helpText.bind("<Leave>", lambda event: event.widget.config(fg="#858c95"))
        #CONFIG HOVERING COLORS

        steamText.place(x=35,y=4)
        viewText.place(x=100,y=4)
        friendsText.place(x=140,y=4)
        gamesText.place(x=200,y=4)
        helpText.place(x=255,y=4)