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
        'fdconvert': 'D-F', 'shift': 'Shift', 'alpha': 'Alpha',
        'xsquared': 'X' + "\u00b2", 'fpconvert': 'F-' + '\u0025',
        'dpconvert': 'D-' + '\u0025', 'answer': 'Ans'}

    shift_characters = {
        character_dict['sin']: character_dict['inversesin'],
        character_dict['cos']: character_dict['inversecos'],
        character_dict['tan']: character_dict['inversetan'],
        character_dict['xsquared']: character_dict['squareroot'],
        character_dict['power']: character_dict['root'],
        character_dict['pi']: character_dict['euler'],
        character_dict['fdconvert']: character_dict['dpconvert']}
    
    alpha_characters = {
        character_dict['fdconvert']: character_dict['fpconvert'],
        character_dict['pi']: character_dict['answer']}

    operation_characters = [
        character_dict['add'], character_dict['minus'],
        character_dict['divide'], character_dict['times'],
        character_dict['factorial'], character_dict['squared'],
        character_dict['power'], character_dict['sin'],
        character_dict['cos'], character_dict['tan'],
        character_dict['log'], character_dict['ln'],
        character_dict['power'], character_dict['squareroot'],
        character_dict['root'], character_dict['squared'],
        character_dict['inversesin'], character_dict['inversecos'],
        character_dict['inversetan']]
    
    brackets = [
        character_dict['lbracket'],
        character_dict['rbracket']]

    
    BEDMAS = {character_dict['times']:0,
              character_dict['divide']:1,
              character_dict['add']:2,
              character_dict['minus']:3}
    
    reverse_BEDMAS = {0:character_dict['times'],
                      1:character_dict['divide'],
                      2:character_dict['add'],
                      3:character_dict['minus']}

    integer_characters = {1: '1', 2: '2', 3: '3',
        4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 0: '0',
        '.':'.'}
    
    constants = {character_dict['pi']:math.pi,
                 character_dict['euler']:math.e}


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
        self.F_toggle = 1

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
        
        # Change F-D command
        Function_class.command_change(self.row1, 4,
                                      lambda: self.convert())

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
        '''FOLLOW BEDMAS'''
        '''PARSE SIN, COS, TAN and etc as bracketed expressions'''
        '''How it works:
        1. Search for brackets. If none found, got to next step.
           otherwise, add bracketed characters to a list, and use
           it as input for the next steps. If there are uneven brackets,
           present error.
        
        2. Scan the digits. For every integer that isn't followed by an
           operator, add the digit to a list and repeat until an operator is 
           detected. Remove each digit from the orignal list if possible
           using index() so that duplicates aren't deleted. Then, join the
           digits in a list together, output as float, and replace the digits
           in the input collection list (self.added_list). Repeat for digits
           after the operator as well.
           
        3. Once no more brackets, search for exponents. SinCosTan, Log,
           Ln count as exponents. Bracket the exponent symbol and the integer
           next to it together. Parse this to produce a single output as a
           float. Replace the symbol and integer with this float value. If an
           exponent has no integer in front of it, present error. For root and
           factorial, they scan for integer behind them
           
        4. Once there are no exponents, search for multiplication/division.
           Look for the terms (Characters.character_dict['times']) and
           (Characters.character_dict['divide']). If there are no digits
           before or after the operator, present error. Otherwise, take the digits
           before and after the operator, and process them using the operator. Use
           a 'for' loop to scan from left to right. Once processed, a single float
           output should come out. Replace the previous digits, and operator, with
           this value in the input collection list.
           
        5. Once there are no times/divide, search for addition/subtraction.
           Look for the terms (Character.character_dict['add']) and
           (Character.character_dict['minus']).If there are no digits before or
           after the operator, present error. Otherwise, take the digits before and
           after the operator, and process them using the operator. Use a 'for'
           loop to scan from left to right. Once processed, a single float output
           should come out. Replace the previous digits, and operator, with this
           value in the input collection list.
        
        6. Finally, the result should be one float, which can be presented using
           self.print_result(float). If there wer brackets in the equation,
           this is the result of one bracket. Remove the brackets, and replace
           it with the result, then repeat the whole process for the other brackets
           until only one float remains muhahaha.'''
        
        self.processed = [] # List of processed characters
        self.temp_operator = [] # List of operators in input line
        self.temp_integer = [] # List of digits in input line
        self.compiled_number = [] # List of compiled numbers
        self.error_status = 0 # Error state
        
        self.error_checking(self.added_list)
        
        '''BEDMAS PROCESS'''
        
        '''insert bracket analysis here'''
        '''Brackets'''
        
        
        '''No bracket input, as this scans in-between brackets
        DO NOT TEST WITH BRACKETS YET'''  
        
        # While an error has not been raised
        #while not self.error_status:
        
        # Separate into operators and digits
        for index, term in enumerate(self.added_list):
            try:                
                # Add to number list if it is an integer or dot
                if int(
                    term) in Characters.integer_characters or str(
                        term) in Characters.integer_characters:
                    self.temp_integer.append (str(term))
                    
                    
                # If the last item in a list is integer
                if index == len(self.added_list)-1:
                    self.compiled_number.append(''.join(self.temp_integer))
                    self.temp_integer = []
                
            except:
                # If operation detected, join numbers together
                if term in Characters.operation_characters:
                    # Join previous integers together into
                    # one number and add to list
                    self.compiled_number.append(''.join(self.temp_integer))
                    self.temp_integer = []
                    self.temp_operator.append (term)
                # If a decimal dot
                elif term in Characters.integer_characters['.']:
                    self.temp_integer.append(term)
                    
                # If character is not recognized
                else:
                    self.error("No matched character")
        
        if self.temp_operator:
            self.processed = [None]*(len(self.compiled_number)+len(self.temp_operator))
            self.processed[::2] = self.compiled_number
            self.processed[1::2] = self.temp_operator       
                
            
        # List with inputted characters
        print (self.temp_operator)
        print (self.compiled_number)
        print (self.processed)
        
        if not self.error_status:
            self.print_result()
        else:
            pass
        
    # Ensure brackets are balanced
    def brackets(self):
        pass
        
    # Bracket analysis
    def analyse_bracket(self, List, searched):
        for i in reversed(range(len(List))):
            if List[i] == searched:
                return i                    
    
    # For checking errors in input
    def error_checking(self, List):
        
        # Check each item in list
        for index, a in enumerate(List):
            # Check for operators/dot
            if (a in Characters.operation_characters or
                a == Characters.character_dict['dot']):
                
                # If the character is a dot        
                if a == Characters.character_dict['dot']:
                    
                    if index != len(List)-1:
                        # If double dots present
                        if List[(List.index(a))+1] == Characters.character_dict['dot']:
                            # Raise error and clear screen
                            self.error('syntax')
                            self.clear_all()
                        
                    # If dot is the last character
                    elif index == len(List)-1:
                        # Raise error and clear screen
                        self.error('syntax')
                        self.clear_all()   
                        
                # If the first character is an operator or decimal dot
                if index == 0:
                    if (a in Characters.operation_characters or
                        a == Characters.character_dict['dot']):
                        self.error('syntax')
                        self.clear_all()
                
                # While the character is not the last character
                elif index != len(List)-1:
                    # If a double operations/dot present
                    if (List[(List.index(a))+1] in Characters.operation_characters):
                        # Raise error and clear screen
                        self.error('syntax')
                        self.clear_all()   
            
                
                # If an operator is the last character
                elif index == len(List)-1:
                    # Raise error and clear screen
                    self.error('syntax')
                    self.clear_all()
                    
                         
            
    # The actual calculations                
    def calculations(self):
        
        # Variables
        self.result = 0 #Result of calculations
        self.list_of_operations = []
        
        # If only digits are inputted 
        if not self.temp_operator or not self.added_list:
            self.print_result(self.number_list[0])
        
        # Look for brackets
        elif Characters.character_dict[
            'lbracket'] in self.added_list:
            self.bracket = []
            self.index_of_lbracket = ''
            
            
            # Searches for the innermost left bracket
            self.innermost_bracket = self.analyse_bracket(
                self.added_list, Characters.character_dict[
                    'lbracket'])            
            
            for a in self.added_list[self.innermost_bracket:]:
                self.bracket.append(a)
                if a == Characters.character_dict['rbracket']:
                    self.rbracket_index = a
                    break
            
            # The result of the innermost brackers
            self.process(self.bracket)
            print (self.bracket)
        
        else:
            print ("No brackets")
            
    def process(self, bracket_list):
        pass
                             
    # Maths
    def calculate(self, a, b, method):
        if method == 'add':
            return a+b
        elif method == 'minus':
            return a-b
        elif method == 'times':
            return a*b
        elif method == 'divide':
            return a/b        
            
        

    # Key bindings
    def bindings(self):
        # Backspace
        self.operation_window.bind(
            '<BackSpace>', lambda command: self.delete())

        # Number keys
        for x in (range(0, 10)):
            self.operation_window.bind(
                str(x), lambda command,
                x=x: self.keys(
                    self.characters.character_dict[x]))
        
        # Decimal dot
        self.operation_window.bind(
            '.', lambda command: self.keys(
                Characters.character_dict['dot']))
        
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
        self.textbox.delete('1.0', 'end')
        self.added_list.append(button['text'])
        self.joined_list = ''.join(self.added_list)
        try:
            self.textbox.insert('insert', self.joined_list)
        except:
            self.error('unknown')
        self.textbox.config(state=tkinter.DISABLED)

    # For buttons with specific values
    def printout_true(self, text):
        # Turn on textbox
        self.textbox.config(state=tkinter.NORMAL)
        self.textbox.delete('1.0', 'end')
        self.added_list.append(text)
        self.joined_list = ''.join(self.added_list)
        try:
            self.textbox.insert('insert', self.joined_list)

        except:
            self.error('Unknown')
        # Turn off textbox
        self.textbox.config(state=tkinter.DISABLED)
    
    # For output result
    def print_result(self):
        # Turn on textbox
        # Width = 30 chars
        self.spacer = []
        self.textbox.config(state=tkinter.NORMAL)
        
        # Insert answer after spacing
        try:
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', '=')
            
            '''Change this to self.result when done'''
            self.textbox.insert('end', "Equals") 

        except:
            self.error('Unknown')
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
        self.textbox.delete('1.0', 'end')
        try:
            # Insert endline marker
            self.added_list.append('')
            self.added_list.pop(-2)
        except:
            pass

        # 'Delete' character
        self.joined_list = ''.join(self.added_list)
        try:
            self.textbox.insert('insert', self.joined_list)
            # Remove endline marker
            self.added_list.remove('')

        except:
            print('error')        
        
        # Turn off textbox
        self.textbox.config(state=tkinter.DISABLED)
        
    # For binding keys function
    def keys(self, character):
        self.printout_true(character)

    # For error messages
    def error(self, error_type):
        if error_type == 'math':
            tkinter.messagebox.showwarning('Error', 'Math error')
            self.error_status = 1
        elif error_type == 'stack':
            tkinter.messagebox.showwarning('Error', 'Stack error')
            self.error_status = 1
        elif error_type == 'syntax':
            tkinter.messagebox.showwarning('Error', 'Syntax error')
            self.error_status = 1
        else:
            tkinter.messagebox.showwarning('Error', 'Unknown error')
            self.error_status = 1
    
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
                    self.convert1 = Characters.shift_characters[a['text']]
                    a.config(text=self.convert1,
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
                    self.convert1 = self.converted[a['text']]
                    a.config(text=self.convert1,
                             command=lambda x=a:self.printout(x))
                else:
                    pass            
            # Toggle
            self.toggle = 1

        else:
            pass
        
    # For the alpha button    
    def alpha_convert(self):
        
        # If not ALPHA, change buttons to ALPHA version
        if self.a_toggle == 1 and self.toggle == 1:
            # Change the color of ALPHA
            self.row1[6].config(bg='#a6a6a6')
            
            # Change convert button
            self.row1[4].config(
                text=Characters.alpha_characters[
                    Characters.character_dict['fdconvert']],
                command=lambda:self.printout(
                    self.row1[4]))
            
            # Change constant button to answer
            self.row3[6].config(
                text=Characters.alpha_characters[
                    Characters.character_dict['pi']],
                command=lambda:self.printout(
                    self.row3[6]))
        
            self.a_toggle = 0
        
        # If ALPHA is on, switch back to original buttons
        elif self.a_toggle == 0 and self.toggle == 1:
            # Change the color of ALPHA
            self.row1[6].config(bg='#f2f2f2')
            
            # Invert dictionary
            self.a_converted = {value: key for (
                key, value) in Characters.alpha_characters.items()}
            
            # Change buttons back to original
            self.row1[4].config(
                text=self.a_converted[
                    Characters.character_dict[
                    'fpconvert']],
                command=lambda:self.printout(
                         self.row1[4]))
            
            self.row3[6].config(
                text=self.a_converted[
                    Characters.character_dict['answer']],
                command=lambda:self.printout(
                    self.row3[6]))            
            
            self.a_toggle = 1
        else:
            pass

    # For the F-D button
    def convert(self):
        if self.F_toggle == 1:
            pass
        '''Get answer output, convert it'''
        '''
        if label is D-F, convert from x.y to x/y form
        if label is D-%, convert from x.y to x% form
        if label is F-P, convert from x/y to x% form
        '''
        
        if self.F_toggle == 0:
            pass
        '''Flip function so that it does the opposite as before'''
        '''
        if label is D-F, convert from x/y x.y form
        if label is D-%, convert from x% to x.y form
        if label is F-P, convert from x% to x/y form
        '''
    
        
        
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
