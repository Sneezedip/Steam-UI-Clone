class UsedWidgets():
    current = []
    
    def ClearWidgets():
       if len(UsedWidgets.current) >= 1:
            for widgets in UsedWidgets.current:
                widgets.place_forget() 