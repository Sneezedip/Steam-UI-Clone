from turtle import bgcolor
import customtkinter
class Loading():
    def __init__(self):
        self.root = customtkinter.CTk()

        self.root.geometry("500x300")
        self.root.title('Steam')
        self.root.overrideredirect(True)
        self.background = customtkinter.CTkFrame(self.root,500,300,fg_color="#171d25",bg_color="#171d25")
        self.loadingbar = customtkinter.CTkProgressBar(self.root,width=150,height=15,corner_radius=5,determinate_speed=0.5,mode='determinate',progress_color="white",bg_color="#171d25")
        self.background.place(x=0,y=0)
        self.loadingbar.place(x=170,y=150)  
        self.loadingbar.set(0)
        self.loadingbar.start()
        from Main import Main
        self.main = Main()
        self.root.after(7000,self.main)
        self.root.mainloop()

    def ClearScreen(self):
        pass

