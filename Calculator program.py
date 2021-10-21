# Calculator program

# Import modules
import tkinter, math

# Main class
class Main:
    def __init__(self, source):
        background = "#99ccff"
        
        # Master root
        self.master = source 
        
        # Main frame
        self.frame = tkinter.Frame(source, padx=5, pady=5,
                                   bg=background)
        # Create grid
        self.frame.grid()
        
        # Heading title
        self.heading = tkinter.Label(self.frame, padx=50, pady=5,
                                     text="Main Menu",
                                     font=(("Yu Gothic Medium"), 50))
        self.heading.grid(row=0, columnspan=2,
                          sticky=tkinter.E+tkinter.W)
    
    

root = tkinter.Tk()
root.title ("Calculator")
run = Main(root)

root.mainloop()