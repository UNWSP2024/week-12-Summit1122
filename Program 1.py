# Miles per gallon generator
# By: Luis Amador
# 11/21/24

import tkinter

class milespergallon:
    def __init__(self):
        #window

        self.main_window = tkinter.Tk()
        self.main_window.title("Miles per gallon calculator")


        # Create two frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #Create a value labels in the top frame
        self.gallons_label = tkinter.Label(self.top_frame, text = 'Please enter how many'
                                                             'Gallons you car can hold')
        self.value_entry1 = tkinter.Entry(self.top_frame)
        self.value_entry1.grid(column = 1, row = 0)
        self.miles_label = tkinter.Label(self.top_frame, text = 'Please enter how many miles'
                                                            'your car can drive on a full tank')
        self.value_entry2 = tkinter.Entry(self.top_frame)
        self.value_entry2.grid(column = 3, row = 0)

        #result label
        self.result_label = tkinter.Label(self.bottom_frame, text = 'MPG:')
        self.result_label.grid(column = 0, row = 0)
        self.result_value = tkinter.Label(self.bottom_frame, text = '')
        self.result_value.grid(column = 1, row = 0)


        def math_calc():
            try:
                gallons= float(self.value_entry1.get())
                miles = float(self.value_entry2.get())
                mpg = miles / gallons
                self.result_value.config(text = mpg)
            except ValueError:
                self.result_value.config(text="Invalid input")


       #Create the Calculate button
        self.calculate = tkinter.Button(self.bottom_frame, text = 'Calculate'
                                        , command = math_calc)



        self.quit_button = tkinter.Button(self.bottom_frame, text = 'Quit',
                                          command = self.main_window.destroy)
        self.calculate.grid(column = 2, row = 0)
        self.quit_button.grid(column = 3, row = 0)

        #pack the labels
        self.gallons_label.grid(row = 0, column = 0)
        self.miles_label.grid(row = 0, column = 2)

        #pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        #enter mainloop
        tkinter.mainloop()





if __name__ == "__main__":
    mygui = milespergallon()