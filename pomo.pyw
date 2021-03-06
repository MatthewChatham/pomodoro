# Pomodoro Timer
# Created by Matthew Chatham
#
# This application implements a simple version of the Pomodoro Technique.
#
#

import tkinter as tk
import tkinter.simpledialog as sd
import tkinter.messagebox as mb
import datetime as dt

# Simple timer
class App():

    MINUTES = 0
    SECONDS = 2
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.wm_title("Pomodoro Timer")
        self.root.resizable(0,0)
        self.root.minsize(width=500, height=150)
        self.root.lift()
        self.root.attributes('-topmost', True)
        self.root.protocol("WM_DELETE_WINDOW", self.export_pomos)
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.iconbitmap('pomo.ico')
        
        self.goPresses = 0
        self.counting = False
        self.pomoCountLabel = tk.StringVar()
        


        self.pomos = []
        self.pomoCount = len(self.pomos)
        self.pomoCountLabel.set('{}'.format(self.pomoCount))
        self.init = dict()
        self.breaks = []
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
                              font=('',20),
                                   relief=tk.SUNKEN,
                                   bg="Orange")


        self.task = tk.StringVar()
        self.task.set('Task:')
        self.taskLabel = tk.Label(textvariable=self.task,
                                  font=('',25))

        
        self.setbutton = tk.Button(text='Set a pomo',
                                     command=self.set_pomo,
                                     font=('',16),
                                   bg="Light Gray")


        self.gobutton = tk.Button(text='GO!',
                                  command=self.go,
                                  font=('',16),
                                  bg="Light Green")

        self.resetbutton = tk.Button(text='END / RESET',
                                     command=self.reset_clock,
                                     font=('',16),
                                     bg="Red")


        self.countLabel = tk.Label(textvariable=self.pomoCountLabel,
                                   font=('',16))


        self.pomosLabel = tk.Label(textvariable=self.pomoText,
                                   font=('',16))

        self.taskLabel.grid(columnspan=2)
        self.clockLabel.grid(columnspan=2, pady=5)
        self.setbutton.grid(columnspan=2)
        self.gobutton.grid(sticky=tk.E, padx=2.5)
        self.resetbutton.grid(row=3, column=1, sticky=tk.W, padx=2.5, pady=5)
        #self.countLabel.grid(row=0,column=3)
        self.pomosLabel.grid(columnspan=2)

        
        self.root.mainloop()

    def go(self):
        if self.clock.strftime('%M:%S') == '00:00':
            self.reset_clock()
            self.go()
            return
        if len(self.pomos) == 0:
            arrival = sd.askstring(title='Arrival Time', prompt='When did you arrive at work?')
            if arrival == None: return
            try: arrival = dt.datetime.strptime(arrival, '%H:%M')
            except:
                mb.showwarning(title='Warning!', message='Please enter a valid time.')
                return
            arrival = arrival.strftime('%H:%M')
            activity = sd.askstring(title='Setting Up', prompt='What have you been doing since getting to work?')
            if activity == None: return
            activity = '"' + activity + '"'
            initial = {'name': activity,
                       'type': 'Initial',
                       'start': arrival,
                       'end': dt.datetime.now().strftime('%H:%M')}
            self.init = initial
        elif len(self.pomos) > 0 and not self.counting:
            activity = sd.askstring(title='Break', prompt='What have you been doing since the last pomo?')
            if activity == None:
                return
            activity = '"' + activity + '"'
            brk = {'name': activity,
                   'type': 'Break',
                   'start': self.pomos[-1]['end'],
                   'end': dt.datetime.now().strftime('%H:%M')}
            self.breaks.append(brk)
        self.goPresses += 1
        self.counting = True
        if self.goPresses == 1:
            self.update_clock()
            pomo = {'name': '"' + self.task.get()[6:] + '"',
                    'type': 'Pomodoro',
                    'start': dt.datetime.now().strftime('%H:%M'),
                    'end': (dt.datetime.now() + dt.timedelta(minutes=self.MINUTES, seconds=self.SECONDS)).strftime('%H:%M')}
            self.pomos.append(pomo)
            self.pomoCount += 1


    def update_clock(self):
        if self.counting:
            if self.clock.strftime('%M:%S') == '00:00':
                self.current.set('One pomodoro down!')
                self.root.deiconify()
                self.pomoCountLabel.set('Pomos completed: {}'.format(self.pomoCount))
                self.pomoText.set(self.pomoText.get() + '\n{} - {}: {}'.format(self.pomos[-1]['start'],
                                                                                   self.pomos[-1]['end'],
                                                                                   self.pomos[-1]['name'].strip('"')))
                self.counting = False
                if self.pomoCount % 4 == 0: mb.showwarning(title='Take a break!', message='Time to take a longer break!')
                return
            self.clock = self.clock - dt.timedelta(seconds=1)
            self.current.set(self.clock.strftime('%M:%S'))
            self.root.after(1000, self.update_clock)

    def set_pomo(self):
        if self.counting == False:
            dialog = sd.askstring(title='Task', prompt='Enter task:')
            if dialog:
                dialog = '"' + dialog + '"'
                self.task.set('Task: ' + dialog.strip('"'))
            else: return

    def reset_clock(self):
        if self.counting:
            self.pomos[-1]['end'] = dt.datetime.now().strftime("%H:%M")
            self.pomoCountLabel.set('Pomos completed: {}'.format(self.pomoCount))
            self.pomoText.set(self.pomoText.get() + '\n{} - {}: {}'.format(self.pomos[-1]['start'],
                                                                           self.pomos[-1]['end'],
                                                                           self.pomos[-1]['name'].strip('"')))
            if self.pomoCount % 4 == 0: mb.showwarning(title='Take a break!', message='Time to take a longer break!')
        self.clock = dt.datetime(year=1,
                                 month=1,
                                 day=1,
                                 minute=self.MINUTES,
                                 second=self.SECONDS)
        self.current.set(self.clock.strftime('%M:%S'))
        self.counting = False
        self.goPresses = 0

    def export_pomos(self):
        if self.init:
            with open('Log' + '.csv', 'a') as outfile:
                day = list()
                day.append(self.init)
                for i in range(len(self.pomos) - 1):
                    day.append(self.pomos[i])
                    day.append(self.breaks[i])
                else: day.append(self.pomos[-1])


                activity = sd.askstring(title='Finishing Up', prompt='What have you been doing since your last pomo?')
                if activity == None: return
                activity = '"' + activity + '"'
                ending = {'name': activity,
                       'type': 'Final',
                       'start': self.pomos[-1]['end'],
                       'end': dt.datetime.now().strftime('%H:%M')}
                day.append(ending)
                for item in day:
                    outfile.write('{},{},{},{},{}\n'.format(dt.datetime.now().strftime('%b %d'),
                                                            item['start'],
                                                            item['end'],
                                                            item['name'],
                                                            item['type']))
        self.root.destroy()

app=App()
