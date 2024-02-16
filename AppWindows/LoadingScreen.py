import customtkinter
from AppGraphics.Graphics import Graphics
from AppUtilities.Utilities import Utilities
class Loading():
    class LoadRecord():
        Loaded = 0
    def __init__(self):
        self.hasstyle = False
        self.LoadTopBar()
        Utilities.BottomIcon(self.root,self.hasstyle)
        Graphics.TopBarTexts(self.root)
        Graphics.LoadIcons(self.root)
        Utilities.BottomIcon(self.root,self.hasstyle)
        self.loading = customtkinter.CTk()
        self.loading.geometry("500x300")
        self.loading.title('Steam')
        self.loading.overrideredirect(True)
        self.background = customtkinter.CTkFrame(self.loading,500,300,fg_color="#171d25",bg_color="#171d25")
        self.loadingbar = customtkinter.CTkProgressBar(self.loading,width=150,height=15,corner_radius=5,progress_color="white",bg_color="#171d25")
        self.background.place(x=0,y=0)
        self.loadingbar.place(x=170,y=150)  
        self.loadingbar.start()
        self.loading.after(1500,self.CheckValues)
        self.loading.mainloop()
    def CheckValues(self):
        print(Loading.LoadRecord.Loaded)
        if Loading.LoadRecord.Loaded == 5:
            self.loading.destroy()
            from Main import Main
            Main()
        else:
            Loading.LoadRecord.Loaded += 1
            self.loading.after(1500, self.CheckValues)

Loading()