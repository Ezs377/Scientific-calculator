# Calculator program

# Import modules
import tkinter
import math
import sys
from tkinter import messagebox

# Class to hold custom functions
class Function_class:

    # Function to create buttons
    def create_button(source, label, pad_x,
                      pad_y, color, font_color,
                      fnt, border_depth,
                      function, active_bg):

        return tkinter.Button(
            source, text=label, padx=pad_x, pady=pad_y,
            bg=color, fg=font_color, font=fnt,
            bd=border_depth, relief=tkinter.RAISED,
            activebackground=active_bg,
            command=function)

    # Function to create exit button in new windows
    def exit_button(source, row_no, name, window):

        exit = Function_class.create_button(
            source, "Back", 5, 10,
            "#ff0000", "#f0f0f0", (("Arial bold"), 10),
            1, lambda: window.destroy(),
            "#b30000")

        exit.grid(row=row_no,
                  sticky=tkinter.NSEW,
                  column=0)

        exit.bind("<Destroy>",
                         lambda event: button_dict[
                             name].config(
                                 state=tkinter.NORMAL))
        return exit

    # Function to allocate buttons for a calculator menu
    def create_row(button_list, name_list, row_no,
                   frame, columnstart, function):

        # Variables
        to_be_added = []
        button_bg = "#f2f2f2"
        button_fg = "#000000"

        # Import characters from character list
        for x in name_list:
            to_be_added.append(Characters.character_dict[x])

        # Create buttons, each with specific functions
        column_no = columnstart
        for index, name in enumerate(to_be_added):

            button_list.append(Function_class.create_button
                             (frame, name, 0, 0,
                              button_bg, button_fg,
                              ("Arial 13 bold"), 1,
                              function, "#cccccc"))
            button_list[index].grid(row=row_no,
                                  column=column_no,
                                  sticky=tkinter.NSEW)
            column_no += 1
            button_list[index].config(height=3,
                                      width=4)

    def command_change(row, column_no,
                       function):
        row[column_no].config(command=function)

