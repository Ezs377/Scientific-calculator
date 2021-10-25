# Calculator program

# Import modules
import tkinter
import math
import sys

# Class to hold custom functions


class Function_class:

    # Function to create buttons
    def create_button(source,
                      label,
                      hgt,
                      wdt,
                      pad_x,
                      pad_y,
                      color,
                      font_color,
                      fnt,
                      border_depth,
                      function,
                      active_bg):
        return tkinter.Button(source,
                              text=label,
                              height=hgt,
                              width=wdt,
                              padx=pad_x,
                              pady=pad_y,
                              bg=color,
                              fg=font_color,
                              font=fnt,
                              bd=border_depth,
                              relief=tkinter.RAISED,
                              activebackground=active_bg,
                              command=function)

    # To create a toplevel window
    def Toplevel_frame(self):
        self.window = tkinter.Toplevel()  # Create new window

        # Create frame
        self.toplevel_frame = (self.window)
        self.toplevel_frame.grid()


# Main class
class Main:

    # init
    def __init__(self, source):

        # Colors and aesthetics
        background = "#3399ff"
        heading_bg = "#f2f2f2"
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
        self.frame = tkinter.Frame(self.master, padx=10, pady=10,
                                   bg=background)

        # Create grid
        self.frame.grid()

        # Heading title
        self.heading = tkinter.Label(self.frame, padx=20, pady=10,
                                     text="Main Menu",
                                     font=(("Yu Gothic Medium bold"), 35),
                                     bg=heading_bg)
        self.heading.grid(row=0, columnspan=2,
                          padx=5,
                          pady=5,
                          sticky=tkinter.NSEW)

        # Menu Buttons
        for index, name in enumerate(buttons):
            self.generated_button = Function_class.create_button(self.frame,
                                                                 name, 2, 13,
                                                                 0,0,
                                                                 button_bg,
                                                                 "#000000",
                                                                 font, 1,
                                                                 functions[index],
                                                                 "#ff8533")
            self.generated_button.grid(row=rowno, column=columnno,
                                       sticky=tkinter.NSEW,
                                       pady=5,
                                       padx=5)
            columnno += 1
            if columnno == 2:
                columnno = 0
                rowno += 1

class Operations:
    def __init__(self):
        state = "on"
        Main.
        Function_class.Toplevel_frame(self)
        self.window.title('Calculator')

        # Input and output text
        self.textbox = tkinter.Text(self.toplevel_frame,
                                    height=5,
                                    width=30,
                                    selectborderwidth=0,
                                    spacing1=5,
                                    wrap=tkinter.WORD,
                                    font=(("Arial"), 20))
        self.textbox.grid(row=0, columnspan=2)
        
        # Calculator buttons
        
        # Exit button
        self.exit_button = Function_class.create_button(self.toplevel_frame,
                                                        "Back",
                                                        0,
                                                        0,
                                                        5,
                                                        10,
                                                        "#ff0000",
                                                        "#f0f0f0",
                                                        (("Arial bold"), 10),
                                                        1,
                                                        lambda:self.window.destroy(),
                                                        "#b30000")
        self.exit_button.grid(row=1, column=0,
                              sticky=tkinter.S+tkinter.W)
        self.exit_button.bind("<Destroy>", lambda event: print ("Closed"))

class Help:
    def __init__(self):
        # Create new window
        Function_class.Toplevel_frame(self)

        self.text1 = tkinter.Label(self.toplevel_frame,
                                   text="Help")
        self.text1.grid(row=0, column=0)


class Statistics:
    def __init__(self):
        Function_class.Toplevel_frame(self)

        self.text1 = tkinter.Label(self.toplevel_frame,
                                   text="Statistics")
        self.text1.grid(row=0, column=0)


class Recall:
    def __init__(self):
        Function_class.Toplevel_frame(self)

        self.text1 = tkinter.Label(self.toplevel_frame,
                                   text="Recall")
        self.text1.grid(row=0, column=0)


class Graph:
    def __init__(self):
        Function_class.Toplevel_frame(self)

        self.text1 = tkinter.Label(self.toplevel_frame,
                                   text="Graph")
        self.text1.grid(row=0, column=0)


class Exit:
    # Exit program
    def __init__(self):
        self.test()

    def test(self):
        sys.exit()


# Main routine
if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Main menu")
    run = Main(root)
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    root.mainloop()
