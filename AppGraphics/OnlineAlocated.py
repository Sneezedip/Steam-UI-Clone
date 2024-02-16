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
    match (Utilities.Info("country").lower()):
        case "unitedstates": USEDFLAG = Utilities.GetImages("https://img.icons8.com/office/16/usa.png");LABEL = "United States"
        case "portugal": USEDFLAG = Utilities.GetImages("https://img.icons8.com/office/16/portugal.png");LABEL= "Portugal"
        case "brazil": USEDFLAG = Utilities.GetImages("https://img.icons8.com/office/16/brazil.png");LABEL= "Brazil"
        case "canada": USEDFLAG = Utilities.GetImages("https://img.icons8.com/office/16/canada.png");LABEL= "Canada"
        case "norway": USEDFLAG = Utilities.GetImages("https://img.icons8.com/office/16/norway.png");LABEL = "Norway"
        case "sweden": USEDFLAG = Utilities.GetImages("https://img.icons8.com/office/16/sweden.png");LABEL= "Sweden"
        case "finland": USEDFLAG = Utilities.GetImages("https://img.icons8.com/office/16/finland.png");LABEL= "Finland"
        case "germany": USEDFLAG = Utilities.GetImages("https://img.icons8.com/office/16/germany.png");LABEL= "Germany"
        case "france": USEDFLAG = Utilities.GetImages("https://img.icons8.com/office/16/france.png");LABEL = "France"
        case "croatia": USEDFLAG = Utilities.GetImages("https://img.icons8.com/office/16/croatia.png");LABEL= "Croatia"
        case "albania": USEDFLAG = Utilities.GetImages("https://img.icons8.com/office/16/albania.png");LABEL= "Albania"
        case "malta": USEDFLAG = Utilities.GetImages("https://img.icons8.com/office/16/malta.png");LABEL= "Malta"
        case "china": USEDFLAG = Utilities.GetImages("https://img.icons8.com/office/16/china.png");LABEL = "China"
        case "japan": USEDFLAG = Utilities.GetImages("https://img.icons8.com/office/16/japan.png");LABEL= "Japan"
        case "ukraine": USEDFLAG = Utilities.GetImages("https://img.icons8.com/office/16/ukraine.png");LABEL= "Ukraine"
        case "belgium": USEDFLAG = Utilities.GetImages("https://img.icons8.com/office/16/belgium.png");LABEL = "Belgium"
        case "jamaica": USEDFLAG = Utilities.GetImages("https://img.icons8.com/office/16/jamaica.png");LABEL= "Jamaica"
    