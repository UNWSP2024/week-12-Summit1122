# Joe's Pricing Calculator
# By: Luis Amador
# 11/21/24

import tkinter
import tkinter.messagebox


class pricing:
    def __init__(self):
        # Create the main window

        self.main_window = tkinter.Tk()

        # Create radiobutton frame and button frame
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # clicked button function
        def clicked():
            total = 0
            if self.var1.get() == 1:
                total += 30
            else:
                total += 0
            if self.var2.get() == 1:
                total += 20
            else:
                total += 0
            if self.var3.get() == 1:
                total += 40
            else:
                total += 0
            if self.var4.get() == 1:
                total += 100
            else:
                total += 0
            if self.var5.get() == 1:
                total += 35
            else:
                total += 0
            if self.var6.get() == 1:
                total += 200
            else:
                total += 0
            if self.var7.get() == 1:
                total += 20
            else:
                total += 0

            tkinter.messagebox.showinfo('Checkout', f"Your total will be ${total} dollars" )


        # Create an Invar object to use the checkboxes
        self.var1 = tkinter.IntVar()
        self.var2 = tkinter.IntVar()
        self.var3 = tkinter.IntVar()
        self.var4 = tkinter.IntVar()
        self.var5 = tkinter.IntVar()
        self.var6 = tkinter.IntVar()
        self.var7 = tkinter.IntVar()

        # create the Radiobutton widgets in the top_frame
        self.oil = tkinter.Checkbutton(self.top_frame,
                                       text="Oil Change: $30.00", variable=self.var1, onvalue=1, offvalue=0)
        self.oil_value = tkinter
        self.lube = tkinter.Checkbutton(self.top_frame,
                                       text="Lube Job: $20.00",variable=self.var2, onvalue=1, offvalue=0)

        self.radiator = tkinter.Checkbutton(self.top_frame,
                                       text="Radiator flushL $40:00",variable=self.var3, onvalue=1, offvalue=0)

        self.transmission = tkinter.Checkbutton(self.top_frame,
                                       text="Transmission Fluid: $100.00", variable=self.var4, onvalue=1, offvalue=0)
        self.inspection = tkinter.Checkbutton(self.top_frame,
                                        text="Inspection: $35.00",variable=self.var5, onvalue=1, offvalue=0 )
        self.muffler = tkinter.Checkbutton(self.top_frame,
                                            text="Muffler Replacement: $200.00", variable=self.var6, onvalue=1, offvalue=0)
        self.tire = tkinter.Checkbutton(self.top_frame, text = "Tire Rotation: $20.00", variable = self.var7, onvalue = 1, offvalue = 0)
        # packing the checkboxes
        self.oil.pack()
        self.lube.pack()
        self.radiator.pack()
        self.transmission.pack()
        self.inspection.pack()
        self.muffler.pack()
        self.tire.pack()


        # Create OK and Quit buttons
        self.total = tkinter.Button(self.bottom_frame,
                                        text='Checkout', command=clicked)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Quit', command=self.main_window.destroy)

        # Pack the buttons
        self.total.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Start the Main loop
        tkinter.mainloop()

        # the show_choice method is the callback function for the OK button




if __name__ == '__main__':
    my_gui = pricing()

