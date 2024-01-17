from ctypes import windll
import ctypes
import requests
from PIL import Image
from io import BytesIO
import tkinter.messagebox as mbox
import json

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
        with open("AppConfig/app.cfg","r") as file:
            lines = file.readlines()
            for line in lines:
                separate = line.split("=")
                if len(separate) == 2 and separate[0].strip() == info:
                    return separate[1].strip()
    def Translations(section,id):
        with open("AppConfig/language.json" , "r") as file:
            json_data = file.read()
        data = json.loads(json_data)
        translation_language = data["translations"][Utilities.Info("language")]
        bar_translations = translation_language[0]["bar"]
        userprofile_translations = translation_language[0]["userprofile"]
        match section:
            case "bar": return next(item["text"] for item in bar_translations if item["id"] == id) 
            case "userprofile": return next(item["text"] for item in userprofile_translations if item["id"] == id) 
    def Positions(id,tabhover):
        with open("AppConfig/pos.json" , "r") as file:
            json_data = file.read()
        data = json.loads(json_data)
        positions = data["positions"][Utilities.Info("language")]
        pos = positions[0]["tabhover"]

        tabhover.configure(width = next(item["width"] for item in pos if item["id"]==id))
        tabhover.place(x = next(item["place_x"] for item in pos if item["id"]==id),y=60)  