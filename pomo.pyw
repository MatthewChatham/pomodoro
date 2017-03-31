# Pomodoro Timer
# Created by Matthew Chatham
#
# This application implements a simple version of the Pomodoro Technique.
#
#

import tkinter as tk
import tkinter.simpledialog as sd
import datetime as dt

# Simple timer
class App():

    MINUTES = 0
    SECONDS = 3
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.resizable(0,0)
        self.root.lift()
        self.root.attributes('-topmost', True)

        
        self.goPresses = 0
        self.counting = False
        self.pomoCount = 0
        self.pomoCountLabel = tk.StringVar()
        self.pomoCountLabel.set('Pomos completed: {}'.format(self.pomoCount))


        self.pomos = []
        self.pomoText = tk.StringVar()
        self.pomoText.set('Pomos:')

        
        self.clock = dt.datetime(year=1,
                                 month=1,
                                 day=1,
                                 minute=self.MINUTES,
                                 second=self.SECONDS)
        self.current = tk.StringVar()
        self.current.set(self.clock.strftime('%M:%S'))
        self.clockLabel = tk.Label(textvariable=self.current,
                              font=('',25))


        self.task = tk.StringVar()
        self.task.set('Task:')
        self.taskLabel = tk.Label(textvariable=self.task,
                                  font=('',25))

        
        self.setbutton = tk.Button(text='Set a pomo',
                                     command=self.set_pomo,
                                     font=('',16))


        self.gobutton = tk.Button(text='GO!',
                                  command=self.go,
                                  font=('',16))

        self.resetbutton = tk.Button(text='Reset',
                                     command=self.reset_clock,
                                     font=('',16))


        self.countLabel = tk.Label(textvariable=self.pomoCountLabel,
                                   font=('',16))


        self.pomosLabel = tk.Label(textvariable=self.pomoText,
                                   font=('',16))


        self.clockLabel.grid()
        self.taskLabel.grid()
        self.setbutton.grid()
        self.gobutton.grid()
        self.resetbutton.grid()
        self.countLabel.grid()
        self.pomosLabel.grid()

        
        self.root.mainloop()

    def go(self):
        self.goPresses += 1
        self.counting = True
        if self.goPresses == 1:
            self.update_clock()
            pomo = {'name': self.task.get()[6:],
                    'start': dt.datetime.now().strftime('%H:%M'),
                    'end': (dt.datetime.now() + dt.timedelta(minutes=self.MINUTES, seconds=self.SECONDS)).strftime('%H:%M')}
            self.pomos.append(pomo)


    def update_clock(self):
        if self.counting:
            if self.clock.strftime('%M:%S') == '00:00':
                self.current.set('One pomodoro down!')
                self.root.deiconify()
                self.pomoCount += 1
                self.pomoCountLabel.set('Pomos completed: {}'.format(self.pomoCount))
                self.pomoText.set(self.pomoText.get() + '\n{} - {}: {}'.format(self.pomos[-1]['start'],
                                                                                   self.pomos[-1]['end'],
                                                                                   self.pomos[-1]['name']))
                return
            self.clock = self.clock - dt.timedelta(seconds=1)
            self.current.set(self.clock.strftime('%M:%S'))
            self.root.after(1000, self.update_clock)

    def set_pomo(self):
        dialog = sd.askstring(title='Task', prompt='Enter task:')
        if dialog: self.task.set('Task: ' + dialog)

    def reset_clock(self):
        self.clock = dt.datetime(year=1,
                                 month=1,
                                 day=1,
                                 minute=self.MINUTES,
                                 second=self.SECONDS)
        self.current.set(self.clock.strftime('%M:%S'))
        self.counting = False
        self.goPresses = 0

app=App()
