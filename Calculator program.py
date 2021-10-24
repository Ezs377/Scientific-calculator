# Calculator program

# Import modules
import tkinter, math, sys

# Main class
class Main:
    
    # Function to create buttons
    def create_button(self, label, hgt, wdt,
                      color, fnt, border_depth, function):
        return tkinter.Button(self.frame,
                       text = label,
                       height=hgt,
                       width=wdt,
                       bg=color,
                       font=fnt,
                       bd=border_depth,
                       relief=tkinter.FLAT,
                       command = function)
    
    # init 
    def __init__(self, source):
        
        # Colors and aesthetics
        background = "#3399ff"
        heading_bg = "#ffe0cc"
        button_bg = "#ffe0cc"
        font = (("Yu Gothic Medium"), 15)
        
        # Variables
        buttons = ["Operations", "Help", "Statistics",
                   "Recall", "Graph", "Exit"]
        functions = [Operations, Help, Statistics, Recall, Graph, Exit]
        rowno = 1
        columnno = 0
        
        # Master root
        self.master = source 
        
        # Main frame
        self.frame = tkinter.Frame(source, padx=10, pady=10,
                                   bg=background)
        # Create grid
        self.frame.grid()
        
        # Heading title
        self.heading = tkinter.Label(self.frame, padx=20, pady=10,
                                     text="Main Menu",
                                     font=(("Yu Gothic Medium bold"), 35),
                                     bg = heading_bg)
        self.heading.grid(row=0, columnspan=2,
                          padx=5,
                          pady=5,
                          sticky=tkinter.E+tkinter.W)
        
        # Menu Buttons
        for index, name in enumerate(buttons):
            self.generated_button = self.create_button(name, 2, 13,
                                                       button_bg, font,
                                                       0, functions[index])
            self.generated_button.grid(row=rowno, column=columnno,
                                       sticky=tkinter.E+tkinter.W,
                                       pady=5,
                                       padx=5)
            
            columnno += 1
            if columnno == 2:
                columnno = 0
                rowno += 1
            

class Operations:
    def __init__(self):
        self.test()
    def test(self):
        print ("hello")

class Help:
    def __init__(self):
        self.test()
    def test(self):
        print ("hello1")

class Statistics:
    def __init__(self):
        self.test()
    def test(self):
        print ("hello2")
    
class Recall:
    def __init__(self):
        self.test()
    def test(self):
        print ("hello3")
    
class Graph:
    def __init__(self):
        self.test()
    def test(self):
        print ("hello4")
    
class Exit:
    def __init__(self):
        self.test()
    def test(self):
        sys.exit()


root = tkinter.Tk()
root.title ("Calculator")
run = Main(root)

root.mainloop()