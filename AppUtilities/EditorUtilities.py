from AppUtilities.Utilities import  Utilities
from AppUtilities.StaticValues import Static
from AppGraphics.OnlineAlocated import Images
class Editor():
    def SaveChanges(changeusername,changelocation,changedescription):
        changes = []
        with open("AppConfig/app.cfg","r") as fileread:
            for line in fileread.readlines():
                if str(line.strip()) == "username="+Utilities.Info("username"):
                    changes.append("username="+changeusername+"\n")
                elif str(line.strip()) == "country="+Utilities.Info("country"):
                    changes.append("country="+changelocation.lower()+"\n")
                elif str(line.strip()) == "description="+Utilities.Info("description"):
                    changes.append("description="+changedescription.lower()+"\n")
                else:
                    changes.append(str(line.strip()+"\n"))
        with open("AppConfig/app.cfg","w")  as file:
            for change in changes:
                file.write(str(change))

        Static.userprofile.configure(text=Utilities.Info("username").upper())
        Static.username.configure(text=Utilities.Info("username"))
        Static.LABEL = Images.GetLabel()
        Static.USEDFLAG = Images.GetFlag()