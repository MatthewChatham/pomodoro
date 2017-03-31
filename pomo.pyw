# Pomodoro Timer
# Created by Matthew Chatham
#
# This application implements a simple version of the Pomodoro Technique.
#
#

import tkinter as tk
import datetime as dt

# Simple timer
class App():

    MINUTES = 25
    SECONDS = 0
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.resizable(0,0)
        self.root.lift()
        self.root.attributes('-topmost', True)
        self.clock = dt.datetime(year=1,
                                 month=1,
                                 day=1,
                                 minute=self.MINUTES,
                                 second=self.SECONDS)
        self.current = tk.StringVar()
        self.current.set(self.clock.strftime('%M:%S'))
        self.label = tk.Label(textvariable=self.current,
                              font=('',25))
        self.label.grid()
        self.startbutton = tk.Button(text='Start / Reset Timer',
                                     command=self.update_clock,
                                     font=('',16))
        self.startbutton.grid()
        self.root.mainloop()

    def update_clock(self):
        if self.current.get() == 'Done!':
            self.clock = dt.datetime(year=1,
                                 month=1,
                                 day=1,
                                 minute=self.MINUTES,
                                 second=self.SECONDS)
            self.current.set(self.clock.strftime('%M:%S'))
            return
        if self.clock.strftime('%M:%S') == '00:00':
            self.current.set('Done!')
            self.root.deiconify()
            return
        self.clock = self.clock - dt.timedelta(seconds=1)
        self.current.set(self.clock.strftime('%M:%S'))
        self.root.after(1000, self.update_clock)

app=App()
