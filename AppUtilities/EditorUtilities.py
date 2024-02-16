from AppUtilities.Utilities import  Utilities
from AppUtilities.StaticValues import Static
class Editor():
    def SaveChanges(changeusername):
        changes = []
        with open("AppConfig/app.cfg","r") as fileread:
            for line in fileread.readlines():
                if str(line.strip()) == "username="+Utilities.Info("username"):
                    changes.append("username="+changeusername+"\n")
                else:
                    changes.append(str(line.strip()+"\n"))
        with open("AppConfig/app.cfg","w")  as file:
            for change in changes:
                file.write(str(change))

        Static.userprofile.configure(text=Utilities.Info("username").upper())
        Static.username.configure(text=Utilities.Info("username"))