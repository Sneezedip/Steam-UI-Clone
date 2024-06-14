from tkinter import messagebox
import webbrowser
class Errors():
    @staticmethod
    def Get(error, can_continue=False):
        with open("AppConfig/errors.cfg", "r") as file:
            for line in file:
                if int(line.split(":")[0]) == error:
                    if messagebox.askyesno("Error", str(line.split(":")[1]), icon=messagebox.ERROR):
                        webbrowser.open("https://github.com/Sneezedip/Steam-UI-Clone/issues")
                    break 
        if not can_continue:
            exit()