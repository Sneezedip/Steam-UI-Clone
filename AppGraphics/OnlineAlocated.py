import customtkinter
from PIL import Image
from AppUtilities.Utilities import Utilities
class Images():
    USEDFLAG = ""
    LABEL = ""
    steamicon = Utilities.GetImages("https://img.icons8.com/external-those-icons-lineal-color-those-icons/24/external-Steam-social-media-those-icons-lineal-color-those-icons.png")
    closebutton = Utilities.GetImages("https://cdn-icons-png.flaticon.com/512/10728/10728089.png")
    fullscreenbutton = Utilities.GetImages("https://img.icons8.com/external-dreamstale-lineal-dreamstale/32/external-expand-arrows-dreamstale-lineal-dreamstale-6.png")
    minimizebutton = Utilities.GetImages("https://img.icons8.com/ios-filled/50/737373/minus-math.png")
    leftarrow = Utilities.GetImages("https://img.icons8.com/cotton/64/forward.png")
    rightarrow = Utilities.GetImages("https://img.icons8.com/cotton/64/forward.png")
    userphoto = Utilities.GetImages("https://th.bing.com/th/id/OIP.MaDrjtmPQGzKiLHrHEPfFAHaHa?rs=1&pid=ImgDetMain") 


    #COUNTRIES
    US = Utilities.GetImages("https://img.icons8.com/office/16/usa.png")
    PT = Utilities.GetImages("https://img.icons8.com/office/16/portugal.png") 
    BR = Utilities.GetImages("https://img.icons8.com/office/16/brazil.png") 
    CA = Utilities.GetImages("https://img.icons8.com/office/16/canada.png") 
    match (Utilities.Info("country")):
        case "unitedstates": USEDFLAG = US;LABEL = "United States"
        case "portugal": USEDFLAG = PT;LABEL= "Portugal"
        case "brazil": USEDFLAG = BR;LABEL= "Brazil"
        case "canada": USEDFLAG = CA;LABEL= "Canada"
    