import tkinter as tk

class calculators:
    calculations = ""  # This variable will contian the formula that will be executed (what the user have like input)

    def add_to_calculate(self,operation): 
        """
        This function will add what the user type to calculations variable and then deleting the text label were the user execute the numbers, operator etc...
        And then insert the new formula into the text label
        """
        self.calculations += str(operation)
        self.text_result.delete(1.0 , "end")
        self.text_result.insert(1.0 , self.calculations)
        return self.calculations

    def wich_button_clicked(self , button):
        """
        By this function we can determinate wich button was clicked by the user so put the write thing in the text label
        """
        if button == "7":
            self.add_to_calculate(7)
        elif button == "8":
            self.add_to_calculate(8)
        elif button == "9":
            self.add_to_calculate(9)
        elif button == "X":
            self.add_to_calculate("*")
        elif button == "4":
            self.add_to_calculate(4)
        elif button == "5":
            self.add_to_calculate(5)
        elif button == "6":
            self.add_to_calculate(6)
        elif button == "-":
            self.add_to_calculate("-")
        elif button == "1":
            self.add_to_calculate(1)
        elif button == "2":
            self.add_to_calculate(2)
        elif button == "3":
            self.add_to_calculate(3)
        elif button == "+":
            self.add_to_calculate("+")
        elif button == "0":
            self.add_to_calculate(0)
        elif button == ",":
            self.add_to_calculate(",")
        elif button == "+/-":
            self.add_to_calculate("(-")
        elif button == "/":
            self.add_to_calculate("/")
        elif button == "()":
            self.add_to_calculate("()")
        elif button == "=":
            self.calculating_formula()

    def clear(self):
        """
        This function delete (clean) the text label and clear the calculation variable that contains the formula
        """
        self.text_result.delete(1.0 , "end")
        self.calculations = ""

    def calculating_formula(self):
        """
        This function give us the result : after this processe:
        1/ deleting the text label so we can put the result . 2/ what we know about eval() is The return value is the result of the evaluated expression
        so in this case we pass it the formula as an argument (type(formula)--> str) and eval() will solve the operation
        3/ And then we show the result in the text label using insert()
        4/ But if eval has a problem were the formula isn't correct or something we will move to except statment
        """
        self.text_result.delete(1.0 , "end")
        try:
            self.calculations = eval(self.calculations)
            self.text_result.insert(1.0 , self.calculations)
        except :
            self.text_result.insert(1.0 , "Error")

    def __init__(self) :
        self.root = tk.Tk()
        self.root.title("Calculator") # Giving the window a title "Calculator"
        self.root.iconbitmap(r"C:\Users\DELL\Desktop\calculatrice\1486395290-09-calculator_80565.ico") # Putting an icon for the app
        
        self.text_result = tk.Text(self.root , font=("Arial",25) , height=4 , width=15)
        self.text_result.pack(fill="x")
        
        self.frame = tk.Frame(self.root) # Initializing a frame that will contain a the buttons
        self.frame.columnconfigure(0 , weight=1) # Creating columns and rows
        self.frame.columnconfigure(1 , weight=1) 
        self.frame.columnconfigure(2 , weight=1) 
        self.frame.columnconfigure(3 , weight=1) 
        self.frame.columnconfigure(4 , weight=1) 
        
        """
        //// The lambda function in the buttons is like a shortcut of this code :        
        # def exampl(button = "+/-"):
        #     self.wich_button_clicked(button) 
        """

        self.btn1 = tk.Button(self.frame , text="AC" , bg="Grey",font=("Arial",25) , command=self.clear) # Creating button for clear the output or the input
        self.btn1.grid(row=0 , column=0 , sticky=tk.E+tk.W)
        self.btn2 = tk.Button(self.frame , text="+/-" , bg="Grey",font=("Arial",25) , command= lambda button = "+/-" : self.wich_button_clicked(button))
        self.btn2.grid(row=0 , column=1 , sticky=tk.E+tk.W)
        self.btn3 = tk.Button(self.frame , text="()" , bg="Grey",font=("Arial",25) , command= lambda button = "()" : self.wich_button_clicked(button))
        self.btn3.grid(row=0 , column=2 , sticky=tk.E+tk.W)
        self.btn4 = tk.Button(self.frame , text="➗" , bg="Yellow",font=("Arial",25) , command= lambda button = "/" : self.wich_button_clicked(button))
        self.btn4.grid(row=0 , column=3 , sticky=tk.E+tk.W)

        self.btn5 = tk.Button(self.frame , text="7" , bg="Blue",font=("Arial",25) , command= lambda button = "7" : self.wich_button_clicked(button))
        self.btn5.grid(row=1 , column=0 , sticky=tk.E+tk.W)
        self.btn6 = tk.Button(self.frame , text="8" , bg="Blue",font=("Arial",25) , command= lambda button = "8" : self.wich_button_clicked(button))
        self.btn6.grid(row=1 , column=1 , sticky=tk.E+tk.W)
        self.btn7 = tk.Button(self.frame , text="9" , bg="Blue",font=("Arial",25) , command= lambda button = "9" : self.wich_button_clicked(button))
        self.btn7.grid(row=1 , column=2 , sticky=tk.E+tk.W)
        self.btn8 = tk.Button(self.frame , text="X" , bg="Yellow",font=("Arial",25) , command= lambda button = "X" : self.wich_button_clicked(button))
        self.btn8.grid(row=1 , column=3 , sticky=tk.E+tk.W )

        self.btn9 = tk.Button(self.frame , text="4" , bg="Blue",font=("Arial",25) , command= lambda button = "4" : self.wich_button_clicked(button))
        self.btn9.grid(row=2 , column=0 , sticky=tk.E+tk.W)
        self.btn10 = tk.Button(self.frame , text="5" , bg="Blue",font=("Arial",25) , command= lambda button = "5" : self.wich_button_clicked(button))
        self.btn10.grid(row=2 , column=1 , sticky=tk.E+tk.W)
        self.btn11 = tk.Button(self.frame , text="6" , bg="Blue",font=("Arial",25) , command= lambda button = "6" : self.wich_button_clicked(button))
        self.btn11.grid(row=2 , column=2 , sticky=tk.E+tk.W)
        self.btn12 = tk.Button(self.frame , text="-" , bg="Yellow",font=("Arial",25) , command= lambda button = "-" : self.wich_button_clicked(button))
        self.btn12.grid(row=2 , column=3 , sticky=tk.E+tk.W)

        self.btn13 = tk.Button(self.frame , text="1" , bg="Blue",font=("Arial",25) , command= lambda button = "1" : self.wich_button_clicked(button))
        self.btn13.grid(row=3 , column=0 , sticky=tk.E+tk.W)
        self.btn14 = tk.Button(self.frame , text="2" , bg="Blue",font=("Arial",25) , command= lambda button = "2" : self.wich_button_clicked(button))
        self.btn14.grid(row=3 , column=1 , sticky=tk.E+tk.W)
        self.btn15 = tk.Button(self.frame , text="3" , bg="Blue",font=("Arial",25) , command= lambda button = "3" : self.wich_button_clicked(button))
        self.btn15.grid(row=3 , column=2 , sticky=tk.E+tk.W)
        self.btn16 = tk.Button(self.frame , text="+" , bg="Yellow",font=("Arial",25) , command= lambda button = "+" : self.wich_button_clicked(button))
        self.btn16.grid(row=3 , column=3 , sticky=tk.E+tk.W)

        self.btn17 = tk.Button(self.frame , text="0" , bg="Blue",font=("Arial",25) , command= lambda button = "0" : self.wich_button_clicked(button))
        self.btn17.grid(row=4 , column=0 , sticky=tk.E+tk.W )
        self.btn18 = tk.Button(self.frame , text="0" , bg="Blue",font=("Arial",25) , command= lambda button = "0" : self.wich_button_clicked(button))
        self.btn18.grid(row=4  , sticky=tk.E+tk.W, )
        self.btn19 = tk.Button(self.frame , text="," , bg="Blue",font=("Arial",25) , command= lambda button = "," : self.wich_button_clicked(button))
        self.btn19.grid(row=4 , column=2 , sticky=tk.E+tk.W)
        self.btn20 = tk.Button(self.frame , text="=" , bg="Yellow",font=("Arial",25)  , command= lambda button = "=" : self.wich_button_clicked(button))
        self.btn20.grid(row=4 , column=3 , sticky=tk.E+tk.W)
        
        self.frame.pack(fill = "both")

        self.root.mainloop()

calculators()