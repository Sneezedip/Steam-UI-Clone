import customtkinter
from AppUtilities.Utilities import Utilities
from AppGraphics.Graphics import Graphics
class Store():
    def StartDrag(self,event):
            global x,y
            x = event.x
            y = event.y
    def MoveWindow(self,event):
        new_x = (self.root.winfo_x() + event.x) - x
        new_y = (self.root.winfo_y() + event.y) - y
        self.root.geometry(f"+{new_x}+{new_y}")
    def LoadTopBar(self):
        background = customtkinter.CTkFrame(self.root,height=1000,width=1000,bg_color="#171d25",fg_color="#171d25")
        title_bar = customtkinter.CTkFrame(self.root,height=50,width=1000,bg_color="#171d25",fg_color="#171d25")
        title_bar.bind("<ButtonPress-1>",self.StartDrag)
        title_bar.bind("<B1-Motion>",self.MoveWindow)

        background.place(x=0,y=0)
        title_bar.place(x=0,y=0)
        Graphics.TopBarTexts(self.root,libraryopen=True)  
    def __init__(self):
        self.hasstyle = False
        self.root = customtkinter.CTk()
        self.root.geometry("1000x600")
        self.root.update_idletasks()
        self.root.withdraw()
        self.root.overrideredirect(True)
        self.root.title('Steam')
        self.root.update_idletasks()
        self.LoadTopBar()
        Graphics.LoadIcons(self.root)
        Utilities.BottomIcon(self.root,self.hasstyle)
        self.root.mainloop()

Store()