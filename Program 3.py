# Long distance Calls

import tkinter
import tkinter.messagebox


class call_calculator:
    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()

        # Create radiobutton frame and button frame
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create an Invar object to use the Radiobuttons
        self.radio_var = tkinter.IntVar()

        # Set the intVar object to 1
        self.radio_var.set(1)

        # create the Radiobutton widgets in the top_frame
        self.rb1 = tkinter.Radiobutton(self.top_frame,
                                       text="Daytime (6:00 A.M through 5:59 P.M.) at $0.02 per minute", variable=self.radio_var, value= 1 )
        self.rb2 = tkinter.Radiobutton(self.top_frame,
                                       text= 'Evening (6:00 P.M.  through 11:59 P.M.) at $0.12 per minute', variable=self.radio_var, value=2)
        self.rb3 = tkinter.Radiobutton(self.top_frame,
                                       text="Off-Peak (midnight through 5:59 P.M.) at $0.05 per minute", variable=self.radio_var, value=3 )

        #Create Entry value
        self.minutes = tkinter.Label(self.top_frame, text='Please enter how long your call was in minutes')

        self.value_entry1 = tkinter.Entry(self.top_frame)
        #pack the Entry value
        self.minutes.grid(row = 0, column = 0)
        self.value_entry1.grid(row = 0, column = 1)
        # packb the Radiobuttons
        self.rb1.grid(row = 1, column = 0)
        self.rb2.grid(row = 2, column = 0)
        self.rb3.grid(row = 3, column = 0)

        # Create OK and Quit buttons
        self.calculate = tkinter.Button(self.bottom_frame,
                                        text='OK', command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Quit', command=self.main_window.destroy)

        # Pack the buttons
        self.calculate.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Start the Main loop
        tkinter.mainloop()

        # the show_choice method is the callback function for the OK button

    def show_choice(self):
        if self.radio_var.get() == 1:
            total_cost = float(self.value_entry1.get()) * 0.02
        if self.radio_var.get() == 2:
            total_cost = float(self.value_entry1.get()) * 0.12
        if self.radio_var.get() == 3:
            total_cost = float(self.value_entry1.get()) * 0.05

        tkinter.messagebox.showinfo('Selection', f"Your total is ${total_cost}")




if __name__ == '__main__':
    my_gui = call_calculator()
