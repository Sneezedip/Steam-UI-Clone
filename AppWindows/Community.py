class Community():
    def StartFrame(self,root,bg):
        bg.configure(fg_color="#171d25")
        self.communityopen = True
    def __init__(self):
        self.communityopen = False
        try:
            self.mainFrame.destroy()
        except:pass
    def GetStatus(self):
        return self.communityopen