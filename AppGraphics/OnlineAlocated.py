from AppUtilities.Utilities import Utilities
from AppUtilities.StaticValues import Static
class Images():
    def GetFlag():
        uf = None
        match (Utilities.Info("country").lower()):
            case "unitedstates": uf = Utilities.GetImages("https://img.icons8.com/office/16/usa.png")
            case "portugal": uf = Utilities.GetImages("https://img.icons8.com/office/16/portugal.png")
            case "brazil": uf = Utilities.GetImages("https://img.icons8.com/office/16/brazil.png")
            case "canada": uf = Utilities.GetImages("https://img.icons8.com/office/16/canada.png")
            case "norway": uf = Utilities.GetImages("https://img.icons8.com/office/16/norway.png")
            case "sweden": uf = Utilities.GetImages("https://img.icons8.com/office/16/sweden.png")
            case "finland": uf = Utilities.GetImages("https://img.icons8.com/office/16/finland.png")
            case "germany": uf = Utilities.GetImages("https://img.icons8.com/office/16/germany.png")
            case "france": uf = Utilities.GetImages("https://img.icons8.com/office/16/france.png")
            case "croatia": uf = Utilities.GetImages("https://img.icons8.com/office/16/croatia.png");
            case "albania": uf = Utilities.GetImages("https://img.icons8.com/office/16/albania.png");
            case "malta": uf = Utilities.GetImages("https://img.icons8.com/office/16/malta.png");
            case "china": uf = Utilities.GetImages("https://img.icons8.com/office/16/china.png")
            case "japan": uf = Utilities.GetImages("https://img.icons8.com/office/16/japan.png")
            case "ukraine": uf = Utilities.GetImages("https://img.icons8.com/office/16/ukraine.png");
            case "belgium": uf = Utilities.GetImages("https://img.icons8.com/office/16/belgium.png")
            case "jamaica": uf = Utilities.GetImages("https://img.icons8.com/office/16/jamaica.png")
        return uf
    def GetLabel():
        l = None
        match (Utilities.Info("country").lower()):
            case "unitedstates":l = "United States"
            case "portugal":l= "Portugal"
            case "brazil": l= "Brazil"
            case "canada": l= "Canada"
            case "norway": l = "Norway"
            case "sweden": l= "Sweden"
            case "finland": l= "Finland"
            case "germany":l= "Germany"
            case "france": l = "France"
            case "croatia": l= "Croatia"
            case "albania": l= "Albania"
            case "malta": l= "Malta"
            case "china": l = "China"
            case "japan": l= "Japan"
            case "ukraine": l= "Ukraine"
            case "belgium": l = "Belgium"
            case "jamaica": l= "Jamaica"
        return l
    Static.USEDFLAG = GetFlag()
    Static.LABEL = GetLabel()
    steamicon = Utilities.GetImages("https://img.icons8.com/external-those-icons-lineal-color-those-icons/24/external-Steam-social-media-those-icons-lineal-color-those-icons.png")
    closebutton = Utilities.GetImages("https://cdn-icons-png.flaticon.com/512/10728/10728089.png")
    fullscreenbutton = Utilities.GetImages("https://img.icons8.com/external-dreamstale-lineal-dreamstale/32/external-expand-arrows-dreamstale-lineal-dreamstale-6.png")
    minimizebutton = Utilities.GetImages("https://img.icons8.com/ios-filled/50/737373/minus-math.png")
    leftarrow = Utilities.GetImages("https://img.icons8.com/cotton/64/forward.png")
    rightarrow = Utilities.GetImages("https://img.icons8.com/cotton/64/forward.png")
    userphoto = Utilities.GetImages("https://th.bing.com/th/id/OIP.MaDrjtmPQGzKiLHrHEPfFAHaHa?rs=1&pid=ImgDetMain") 

    Static.Countries.append("United States")
    Static.Countries.append("Portugal")
    Static.Countries.append("Brazil")
    Static.Countries.append("Canada")
    Static.Countries.append("Norway")
    Static.Countries.append("Sweden")
    Static.Countries.append("Finland")
    Static.Countries.append("Germany")
    Static.Countries.append("France")
    Static.Countries.append("Croatia")
    Static.Countries.append("Albania")
    Static.Countries.append("Malta")
    Static.Countries.append("China")
    Static.Countries.append("Japan")
    Static.Countries.append("Ukraine")
    Static.Countries.append("Belgium")
    Static.Countries.append("Jamaica")