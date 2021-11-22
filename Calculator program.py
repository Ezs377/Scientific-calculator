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

        exit.bind(
            "<Destroy>",
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

            button_list.append(Function_class.create_button(
                frame, name, 0, 0,
                button_bg, button_fg,
                ("Arial 13 bold"), 1,
                function, "#cccccc"))
            button_list[index].grid(
                row=row_no,
                column=column_no,
                sticky=tkinter.NSEW)
            column_no += 1
            button_list[index].config(
                height=3,
                width=4)

    def command_change(row, column_no, function):
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

    basic_operations = [
        character_dict['add'], character_dict['minus'],
        character_dict['divide'], character_dict['times']]        

    complex_before = [
        character_dict['factorial'], character_dict['squared']]

    complex_after = [
        character_dict['sin'], character_dict['cos'],
        character_dict['tan'], character_dict['log'],
        character_dict['ln'], character_dict['inversesin'],
        character_dict['inversecos'], character_dict['inversetan'],
        character_dict['squareroot'], character_dict['root']]    

    brackets = [
        character_dict['lbracket'],
        character_dict['rbracket']]

    integer_characters = {
        1: '1', 2: '2', 3: '3',
        4: '4', 5: '5', 6: '6', 7: '7',
        8: '8', 9: '9', 0: '0',
        '.': '.'}
    
    constants = [character_dict['pi'],
                 character_dict['euler']]

    constants_def = {character_dict['pi']: math.pi,
                 character_dict['euler']: math.e}


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
        
        # History file
        self.history_file = open('History.txt', 'a')

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

            button_dict[name].grid(
                row=rowno, column=columnno,
                sticky=tkinter.NSEW,
                pady=5, padx=5)
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
        self.namelist = [
            'clear', 'delete', 'factorial', 'add', 'alpha']
        Function_class.create_row(self.row1, self.namelist, 1,
                                  self.operation_frame,
                                  0, lambda: None)

        # Change commands of each button
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

        # Shift button
        self.shift_button = (Function_class.create_button
                             (self.operation_frame,
                              Characters.character_dict['shift'],
                              0, 0, button_bg, button_fg,
                              ("Arial 13 bold"), 1,
                              lambda: None, "#cccccc"))
        # Grid placement
        self.shift_button.grid(
            row=1, column=4, columnspan=3, sticky=tkinter.NSEW)

        # Command change
        self.shift_button.config(
            command=lambda: self.shift_convert())

        # Row 2
        self.namelist = [
            7, 8, 9, 'minus', 'sin', 'cos', 'tan']
        Function_class.create_row(self.row2, self.namelist, 2,
                                  self.operation_frame,
                                  0, lambda: None)

        # Change button commands
        for index, button in enumerate(self.row2):
            button.config(
                command=lambda index=index: self.printout(
                    self.row2[index]))
        # Row 3
        self.namelist = [4, 5, 6, 'times', 'log', 'ln', 'pi']
        Function_class.create_row(self.row3, self.namelist, 3,
                                  self.operation_frame,
                                  0, lambda: None)
        # Change button commands
        for index, button in enumerate(self.row3):
            button.config(
                command=lambda index=index: self.printout(
                    self.row3[index]))
        # Row 4
        self.namelist = [1, 2, 3, 'divide', 'xsquared', 'power']
        Function_class.create_row(self.row4, self.namelist, 4,
                                  self.operation_frame,
                                  0, lambda: None)
        # Change button commands
        for index, button in enumerate(self.row4):
            button.config(
                command=lambda index=index: self.printout(
                    self.row4[index]))

        # Change command for squared button 
        self.row4[4].config(
            command=lambda: self.printout_true(
                self.characters.character_dict['squared']))

        # Row 5
        self.namelist = [0, 'dot', 'lbracket', 'rbracket']
        Function_class.create_row(self.row5, self.namelist, 5,
                                  self.operation_frame, 2, lambda: None)
        # Change button commands
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
        # Equals button grid
        self.equal_button.grid(
            row=4, rowspan=2, column=6, sticky=tkinter.NSEW)
        # Equals command
        self.equal_button.config(
            command=lambda: self.equals())

        # Add all butons to a list, so they can
        # be located easily
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

        # Turn on keyboard bindings
        self.bindings()

    # Calculating function, when equals is pressed
    def equals(self):
        '''FOLLOW BEDMAS'''
        '''PARSE SIN, COS, TAN and etc as bracketed expressions'''
        '''This is what the equals button calls'''
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
           before or after the operator, present error. Otherwise,
           take the digits before and after the operator, and process them
           using the operator. Use a 'for' loop to scan from left to right.
           Once processed, a single float output should come out. Replace
           the previous digits, and operator, with this value in the input
           collection list.

        5. Once there are no times/divide, search for addition/subtraction.
           Look for the terms (Character.character_dict['add']) and
           (Character.character_dict['minus']).If there are no digits
           before or after the operator, present error. Otherwise, take the
           digits before and after the operator, and process them using the
           operator. Use a 'for' loop to scan from left to right. Once
           processed, a single float output should come out. Replace the
           previous digits, and operator, with this value in the input
           collection list.

        6. Finally, the result should be one float, which can be
           presented using self.print_result(float). This is the result
           of a bracket pair. Remove the brackets, and replace it with the
           result, then repeat the whole process for the other brackets
           until only one float remains muhahaha.'''

        self.processed = []  # List of processed characters
        self.temp_operator = []  # List of operators in input line
        self.temp_integer = []  # List of digits in input line
        self.compiled_number = []  # List of compiled numbers
        self.bracket_count = 0 # Amount of bracket pairs
        self.error_status = 0  # Error state
        self.to_calculate = self.added_list[:]
        
        '''1. Check for errors
           2. If errors, force user to change input. Else, continue to next step
           3. If brackets detected, search for most innermost pair
           4. Compile into an equation in a list
           5. Process equation to get a result
           6. If brackets detected, replace bracket pair with output value
           7. Repeat all steps if more bracket pairs detected'''
        
        # Check for errors in input
        '''This would ensure the input is able to be processed.
        and gives amount of bracket pairs if any are present'''
        self.error_checking(self.to_calculate)

        # If there are brackets in input
        if (Characters.character_dict['lbracket'] in
            self.added_list or Characters.character_dict['rbracket'] in
            self.to_calculate): 
            self.bracket_check(self.to_calculate)

        # Scan for innermost bracket pair (right now it only searches for one pair)
        while self.bracket_count > 0:
            self.lbracket_index = 0
            self.rbracket_index = 0
            # Get the equation in innermost brackets
            self.filtered = self.bracket_analysis(self.to_calculate)

            # Process equation
            self.bracket_equation = self.get_equation(self.filtered)

            # Calculate equation
            self.bracket_result = self.calculate(self.bracket_equation)

            # Replace brackets with processed equation
            self.to_calculate[self.lbracket_index:self.rbracket_index+1] = [self.bracket_result]

            # Reduce bracket counts
            self.bracket_count -= 1

        # Get an equation from list input
        '''Brackets should've been removed prior to this step'''
        self.equation = self.get_equation(self.to_calculate)
        self.answer = self.equation

        # If an error has not been raised
        if not self.error_status:
            if not self.temp_operator and self.compiled_number:
                print ('single digit,', self.answer)

            # If no input
            elif not self.compiled_number:
                pass

            else:
                self.final_answer = self.calculate(self.processed)
                print ('final', self.final_answer)
        else:
            # If error detected, do nothing
            pass
        '''printout answer'''
        # self.print_result()        

    # Process input and get an equation (compiling)
    def get_equation(self, List):
        self.temp_integer = []
        self.temp_operator = []
        self.compiled_number = []

        # Separate into operators and digits
        for index, term in enumerate(List):
            
            try:
                # Convert input to integer
                int_term = int(term)

                # Add to number list if it is an integer
                if (int(term) in Characters.integer_characters):
                    self.temp_integer.append(str(term))
                
                elif term == float(term):
                    self.temp_integer.append(str(term))
                
                else:
                    self.temp_integer.append(str(term))

            except:
                
                # If operation detected, join numbers together
                if term in Characters.operation_characters:
                    # Join previous integers together into
                    # one number and add to list
                    self.compiled_number.append(''.join(self.temp_integer))
                    self.temp_integer = []
                    self.temp_operator.append(term)

                # If a decimal dot
                elif term == Characters.integer_characters['.']:
                    self.temp_integer.append(term)

                # If a constant
                elif str(term) in Characters.constants:
                    self.temp_integer.append(str(Characters.constants_def[term]))
                    
                # If character is float (i.e. decimal)
                else:
                    self.temp_integer.append(str(term))

            # If the last item in a list is integer
            if index == len(List) - 1:
                self.compiled_number.append(''.join(self.temp_integer))
                self.temp_integer = []
    
        # If there are operators
        if self.temp_operator:
            '''Create a list that is the exact length of the
                compiled and operations lists, this ensures that
                list can perfectly hold the combined values
                of both lists'''
            self.processed = [None] * (len(
                    self.compiled_number) + len(self.temp_operator))

            # For every second value in list, insert a number
            self.processed[::2] = self.compiled_number
    
            # Starting from position 1, for every second value
            # from list, insert an operator
            self.processed[1::2] = self.temp_operator
            
            # Remove extra characters if present
            if '' in self.processed:
                self.processed.remove('')
            
        else:
            if len(self.compiled_number) == 1:
                self.processed = self.compiled_number[:]
    
        '''List with inputted characters
            - self.added_list = list of inputs
            - self.temp_integer = temporary list of
              integers from self.added_list
            - self.temp_operator = temporary list of detected operators
            - self.compiled_number = list of multidigit numbers
            - self.processed = Equation result from input'''

        return self.processed

    # Check for brackets
    def bracket_check(self, List):
        # Number of brackets in input
        self.lbracket_count = 0
        self.rbracket_count = 0

        for index, char in enumerate(List):
            if index != 0 and char == Characters.character_dict['lbracket']:
                if List[index-1] not in Characters.operation_characters:
                    self.error('syntax')
                    return ('error')

            # If item is a bracket
            if char in Characters.brackets:
                # If it's a left bracket
                if char == Characters.character_dict['lbracket']:
                    self.lbracket_count += 1

                # If it's a right bracket
                elif char == Characters.character_dict['rbracket']:
                    self.rbracket_count += 1
            

        # If there are brackets present
        if self.lbracket_count and self.rbracket_count > 0:
            # If brackets are even and closed
            if self.lbracket_count == self.rbracket_count:
                # Add one count to number of paired brackets
                # lbracket count used
                self.bracket_count = self.lbracket_count
        
        # Errors involving brackets
        # If brackets are uneven, thus open
        if self.lbracket_count != self.rbracket_count:
            self.error('syntax')

        # If last character is an open bracket (left)
        elif List[-1] == Characters.character_dict['lbracket']:
            self.error('syntax')

        # If first charcter is closing bracket (right)
        elif List[0] == Characters.character_dict['rbracket']:
            self.error('syntax')

    # For checking errors in input
    def error_checking(self, List):

        # Check each item in list
        for index, a in enumerate(List):
            
            # Check for operators/dot
            if (a in Characters.operation_characters or
                    a == Characters.character_dict['dot']):

                # If the character is a dot
                if a == Characters.character_dict['dot']:

                    if index != len(List) - 1:
                        # If double dots present
                        if List[
                            (List.index(
                                a)) + 1] == Characters.character_dict[
                                    'dot']:
                            # Raise error and clear screen
                            self.error('syntax')

                    # If dot is the last character
                    elif index == len(List) - 1:
                        # Raise error and clear screen
                        self.error('syntax')

                # If the first character is an operator or decimal dot
                if index == 0:
                    if (a in Characters.basic_operations or
                            a == Characters.character_dict['dot'] or
                            a in Characters.complex_before):
                        self.error('syntax')

                # While the character is not the last character
                elif index != len(List) - 1:
                    # If a double operations/dot present
                    if (
                        List[(List.index(
                            a)) + 1] in Characters.basic_operations or
                        List[(List.index(
                            a)) + 1] in Characters.complex_before):
                        if (
                            List[List.index(
                                a)] in Characters.basic_operations and
                            List[(List.index(a))+1] in
                            Characters.complex_before):
                            
                            # Raise error and clear screen
                            self.error('syntax')

            # If there are brackets present
            elif a in Characters.brackets:
                self.bracket_check(self.to_calculate)

            # If an operator is the last character
            elif index == len(List) - 1:
                if (a in Characters.complex_after or
                    a in Characters.basic_operations):
                    # Raise error and clear screen
                    self.error('syntax')
                        

    # The process of searching for bracket pairs
    def bracket_analysis(self, List):
        '''CURERNTLY: LEFT BRACKET SCANNER WORKS,
        BUT RIGHT BRACKET GOES TO THE FIRST RIGHT BRACKET,
        INSTEAD OF GOING TO THE RIGHT BRACKET AFTER THE INNERMOST LEFT BRACKET'''
        # Look for brackets
        if Characters.character_dict[
            'lbracket'] in List:

            # Variables
            self.bracket = [] # List of equation within brackets
            self.lbracket_index = 0 # Index of left bracket
            self.rbracket_index = 0 # Index of right bracket

            # Searches for the innermost left bracket
            # Search through the list backwards
            for i in reversed(range(len(self.to_calculate))):
                # If the item is a left bracket
                if self.to_calculate[i] == Characters.character_dict[
                    'lbracket']:
                    self.innermost_bracket = i
                    self.lbracket_index = i
                    break

            # For every character after the innermost left bracket
            for index, a in enumerate(List[self.innermost_bracket:]):

                # Add character to list
                self.bracket.append(a)

                # If the corresponding right bracket is found
                if a == Characters.character_dict['rbracket']:

                    # Stop adding characters
                    self.rbracket_index = ((self.lbracket_index)+index)
                    break

            # Remove the bracket characters from list
            while (Characters.character_dict[
                'lbracket'] in self.bracket or
                   Characters.character_dict[
                       'lbracket'] in self.bracket):              
                if Characters.character_dict['lbracket'] in self.bracket:
                    self.bracket.remove(Characters.character_dict['lbracket'])

                if Characters.character_dict['rbracket'] in self.bracket:
                    self.bracket.remove(Characters.character_dict['rbracket'])

            # The result of the characters in innermost brackets,
            # without the brackets
            return self.bracket
       

    # Calculations
    def calculate(self, List):
        # Remove blanks
        if '' in List:
            List.remove('')        
        
        # Scan every character in equation
        self.final_equation = List[:] # Copy of original list to use
        
        for index, x in enumerate(self.final_equation):
            
            # Order: Exponents, Factorial, Trigonometry and Logs, 
            # Multiply/Divide, Addition/Minus

            '''Calculations'''
            # For every character in list
            for index, a in enumerate(self.final_equation):
                # If a factorial or squared symbol. There
                # should only be 2 characters processed,
                # a number and an operator
                if a in Characters.complex_before:
                    '''Factorial only works for whole numbers'''
                    '''If factorial is a symbol'''
                    if a == Characters.character_dict['factorial']:
                        # Check for whole number
                        try:
                            # If number before factorial is whole,
                            # calculate
                            number = int(self.final_equation[index-1])
                            total = number
                            # Factorial process
                            total = math.factorial(total)
                            # Replace the number and ! character with the result
                            self.final_equation[index-1:index+1] = [total]
                        except:
                            # If a float is detected before factorial
                            self.error('math')
                    
                    '''If squared symbol detected'''
                    if a == Characters.character_dict['squared']:
                        # Multiply the number by itself
                        total = float(self.final_equation[
                            index-1])*float(self.final_equation[index-1])
                        # Replace symbol and number before the symbol
                        # with result
                        self.final_equation[index-1:index+1] = [total]
            
            # For all other complex operators, there should 
            # be either 2 or 3 characters processed, 
            # depending on the operator
            for index, a in enumerate (self.final_equation):
                # If character is a complex operator
                if a in Characters.complex_after:
                    '''If square root is a symbol'''
                    if a == Characters.character_dict['squareroot']:

                        # Square root the number after the symbol
                        # (Only positive numbers, otherwise raise error
                        if float(self.final_equation[index+1]) <= 0:
                            self.error('math')
                        else:
                            total = math.sqrt(float(
                                self.final_equation[index+1]))
                            self.final_equation[index:index+2] = [total]

                    '''If sin is a symbol'''
                    # Python assumes input is in radians for trigonometry
                    if a == Characters.character_dict['sin']:
                        # Convert input to radians first
                        total = math.sin(math.radians(
                            float(self.final_equation[index+1])))
                        self.final_equation[index:index+2] = [total]

                    '''If inverse sin is a symbol'''
                    if a == Characters.character_dict['inversesin']:

                        # If value is outside limit
                        if float(self.final_equation[
                            index+1]) > 1 or float(
                                self.final_equation[index+1]) < -1:
                            self.error('math')

                        # Convert output to degrees
                        else:
                            total = math.asin(float(
                                self.final_equation[index+1]))
                            total = math.degrees(total)
                            self.final_equation[index:index+2] = [total]                     
                    
                    
                    
                    '''If cos is a symbol'''
                    if a == Characters.character_dict['cos']:
                        # Convert input to radians
                        total = math.cos(math.radians(
                            float(self.final_equation[index+1])))
                        self.final_equation[index:index+2] = [total]                     
                    
                    
                    '''If inverse cos is a symbol'''
                    if a == Characters.character_dict['inversecos']:

                        # If value is outside limit
                        if float(self.final_equation[
                            index+1]) > 1 or float(
                                self.final_equation[index+1]) < -1:
                            self.error('math')

                        else:
                            # Use inverse cos, which has an input range of -1<0<1
                            total = math.acos(float(
                                self.final_equation[index+1]))
                            total = math.degrees(total)
                            self.final_equation[index:index+2] = [total]

                    '''If tan is a symbol'''
                    if a == Characters.character_dict['tan']:
                        # Use tan, convert input to radians
                        # first to get degree output
                        total = math.tan(math.radians(
                            float(self.final_equation[index+1])))
                        self.final_equation[index:index+2] = [total]                     
                    
                    '''If inverse tan is a symbol'''
                    if a == Characters.character_dict['inversetan']:
                        # Use inverse tan, returns result in radians
                        total = math.atan((float(
                            self.final_equation[index+1])))
                        # Convert to degrees
                        total = math.degrees(total)
                        self.final_equation[
                            index:index+2] = [total]                     

                    '''If log is a symbol'''
                    if a == Characters.character_dict['log']:
                        # Use log base 10
                        total = math.log10(float(
                            self.final_equation[index+1]))
                        self.final_equation[
                            index:index+2] = [total]
                    
                    '''If Ln is a symbol'''
                    if a == Characters.character_dict['ln']:
                        # Use natural log
                        total = math.log(float(
                            self.final_equation[index+1]))
                        self.final_equation[
                            index:index+2] = [total]


            # For powers and roots, which take 2 number values
            # If power is a symbol
            while (
                Characters.character_dict[
                    'power'] in self.final_equation) or (
                        Characters.character_dict[
                            'root'] in self.final_equation):
                for index, a in enumerate (self.final_equation):
                    if a == Characters.character_dict['power']:
    
                        # Raise the number before symbol to the number after symbol
                        # i.e. before ^ after
                        total = float(self.final_equation[
                            index-1])**float(self.final_equation[index+1])
    
                        # Replace the 3 characters with the result
                        self.final_equation[index-1:index+2] = [total]
    
                    if a == Characters.character_dict['root']:
                        if float(self.final_equation[index+1]) <= 0:
                            '''If the error doesn't reset program, insert a try&except'''
                            self.error('math')
                        else:
                            # Nth root of X == X^(1/N)
                            total = float(
                                self.final_equation[
                                    index+1])**(1/(
                                        float(self.final_equation[index-1])))
                            self.final_equation[index-1:index+2] = [total]
                            break

            # For multiply/divide. There should only be 3
            # characters processed, 2 numbers and an operator
            while (
                Characters.character_dict[
                    'times'] in self.final_equation) or (
                        Characters.character_dict[
                            'divide'] in self.final_equation):
                    for index, a in enumerate (self.final_equation):
                        '''If multiply (x) is a symbol'''
                        if a == Characters.character_dict['times']:
                                total = float(
                                    self.final_equation[
                                        index-1])*float(
                                            self.final_equation[
                                                index+1])
                                self.final_equation[
                                    index-1:index+2] = [total]
                                break

                        '''If divide (\u00f7) is a symbol'''
                        if a == Characters.character_dict['divide']:
                                total = float(
                                    self.final_equation[
                                        index-1])/float(
                                            self.final_equation[
                                                index+1])
                                self.final_equation[
                                    index-1:index+2] = [total]
                                break
            
            '''Adding/minus is same procedure as times/divide'''
            while (
                Characters.character_dict['add'] in
                self.final_equation or Characters.character_dict[
                    'minus'] in self.final_equation):
                    for index, a in enumerate (self.final_equation):
                        '''If addition (+) is a symbol'''
                        if a == Characters.character_dict['add']:
                                total = float(
                                    self.final_equation[
                                        index-1])+float(
                                            self.final_equation[
                                                index+1])
                                self.final_equation[
                                    index-1:index+2] = [total]
                                break

                        '''If subtraction (-) is a symbol'''
                        if a == Characters.character_dict['minus']:
                                total = float(
                                    self.final_equation[
                                        index-1])-float(
                                            self.final_equation[index+1])
                                self.final_equation[
                                    index-1:index+2] = [total]
                                break

            # Return answer
            return (self.final_equation[0])

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

        # Complex arithmetics
        cplx_dict = {'!':'factorial', 's':'sin',
                     'c':'cos', 't':'tan',
                     'l':'log', 'n':'ln', 'p':'pi'}
        for t in cplx_dict:
            self.operation_window.bind(
                str(t), lambda command,
                t=t: self.keys(
                    self.characters.character_dict[
                        cplx_dict[t]]))

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
            self.error('unknown')

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
            self.row1[4].config(bg='#a6a6a6')

            for a in self.allrows:
                # If the label of a button matches
                # a character in shift dictionary
                if a['text'] in Characters.shift_characters:
                    self.convert1 = Characters.shift_characters[a['text']]
                    a.config(text=self.convert1,
                             command=lambda x=a: self.printout(x))
                else:
                    pass
            # Toggle
            self.toggle = 0

        # If shifted
        elif self.toggle == 0 and self.a_toggle == 1:
            # Change color of SHIFT
            self.row1[4].config(bg='#f2f2f2')

            # Inverterd shift dictionary
            self.converted = {value: key for (
                key, value) in Characters.shift_characters.items()}

            for a in self.allrows:
                # If the label of a button matches
                # a character in shift dictionary
                if a['text'] in self.converted:
                    self.convert1 = self.converted[a['text']]
                    a.config(text=self.convert1,
                             command=lambda x=a: self.printout(x))
                else:
                    pass
            # Toggle
            self.toggle = 1

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
        
        self.file4 = open('Bottom help.txt', 'r')
        self.b_help = (self.file4.read())

        # This disables the corresponding button in the main menu
        button_dict["Help"].config(state=tkinter.DISABLED)

        # Create window and frame
        self.Help_window = tkinter.Toplevel()
        self.Help_window.title('Help')

        self.Help_frame = tkinter.Frame(self.Help_window,
                                        bg="#ffffff")
        self.Help_frame.grid()

        # Help text, separated into 4 texts
        self.text_top = tkinter.Label(
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
        self.text_top.grid(row=0, columnspan=3)

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

        self.text_bottom = tkinter.Label(
            self.Help_frame,
            text=self.b_help,
            anchor=tkinter.CENTER,
            bg="#ffffff",
            fg="#000000",
            font=('Arial, 11'),
            bd=10,
            padx=10,
            pady=10)

        self.text_bottom.grid(
            row=2, columnspan = 2,
            sticky=tkinter.NSEW)

        # Exit button
        self.exit_button_help = Function_class.exit_button(self.Help_frame, 3,
                                                      "Help", self.Help_window)
        self.exit_button_help.grid(sticky=tkinter.SW)


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

        # Text
        self.text1 = tkinter.Label(
            self.recall_frame,
            text="Here, you can view your past calculations!")
        self.text1.grid(row=0, column=0)
        
        self.text2 = tkinter.Label(
            self.recall_frame,
            text="Unfortunately, this is still in development")
        
        self.text2.grid(row=1, column=0)
        
        # Listbox
        self.listbox = tkinter.Listbox(self.recall_window)
        self.listbox.grid(column = 1,
                          rowspan = 3,
                          row = 0,
                          sticky = tkinter.NSEW)
        
        # Clear button
        self.clear_button = tkinter.Button(
            self.recall_frame,
            text='Clear file')
        self.clear_button.grid(
            row=4, columnspan = 3,
            sticky=tkinter.NSEW)
        

        # Exit button
        self.exit_button_recall = (
            Function_class.exit_button(
                self.recall_frame, 4,
                "Recall", self.recall_window))
        self.exit_button_recall.grid(
            column = 0, row = 5, sticky = tkinter.SW)
        


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