# Import Unicode
class Characters:
    character_dict = {
        'euler': "\u2107", 'pi': "\u03c0",
        'squared': "\u00b2", 'lbracket': '(', 'rbracket': ')', 'log': 'log ',
        'sin': 'sin ', 'cos': 'cos ', 'tan': 'tan ', 'ln': 'ln ',
        'factorial': '!', 'inverse': '\u207b' + '\u00b9',
        'inversesin': 'sin' + '\u207b' + '\u00b9 ',
        'inversetan': 'tan' + '\u207b' + '\u00b9 ',
        'inversecos': 'cos' + '\u207b' + '\u00b9 ',
        'percent': '\u0025', 'clear': "AC", 'delete': 'DEL',
        "plusminus": "+/-", 'add': '+', 'minus': '-',
        'divide': '\u00f7', 'times': 'x', 'equals': '=', 'power': '^',
        'squareroot': '\u221a', 'root': '\u02e3' + '\u221a',
        0: '0', 'dot': '.', 1: '1', 2: '2', 3: '3',
        4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
        'fdconvert': 'F-D', 'shift': 'Shift', 'alpha': 'Alpha',
        'xsquared': 'X' + "\u00b2", 'fpconvert': 'F-' + '\u0025',
        'dpconvert': 'D-' + '\u0025'}

    shift_characters = {
        character_dict['sin']: character_dict['inversesin'],
        character_dict['cos']: character_dict['inversecos'],
        character_dict['tan']: character_dict['inversetan'],
        character_dict['xsquared']: character_dict['squareroot'],
        character_dict['power']: character_dict['root'],
        character_dict['pi']: character_dict['euler'],
        character_dict['fdconvert']: character_dict['fpconvert']}
    
    alpha_characters = {
        character_dict['fdconvert']: character_dict['dpconvert']}

    operation_characters = {'add': '+', 'minus': '-',
        'divide': '\u00f7', 'times': 'x', 'equals': '=', 'power': '^',
        'squareroot': '\u221a', 'root': '\u02e3' + '\u221a'}

    integer_characters = {1: '1', 2: '2', 3: '3',
        4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 0: '0'}


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
        self.heading = tkinter.Label(
            self.frame, padx=20, pady=10,
            text="Main Menu",
            font=(("Yu Gothic Medium bold"), 35),
            bg=heading_bg)

        self.heading.grid(row=0, columnspan=2,
                          padx=5,
                          pady=5,
                          sticky=tkinter.NSEW)

        # Menu Buttons
        for index, name in enumerate(buttons):
            button_dict[name] = (
                Function_class.create_button(
                    self.frame,
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
        button_dict["Operations"].config(
            state=tkinter.DISABLED)

        # Import custom characters
        self.characters = Characters()

        # Color and aesthetics
        button_bg = "#f2f2f2"
        button_fg = "#000000"
        self.toggle = 1
        self.a_toggle = 1

        # Create window and frame
        self.operation_window = tkinter.Toplevel()
        self.operation_window.title("Calculator")

        # Disable resizing
        self.operation_window.resizable(0, 0)

        self.operation_frame = tkinter.Frame(
            self.operation_window)
        self.operation_frame.grid()

        # Grid weights
        for a in range(1, 5):
            self.operation_frame.rowconfigure(a, weight=1)
        for b in range(0, 7):
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
        self.textbox.config(state=tkinter.DISABLED)
        self.textbox.focus()

        # Calculator buttons
        self.row1 = []
        self.row2 = []
        self.row3 = []
        self.row4 = []
        self.row5 = []
        self.allrows = []
        self.added_list = []

        # Row 1
        self.namelist = ['clear', 'delete', 'factorial', 'add',
                    'fdconvert', 'shift', 'alpha']
        Function_class.create_row(self.row1, self.namelist, 1,
                                  self.operation_frame,
                                  0, lambda: None)

        for index, button in enumerate(self.row1):
            button.config(
                command=lambda index=index: self.printout(
                    self.row1[index]))

        # Change AC button command
        Function_class.command_change(self.row1, 0,
                                      lambda: self.clear_all())

        # Change DEL button command
        Function_class.command_change(self.row1, 1,
                                      lambda: self.delete())

        # Change SHIFT button command
        Function_class.command_change(self.row1, 5,
                                      lambda: self.shift_convert())

        # Change ALPHA button command
        Function_class.command_change(self.row1, 6,
                                      lambda: self.alpha_convert())

        # Row 2
        self.namelist = [7, 8, 9, 'minus', 'sin', 'cos',
                             'tan']
        Function_class.create_row(self.row2, self.namelist, 2,
                                  self.operation_frame,
                                  0, lambda: None)

        for index, button in enumerate(self.row2):
            button.config(
                command=lambda index=index: self.printout(
                    self.row2[index]))
        # Row 3
        self.namelist = [4, 5, 6, 'times', 'log', 'ln', 'pi']
        Function_class.create_row(self.row3, self.namelist, 3,
                                  self.operation_frame,
                                  0, lambda: None)

        for index, button in enumerate(self.row3):
            button.config(
                command=lambda index=index: self.printout(
                    self.row3[index]))
        # Row 4
        self.namelist = [1, 2, 3, 'divide', 'xsquared', 'power']
        Function_class.create_row(self.row4, self.namelist, 4,
                                  self.operation_frame,
                                  0, lambda: None)

        for index, button in enumerate(self.row4):
            button.config(
                command=lambda index=index: self.printout(
                    self.row4[index]))

        self.row4[4].config(
            command=lambda: self.printout_true(
                self.characters.character_dict['squared']))

        # Row 5
        self.namelist = [0, 'dot', 'lbracket', 'rbracket']
        Function_class.create_row(self.row5, self.namelist, 5,
                                  self.operation_frame, 2, lambda: None)

        for index, button in enumerate(self.row5):
            button.config(
                command=lambda index=index: self.printout(
                    self.row5[index]))

        # Equals button
        self.equal_button = (Function_class.create_button
                             (self.operation_frame, '=', 0, 0,
                              button_bg, button_fg,
                              ("Arial"), 1,
                              lambda: None, "#cccccc"))

        self.equal_button.grid(row=4, rowspan=2, column=6,
                                sticky=tkinter.NSEW)

        self.equal_button.config(
            command=lambda: self.equals())
        
        
        for buttons in self.row1:
            self.allrows.append(buttons)
        for buttons in self.row2:
            self.allrows.append(buttons)
        for buttons in self.row3:
            self.allrows.append(buttons)
        for buttons in self.row4:
            self.allrows.append(buttons)
        for buttons in self.row5:
            self.allrows.append(buttons)

        # Scrollbar
        scrollbar = tkinter.Scrollbar(self.operation_frame)
        self.textbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.textbox.yview)

        # Exit button
        self.exit_button = Function_class.exit_button(
            self.operation_frame, 5,
            "Operations", self.operation_window)
        self.exit_button.grid(columnspan=2)

        self.bindings()

    # Calculating function
    def equals(self):
        
        # Split numbers and operators
        self.temp_number = []
        self.temp_operator = []
            
        # Search for numbers
        for char in self.added_list:
            try:
                char = int(char)
            except:
                self.temp_operator.append(char)
            
            if char in self.characters.integer_characters:
                self.temp_number.append(char)
        print (self.temp_number)
        print (self.temp_operator)
        
                
        '''WORK ON CALCULATIONS'''
        
        # Brackets
        if '(' in self.added_list:
            for element in self.added_list:
                if element == '(':
                    index1 = (self.added_list.index(element))
                

    # Key bindings
    def bindings(self):
        # Backspace
        self.operation_window.bind(
            '<BackSpace>', lambda command: self.delete())

        # Number keys
        for x in (range(0, 9)):
            self.operation_window.bind(
                str(x), lambda command,
                x=x: self.keys(
                    self.characters.character_dict[x]))
        
        # Enter
        self.operation_window.bind(
            '<Return>',
            lambda command: self.equals())

        # Operations
        o_dict = {'+': 'add', '-': 'minus',
                  '*': 'times', '/': 'divide',
                  '(': 'lbracket', ')': 'rbracket'}
        for x in o_dict:
            self.operation_window.bind(
                str(x), lambda command,
                x=x: self.keys(
                    self.characters.character_dict[
                        o_dict[x]]))

    # To prinout from button to text
    def printout(self, button):
        self.textbox.config(state=tkinter.NORMAL)
        self.added_list.append(button['text'])
        try:
            self.textbox.insert('insert', self.added_list[-1])
        except:
            print ('error')
        self.textbox.config(state=tkinter.DISABLED)

    # For buttons with specific values
    def printout_true(self, text):
        # Turn on textbox
        self.textbox.config(state=tkinter.NORMAL)
        self.added_list.append(text)
        try:
            self.textbox.insert('insert', self.added_list[-1])

        except:
            print('error')
        # Turn off textbox
        self.textbox.config(state=tkinter.DISABLED)

    # Clear screen
    def clear_all(self):
        self.textbox.config(state=tkinter.NORMAL)
        self.textbox.delete('1.0', 'end')
        self.added_list = []
        self.textbox.config(state=tkinter.DISABLED)

    # Backspace
    def delete(self):
        # Turn on textbox
        self.textbox.config(state=tkinter.NORMAL)
        try:
            self.added_list.pop()
        except:
            pass

        # Delete character
        self.textbox.delete('end-2c')
        # Turn off textbox
        self.textbox.config(state=tkinter.DISABLED)
        
    # For binding keys function
    def keys(self, character):
        self.printout_true(character)

    # For error messages
    def error(self, error_type):
        if error_type == 'math':
            tkinter.messagebox.showwarning('Error', 'Math error')
        elif error_type == 'stack':
            tkinter.messagebox.showwarning('Error', 'Stack error')
        else:
            tkinter.messagebox.showwarning('Error', 'Unknown error')
    
    # For the shift button
    def shift_convert(self):
        
        # If unshifted
        if self.toggle == 1 and self.a_toggle == 1:
            
            # Change color of SHIFT
            self.row1[5].config(bg='#a6a6a6')
            
            for a in self.allrows:
                # If the label of a button matches 
                # a character in shift dictionary
                if a['text'] in Characters.shift_characters:
                    self.convert = Characters.shift_characters[a['text']]
                    a.config(text=self.convert,
                             command=lambda x=a:self.printout(x))
                else:
                    pass
            # Toggle
            self.toggle = 0
            
        # If shifted
        elif self.toggle == 0 and self.a_toggle == 1:
            # Change color of SHIFT
            self.row1[5].config(bg='#f2f2f2')
            
            # Inverterd shift dictionary
            self.converted = {value: key for (
                key, value) in Characters.shift_characters.items()}
            
            for a in self.allrows:
                # If the label of a button matches 
                # a character in shift dictionary
                if a['text'] in self.converted:
                    self.convert = self.converted[a['text']]
                    a.config(text=self.convert,
                             command=lambda x=a:self.printout(x))
                else:
                    pass            
            # Toggle
            self.toggle = 1

        else:
            pass
        
    # For the alpha button    
    def alpha_convert(self):
        
        # If not ALPHA
        if self.a_toggle == 1 and self.toggle == 1:
            # Change the color of ALPHA
            self.row1[6].config(bg='#a6a6a6')
            self.row1[4].config(
                text=Characters.alpha_characters[
                    Characters.character_dict['fdconvert']],
                     command=lambda:self.printout(
                         self.row1[4]))
            self.a_toggle = 0
        
        elif self.a_toggle == 0 and self.toggle == 1:
            # Change the color of ALPHA
            self.row1[6].config(bg='#f2f2f2')
            
            # Invert dictionary
            self.a_converted = {value: key for (
                key, value) in Characters.alpha_characters.items()}
            
            self.row1[4].config(
                text=self.a_converted[
                    Characters.character_dict[
                    'dpconvert']],
                command=lambda:self.printout(
                         self.row1[4]))
            self.a_toggle = 1
        else:
            pass

# User guide
class Help:
    def __init__(self):
        self.file = open('Help.txt', 'r')
        self.help_file = (self.file.read())

        self.file2 = open('Left help.txt', 'r')
        self.l_help = (self.file2.read())

        self.file3 = open('Right help.txt', 'r')
        self.r_help = (self.file3.read())

        # This disables the corresponding button in the main menu
        button_dict["Help"].config(state=tkinter.DISABLED)

        # Create window and frame
        self.Help_window = tkinter.Toplevel()
        self.Help_window.title('Help')

        self.Help_frame = tkinter.Frame(self.Help_window,
                                        bg="#ffffff")
        self.Help_frame.grid()

        self.text1 = tkinter.Label(
            self.Help_frame,
            text=self.help_file,
            anchor=tkinter.CENTER,
            bg="#ffffff",
            fg="#000000",
            font=('Arial, 12'),
            bd=10,
            relief=tkinter.GROOVE,
            padx=10,
            pady=10)
        self.text1.grid(row=0, columnspan=3)

        self.text_left = tkinter.Label(
            self.Help_frame,
            text=self.l_help,
            anchor=tkinter.CENTER,
            bg="#ffffff",
            fg="#000000",
            font=('Arial, 12'),
            bd=10,
            padx=10,
            pady=10)

        self.text_left.grid(
            row=1, column=0,
            sticky=tkinter.NSEW)

        self.text_right = tkinter.Label(
            self.Help_frame,
            text=self.r_help,
            anchor=tkinter.CENTER,
            bg="#ffffff",
            fg="#000000",
            font=('Arial, 12'),
            bd=10,
            padx=10,
            pady=10)

        self.text_right.grid(
            row=1, column=1,
            sticky=tkinter.NSEW)

        # Exit button
        self.exit_button = Function_class.exit_button(self.Help_frame, 2,
                                                      "Help", self.Help_window)
        self.exit_button.grid(sticky=tkinter.SW)


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
    root.resizable(0, 0)
    main_class = Main(root)
    root.mainloop()
