from ctypes import windll
import ctypes
import requests
from PIL import Image
from io import BytesIO
import tkinter.messagebox as mbox
import json
import customtkinter
class Utilities():
    def BottomIcon(root,hasstyle):
        GWL_EXSTYLE=-20
        WS_EX_APPWINDOW=0x00040000
        WS_EX_TOOLWINDOW=0x00000080
        if not hasstyle:
            hwnd = windll.user32.GetParent(root.winfo_id())
            style = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
            style = style & ~WS_EX_TOOLWINDOW
            style = style | WS_EX_APPWINDOW
            res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style)
            root.withdraw()
            root.after(10, lambda:root.wm_deiconify())
            region = ctypes.windll.gdi32.CreateRoundRectRgn(0, 0, root.winfo_width(), root.winfo_height(), 10, 10)
            ctypes.windll.user32.SetWindowRgn(hwnd, region, True)
            hasstyle=True
    def GetImages(url):
        response = requests.get(url)
        if response.status_code == 200:
            return Image.open(BytesIO(response.content))
        else:
            mbox.showerror(title="Steam",message="Failed to retrieve data. Contact .sneezedip")
            exit()
    def Info(info):
        with open("app.cfg","r") as file:
            lines = file.readlines()
            for line in lines:
                separate = line.split("=")
                if len(separate) == 2 and separate[0].strip() == info:
                    return separate[1].strip()
    def Translations(section,id):
        with open("language.json" , "r") as file:
            json_data = file.read()
        data = json.loads(json_data)
        translation_language = data["translations"][Utilities.Info("language")]
        bar_translations = translation_language[0]["bar"]

        match section:
            case "bar": return next(item["text"] for item in bar_translations if item["id"] == id)
    def LoadIcons(root):
        steamicon = customtkinter.CTkLabel(root,height=18,width=18,image=customtkinter.CTkImage(Utilities.GetImages("https://img.icons8.com/external-those-icons-lineal-color-those-icons/24/external-Steam-social-media-those-icons-lineal-color-those-icons.png"), size=(18, 18)),text="",bg_color="#171d25").place(x=9,y=9)
        closebutton = customtkinter.CTkLabel(root,height=18,width=18,image=customtkinter.CTkImage(Utilities.GetImages("https://img.icons8.com/material-two-tone/24/delete-sign.png"), size=(18, 18)),text="",bg_color="#171d25")
        fullscreenbutton = customtkinter.CTkLabel(root,height=18,width=18,image=customtkinter.CTkImage(Utilities.GetImages("https://img.icons8.com/ios/50/full-screen--v1.png"), size=(18, 18)),text="",bg_color="#171d25").place(x=945,y=5)
        minimizebutton = customtkinter.CTkLabel(root,height=18,width=18,image=customtkinter.CTkImage(Utilities.GetImages("https://img.icons8.com/ios-glyphs/30/horizontal-line.png"), size=(18, 18)),text="",bg_color="#171d25").place(x=910,y=5)
        #user
        userphoto = customtkinter.CTkLabel(root,height=25,width=25,image=customtkinter.CTkImage(Utilities.GetImages("https://th.bing.com/th/id/OIP.MaDrjtmPQGzKiLHrHEPfFAHaHa?rs=1&pid=ImgDetMain"), size=(25, 25)),text="",bg_color="#171d25").place(x=745,y=5)
        userbackground = customtkinter.CTkFrame(root,height=25,width=120,bg_color="#272d37",fg_color="#272d37").place(x=770,y=5)
        username = customtkinter.CTkLabel(root,text=Utilities.Info("username"),height=25,font=("Motiva Sans",12),bg_color="#272d37",text_color="#4cb3fe").place(x=775,y=5)
        balance = customtkinter.CTkLabel(root,text=Utilities.Info("balance")+"$",height=25,font=("Motiva Sans",12),bg_color="#272d37",text_color="#67767e").place(x=840,y=5)
        #user
        closebutton.bind("<ButtonPress-1>",exit)
        closebutton.place(x=975,y=5)
    def TopBarTexts(root):
        steamText = customtkinter.CTkLabel(root,text="Steam",font=("Motiva Sans",13),bg_color="#171d25",text_color="#858c95")
        seeText = customtkinter.CTkLabel(root,text=Utilities.Translations("bar",1),font=("Motiva Sans",13),bg_color="#171d25",text_color="#858c95")
        friendsText = customtkinter.CTkLabel(root,text=Utilities.Translations("bar",2),font=("Motiva Sans",13),bg_color="#171d25",text_color="#858c95")
        gamesText = customtkinter.CTkLabel(root,text=Utilities.Translations("bar",3),font=("Motiva Sans",13),bg_color="#171d25",text_color="#858c95")
        helpText = customtkinter.CTkLabel(root,text=Utilities.Translations("bar",4),font=("Motiva Sans",13),bg_color="#171d25",text_color="#858c95")

        steamText.place(x=35,y=4)
        seeText.place(x=100,y=4)
        friendsText.place(x=140,y=4)
        gamesText.place(x=200,y=4)
        helpText.place(x=255,y=4)
        