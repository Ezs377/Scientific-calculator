# Calculator program

# Import modules
import tkinter
import math
import sys

# Class to hold custom functions


class Function_class:

    # Function to create buttons
    def create_button(source, label, hgt, wdt, pad_x, pad_y, color,
                      font_color, fnt, border_depth, function, active_bg):

        return tkinter.Button(source, text=label, height=hgt, width=wdt,
                              padx=pad_x, pady=pad_y, bg=color, fg=font_color,
                              font=fnt, bd=border_depth, relief=tkinter.RAISED,
                              activebackground=active_bg,
                              command=function)

    # Function to create exit button in new windows
    def exit_button(source, row_no, name, window):

        exit = Function_class.create_button(source, "Back", 0, 0, 5, 10,
                      "#ff0000", "#f0f0f0", (("Arial bold"), 10),
                      1, lambda: window.destroy(),
                      "#b30000")

        exit.grid(row=row_no, column=0,
                         sticky=tkinter.S + tkinter.W)

        exit.bind("<Destroy>",
                         lambda event: button_dict[name].config(state=tkinter.NORMAL))

    # Function to allocate buttons for a calculator menu
    def calc_buttons():
        button_list = []
        
        operation_dict = {'add':'+', 'minus':'-', 'divide':'\u00f7',
                          'times':'x', 'equals':'=', 'power':'^',
                          'squareroot':'\u221a', 'root':'\u02e3'+'\u221a'}
        
        symbols_dict = {'euler':"\u2107", 'pi':"\u03c0", 'squared':"\u00b2",
                        'lbracket':'(', 'rbracket':')', 'log':'log ',
                        'sin':'sin ', 'cos':'cos ', 'tan':'tan ', 'ln':'ln ',
                        'factorial':'!','inverse':'\u207b'+'\u00b9',
                        'inversesin':'sin'+'\u207b'+'\u00b9 ',
                        'inversetan':'tan'+'\u207b'+'\u00b9 ',
                        'inversecos':'cos'+'\u207b'+'\u00b9 ',
                        'percent':'\u0025'}

        print (button_list)
        print (operation_dict)
        print (symbols_dict)

# Main class
class Main:

    # init
    def __init__(self, source):

        # Colors and aesthetics
        background = "#3399ff"
        heading_bg = "#f2f2f2"
        button_bg = "#ffe0cc"
        font = (("Yu Gothic Medium"), 15)
        button_no = ""
        global button_dict
        button_dict = {}

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
            button_dict[name] = (Function_class.create_button(self.frame,
                                                              name, 2, 13,
                                                              0, 0,
                                                              button_bg,
                                                              "#000000",
                                                              font, 1,
                                                              functions[index],
                                                              "#ff8533"))
            button_dict[name].grid(row=rowno, column=columnno,
                                       sticky=tkinter.NSEW,
                                       pady=5,
                                       padx=5)
            columnno += 1
            if columnno == 2:
                columnno = 0
                rowno += 1

# For calculator calculations
class Operations:
    def __init__(self):
        # This disables the corresponding button in the main menu
        button_dict["Operations"].config(state=tkinter.DISABLED)

        Function_class.calc_buttons()

        # Create window and frame
        self.operation_window = tkinter.Toplevel()
        self.operation_window.title("Calculator")

        self.operation_frame = tkinter.Frame(self.operation_window)
        self.operation_frame.grid()

        # Input and output text
        self.textbox = tkinter.Text(self.operation_frame,
                                    height=5,
                                    width=30,
                                    selectborderwidth=0,
                                    spacing1=5,
                                    wrap=tkinter.WORD,
                                    font=(("Arial"), 20))
        self.textbox.grid(row=0, columnspan=2)

        # Calculator buttons

        # Exit button
        Function_class.exit_button(self.operation_frame, 1,
                                   "Operations", self.operation_window)


# User guide
class Help:
    def __init__(self):

        # This disables the corresponding button in the main menu
        button_dict["Help"].config(state=tkinter.DISABLED)

        # Create window and frame
        self.Help_window = tkinter.Toplevel()
        self.Help_window.title('Help')

        self.Help_frame = tkinter.Frame(self.Help_window)
        self.Help_frame.grid()

        self.text1 = tkinter.Label(self.Help_frame,
                                   text="Help")
        self.text1.grid(row=0, column=0)

        # Exit button
        Function_class.exit_button(self.Help_frame, 1,
                                   "Help", self.Help_window)


# For using statistics and data
class Statistics:
    def __init__(self):
        # This disables the corresponding button in the main menu
        button_dict["Statistics"].config(state=tkinter.DISABLED)

        # Create window and frame
        self.statistic_window = tkinter.Toplevel()
        self.statistic_window.title("Statistics")

        self.statistic_frame = tkinter.Frame(self.statistic_window)
        self.statistic_frame.grid()

        self.text1 = tkinter.Label(self.statistic_frame,
                                   text="Statistics")
        self.text1.grid(row=0, column=0)

        # Exit button
        Function_class.exit_button(self.statistic_frame, 1,
                                   "Statistics", self.statistic_window)

# Viewing past calculations
class Recall:
    def __init__(self):
        # This disables the corresponding button in the main menu
        button_dict["Recall"].config(state=tkinter.DISABLED)

        # Create window and frame
        self.recall_window = tkinter.Toplevel()
        self.recall_window.title("History")

        self.recall_frame = tkinter.Frame(self.recall_window)
        self.recall_frame.grid()

        self.text1 = tkinter.Label(self.recall_frame,
                                   text="Recall")
        self.text1.grid(row=0, column=0)

        # Exit button
        Function_class.exit_button(self.recall_frame, 1,
                                   "Recall", self.recall_window)


# For grpahing
class Graph:
    def __init__(self):
        # This disables the corresponding button in the main menu
        button_dict["Graph"].config(state=tkinter.DISABLED)

        # Create window and frame
        self.graph_window = tkinter.Toplevel()
        self.graph_window.title("Graph")

        self.graph_frame = tkinter.Frame(self.graph_window)
        self.graph_frame.grid()

        self.text1 = tkinter.Label(self.graph_frame,
                                   text="graph")
        self.text1.grid(row=0, column=0)

        # Exit button
        Function_class.exit_button(self.graph_frame, 1,
                                   "Graph", self.graph_window)


# Exit program
class Exit:
    # Exit program
    def __init__(self):
        sys.exit()

# Main routine
if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Main menu")
    main_class = Main(root)
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    root.mainloop()
