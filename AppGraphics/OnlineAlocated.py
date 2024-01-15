import customtkinter
from PIL import Image
from AppUtilities.Utilities import Utilities
class Images():
    def Loaded(self):
        self.steamicon = Utilities.GetImages("https://img.icons8.com/external-those-icons-lineal-color-those-icons/24/external-Steam-social-media-those-icons-lineal-color-those-icons.png")
        self.closebutton = Utilities.GetImages("https://cdn-icons-png.flaticon.com/512/10728/10728089.png")
        self.fullscreenbutton = Utilities.GetImages("https://img.icons8.com/external-dreamstale-lineal-dreamstale/32/external-expand-arrows-dreamstale-lineal-dreamstale-6.png")
        self.minimizebutton = Utilities.GetImages("https://img.icons8.com/ios-filled/50/737373/minus-math.png")
        self.leftarrow = Utilities.GetImages("https://img.icons8.com/cotton/64/forward.png")
        self.rightarrow = Utilities.GetImages("https://img.icons8.com/cotton/64/forward.png")
        self.userphoto = Utilities.GetImages("https://th.bing.com/th/id/OIP.MaDrjtmPQGzKiLHrHEPfFAHaHa?rs=1&pid=ImgDetMain")   