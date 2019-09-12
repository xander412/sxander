#!/usr/bin/env python3
from tkinter import *
import subprocess
from threading import *
class Menu:
    def __init__(self):
        self.mw = Tk()
        self.mw.geometry("1200x1200")
        self.gui()
        self.mw.mainloop()
    def gui(self):
        bg = PhotoImage(file='/usr/lib/Joker3/bg1.png')
        self.bg_label = Label(self.mw,
                              image = bg)
        self.bg_label.image = bg
        self.bg_label.place(relx = 0, rely = 0)
        self.head = Label(self.mw,
                          text = "XanderPoker",
                          font = ("TlwgTypist", 25, 'bold italic'),
                          bg = 'green',
                          fg = 'cyan')
        self.head.pack(pady = 4)
        self.main_frame = Frame(self.mw)
        self.main_frame.place(relx = 0.45, rely = 0.6)
        self.server = Button(self.main_frame,
                          text = 'Server',
                          font = ('Times', 17, 'italic'),
                          fg = 'red',
                          bd = 5,
                          relief = 'ridge',
                          bg = 'black',
                          activeforeground = 'green',
                          command = self.server_but,
                          cursor = 'hand2')
        self.server.pack(fill = X)
        self.client = Button(self.main_frame,
                          text='Client',
                          font=('Times', 17, 'italic'),
                          fg='red',
                          bd=5,
                          relief='ridge',
                          bg='black',
                          activeforeground='green',
                          command=self.client_but,
                          cursor='hand2')
        self.client.pack(fill=X)
        self.instruct = Button(self.main_frame,
                          text='Instructions',
                          font=('Times', 17, 'italic'),
                          fg='red',
                               bd = 5,
                               relief = 'ridge',
                               bg = 'black',
                               activeforeground = 'green',
                               command = self.instruct_func,
                               cursor = 'hand2')
        self.instruct.pack(fill = X)
        self.exit = Button(self.main_frame,
                          text='Quit',
                          font=('Times', 17, 'italic'),
                          fg='red',
                           bd = 5,
                           relief = 'ridge',
                           bg = 'black',
                           activeforeground = 'green',
                           command = self.mw.destroy,
                           cursor = 'hand2')
        self.exit.pack(fill = X)
        self.credit = Button(self.main_frame,
                           text='Credits',
                           font=('Times', 17, 'italic'),
                           fg='red',
                           bd=5,
                           relief='ridge',
                           bg='black',
                           activeforeground='green',
                           command=self.credit_func,
                           cursor='hand2')
        self.credit.pack(fill=X)
    def server_but(self):
        Thread(target=subprocess.call, args = [['python3', '/usr/lib/Joker3/poker_gui.py']]).start()
    def client_but(self):
        Thread(target=subprocess.call, args = [['python3', '/usr/lib/Joker3/poker2.py']]).start()
    def instruct_func(self):
        Thread(target=subprocess.call, args = [['firefox', '/usr/lib/Joker3/html_source/instructions.html']]).start()
    def credit_func(self):
        Thread(target=self.credits).start()
    def credits(self):
        self.credit_window = Toplevel()
        self.credit_window.title('XanderSiva')
        self.credit_window['bg'] = 'lightgreen'
        img = PhotoImage(file='/usr/lib/Joker3/icon1.png')
        print(img)
        self.label = Label(self.credit_window,
                           image=img)
        self.label.pack()
        self.label.image = img
        self.lab2 = Label(self.credit_window,
                          text='XanderPoker',
                          fg='white',
                          bg='lightgreen',
                          font=('TlwgTypist', 14, 'bold'))
        self.lab2.pack()
        self.b_frame = Frame(self.credit_window)
        self.b_frame.pack()
        self.lab3 = Label(self.b_frame,
                          text='CreatedBy:',
                          fg='black',
                          bg='lightgreen',
                          font=('TlwgTypist', 14, 'bold'))
        self.lab3.pack(side=LEFT)
        self.lab4 = Label(self.b_frame,
                          text='SivaPrasad.C',
                          fg='black',
                          bg='lightgreen',
                          font=('Times', 14, 'italic'))
        self.lab4.pack(side=LEFT)
        self.lab5 = Label(self.b_frame,
                          text='(R170262)',
                          fg='black',
                          bg='lightgreen',
                          font=('Times', 14, 'italic'))
        self.lab5.pack(side=LEFT)
        self.credit_window.bind("<Enter>", self.anim1)
        self.credit_window.bind("<Leave>", self.leave)
    def anim1(self, *args):
        self.lab4['font'] = ('TlwgTypist', 14, 'bold italic')
        self.lab4['fg'] = 'blue'
        self.lab5['font'] = ('TlwgTypist', 14, 'bold italic')
        self.lab5['fg'] = 'blue'
    def leave(self, *args):
        self.lab4['font'] = self.lab5['font'] = ('Times', 14, 'italic')
        self.lab4['fg'] = self.lab5['fg'] = 'black'
if __name__ == "__main__":
    obj = Menu()
