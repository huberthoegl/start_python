
# Taken from Python-Kurs by Bernd Klein
# https://www.python-kurs.eu/python_tkinter.php

# Entry Widget https://www.python-kurs.eu/tkinter_entry_widgets.php

from tkinter import *

master = Tk()
Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

mainloop()
