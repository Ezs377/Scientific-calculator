# Calculator program

# Import modules
import tkinter
import math
import sys

# Class to hold custom functions


class Function_class:

    # Function to create buttons
    def create_button(source, label, pad_x, pad_y, color,
                      font_color, fnt, border_depth, function, active_bg):

        return tkinter.Button(source, text=label, padx=pad_x, pady=pad_y,
                              bg=color, fg=font_color, font=fnt,
                              bd=border_depth, relief=tkinter.RAISED,
                              activebackground=active_bg,
                              command=function)

    # Function to create exit button in new windows
    def exit_button(source, row_no, name, window):

        exit = Function_class.create_button(source, "Back", 5, 10,
                      "#ff0000", "#f0f0f0", (("Arial bold"), 10),
                      1, lambda: window.destroy(),
                      "#b30000")

        exit.grid(row=row_no,
                  sticky=tkinter.NSEW,
                  columnspan=2)

        exit.bind("<Destroy>",
                         lambda event: button_dict[name].config(state=tkinter.NORMAL))


    # Function to allocate buttons for a calculator menu
    def create_row(button_list, name_list, row_no,
                   frame, columnstart):
        to_be_added = []
        button_bg = "#f2f2f2"
        button_fg = "#000000"
        
        for x in name_list:
            to_be_added.append(Characters.character_dict[x])
            
        
        column_no = columnstart
        for index, name in enumerate(to_be_added):
            
            button_list.append(Function_class.create_button
                             (frame,name, 0, 0,
                              button_bg, button_fg,
                              ("Arial 13 bold"), 1,
                              lambda name=name:(name), "#cccccc"))
            button_list[index].grid(row=row_no,
                                  column=column_no,
                                  sticky=tkinter.NSEW)
            column_no += 1
            button_list[index].config(height=3,
                                      width=4)
    def printout(button):
        pass
            
# Import Unicode
class Characters:
    character_dict = {'euler': "\u2107", 'pi': "\u03c0", 'squared': "\u00b2",
                      'lbracket': '(', 'rbracket': ')', 'log': 'log ',
                      'sin': 'sin ', 'cos': 'cos ', 'tan': 'tan ', 'ln': 'ln ',
                      'factorial': '!', 'inverse': '\u207b' + '\u00b9',
                      'inversesin': 'sin' + '\u207b' + '\u00b9 ',
                      'inversetan': 'tan' + '\u207b' + '\u00b9 ',
                      'inversecos': 'cos' + '\u207b' + '\u00b9 ',
                      'percent': '\u0025','clear': "AC",'delete': 'DEL',
                      "plusminus": "+/-",'add': '+', 'minus': '-',
                      'divide': '\u00f7','times': 'x', 'equals': '=', 'power': '^',
                      'squareroot': '\u221a', 'root': '\u02e3' + '\u221a',
                      'zero': '0', 'dot': '.', 1:'1', 2:'2', 3:'3',
                      4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9',
                      'convert':'F-D', 'shift':'Shift', 'alpha':'Alpha',
                      'xsquared':'X'+"\u00b2"}


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
        buttons = ["Operations", "Recall",
                   "Help", "Exit"]
        functions = [Operations, Recall, Help, Exit]
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
                                                              name, 0, 0,
                                                              button_bg,
                                                              "#000000",
                                                              font, 1,
                                                              functions[index],
                                                              "#ff8533"))

            button_dict[name].grid(row=rowno, column=columnno,
                                       sticky=tkinter.NSEW,
                                       pady=5,
                                       padx=5)
            button_dict[name].config(height=2, width=13)

            columnno += 1
            if columnno == 2:
                columnno = 0
                rowno += 1

# For calculator calculations
class Operations:
    def __init__(self):
        # This disables the corresponding button in the main menu
        button_dict["Operations"].config(state=tkinter.DISABLED)

        # Import custom characters
        characters = Characters()

        # Color and aesthetics
        button_bg = "#f2f2f2"
        button_fg = "#000000"

        # Create window and frame
        self.operation_window = tkinter.Toplevel()
        self.operation_window.title("Calculator")

        self.operation_frame = tkinter.Frame(self.operation_window)
        self.operation_frame.grid()

        # Grid weights
        for a in range (1,5):
            self.operation_frame.rowconfigure(a, weight=1)
        for b in range (0,7):
            self.operation_frame.columnconfigure(b, weight=1)

        # Input and output text
        self.textbox = tkinter.Text(self.operation_frame,
                                    height=5,
                                    width=30,
                                    selectborderwidth=0,
                                    spacing1=5,
                                    wrap=tkinter.WORD,
                                    font=(("Arial"), 20))
        self.textbox.grid(row=0, columnspan=7)

        # Calculator buttons
        self.row1 = []
        self.row2 = []
        self.row3 = []
        self.row4 = []
        self.row5 = []
        
        # Row 1
        self.namelist = ['clear', 'delete', 'plusminus', 'add',
                    'convert', 'shift', 'alpha']
        Function_class.create_row(self.row1, self.namelist, 1,
                                  self.operation_frame,0)
        
        # Row 2
        self.namelist = [7, 8, 9, 'minus','sin','cos',
                             'tan']
        Function_class.create_row(self.row2, self.namelist, 2,
                                  self.operation_frame,0)
        
        # Row 3
        self.namelist = [4,5,6,'times','log', 'ln','pi']
        Function_class.create_row(self.row3, self.namelist, 3,
                                  self.operation_frame,0)  
        
        # Row 4
        self.namelist = [1,2,3,'divide', 'xsquared','power'] 
        Function_class.create_row(self.row4, self.namelist, 4,
                                  self.operation_frame,0)   
        
        # Row 5
        self.namelist = ['zero','dot','lbracket','rbracket']
        Function_class.create_row(self.row5, self.namelist, 5,
                                  self.operation_frame,2) 
        
        # Equals button
        self.equal_button = (Function_class.create_button
                             (self.operation_frame,'=', 0, 0,
                              button_bg, button_fg,
                              ("Arial"), 1,
                              lambda: print ("hello"), "#cccccc"))
        self.equal_button.grid (row=4,rowspan=2, column=6,
                                sticky=tkinter.NSEW)
        
        # Scrollbar
        scrollbar = tkinter.Scrollbar(self.operation_frame)
        self.textbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.textbox.yview)
        
        # Interactivity with textbox
        self.textbox.insert
        
        # Exit button
        Function_class.exit_button(self.operation_frame, 5,
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
    root.mainloop()
