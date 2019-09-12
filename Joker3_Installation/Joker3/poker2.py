# 192.168.0.8
from tkinter import *
from tkinter import simpledialog, PhotoImage
import socket
from threading import *
from logging import *
class Poker_Gui(Thread, Logger):
    def __init__(self):
        self.permit = 0
        self.flag = 0
        self.head_k = 0
        Thread.__init__(self)
        Logger.__init__(self, name='Xogger')
        with open("debug.log", 'w') as file:
            pass
        self.permit = 0
        self.setLevel(DEBUG)
        self.file_handler = FileHandler(filename="debug.log")
        self.file_handler.setLevel(DEBUG)
        self.formatter = Formatter("%(message)s")
        self.file_handler.setFormatter(self.formatter)
        self.addHandler(self.file_handler)
        self.trash = []
        self.win = Tk()
        self.win.config(bg='lightgreen')
        self.debug("Window created successfully.")
        self.bgc = PhotoImage(
            file='/usr/lib/Joker3/NewImages/b.png')  # bgc stands for back ground of card
        self.ggc = PhotoImage(file='/usr/lib/Joker3/NewImages/g.png')
        self.debug("Background images photoimages are created.")
        self.gui() # This list conatins the thirteen buttons
        print("Flow of execution")
        self.win.mainloop()
    def gui(self):
        '''This method is contains the structure of the graphical user interface.'''
        self.debug("_"*50 + "GUI" + "_"*50)
        self.window = Toplevel()
        self.window.title('Xander Poker')
        self.window.config(bg='black')
        label = Label(self.window,
                      text='Enter your address:-',
                      bg='black',
                      fg='white',
                      font=('TlwgTypist', 13, 'bold'))
        label.pack()
        self.entry = Entry(self.window,
                           font=('TlwgTypist', 13),
                           bg='white',
                           fg='black')
        self.entry.pack()
        self.entry.focus()
        frame = Frame(self.window,
                      bg='black')
        frame.pack(pady=3)
        ok = Button(frame,
                    text='OK',
                    fg='white',
                    bg='black',
                    font=('TlwgTypist', 13, 'bold'),
                    command=self.ok_func)
        ok.pack(side=LEFT, padx=10)
        cancel = Button(frame,
                        text='Cancel',
                        fg='white',
                        bg='black',
                        font=('TlwgTypist', 13, 'bold'),
                        command=self.cancel_func)
        cancel.pack(side=LEFT)
        self.window.mainloop()
        self.win.attributes('-fullscreen', 'true')
        self.debug("Ipv4 address is taken {}.".format(self.ip))
        self.debug("self.socket method is going to be executed next")
        try:
            self.socket()
        except:
            print("entered")
            error_label = Label(self.win,
                                text='Network Error',
                                bg='lightgreen',
                                fg='red',
                                font=('TlwgTypist', 20, 'italic'))
            error_label.pack()
            steps = Label(self.win,
                          text='1.Check whether you if the server started or not.\n2.Try disconnecting and reconnecting to the network.\n3.Wait for sometime for the Server to Refresh.\n4.Check whether you entered correct IP address or not and try again.',
                          bg='lightgreen',
                          fg='black',
                          font=('Times', 13, 'italic'))
            steps.pack()
            quit = Button(self.win,
                          text='Quit',
                          bg='black',
                          fg='lightgreen',
                          font=('Times', 13, 'italic'),
                          command=self.win.destroy)
            quit.pack()
            return None
        self.heading = Label(self.win,
                             text = 'Start the Game',
                             font = ('URWGothic', 30, 'italic'),
                             bg = 'lightgreen',
                             fg = 'black',
                             cursor = 'hand1')
        self.debug("Heading 'Start the Game' is created and command set to self.receiving.")
        self.heading.pack(side = TOP)
        self.heading.bind('<Button-1>', self.head_func)
        self.heading.bind('<Enter>', self.head_enter)
        self.heading.bind('<Leave>', self.head_leave)
        # We have to create 13 buttons for 13 cards
        # First we will create a frame that contain thirteen cards and use grid layout to manage cards in the gui
        self.m_frame = Frame(self.win)  # This is the main frame we are talking about earlier
        self.m_frame.config(background='lightgreen')
        self.m_frame.pack(side='left', anchor=SW)
        self.debug("A main frame is created for the 13 cards.")
        # We just declared the buttons so that we can use them in loop
        self.b0 = Button(self.m_frame)
        self.b0.grid(row=0, column=0)
        self.b1 = Button(self.m_frame)
        self.b1.grid(row=1, column=0)
        self.b2 = Button(self.m_frame)
        self.b2.grid(row=2, column=0)
        self.b3 = Button(self.m_frame)
        self.b3.grid(row=0, column=1)
        self.b4 = Button(self.m_frame)
        self.b4.grid(row=1, column=1)
        self.b5 = Button(self.m_frame)
        self.b5.grid(row=2, column=1)
        self.b6 = Button(self.m_frame)
        self.b6.grid(row=0, column=2)
        self.b7 = Button(self.m_frame)
        self.b7.grid(row=1, column=2)
        self.b8 = Button(self.m_frame)
        self.b8.grid(row=2, column=2)
        self.b9 = Button(self.m_frame)
        self.b9.grid(row=0, column=3)
        self.b10 = Button(self.m_frame)
        self.b10.grid(row=1, column=3)
        self.b11 = Button(self.m_frame)
        self.b11.grid(row=2, column=3)
        self.b12 = Button(self.m_frame)
        self.b12.grid(row=1, column=4)
        self.debug("All the 13 buttons are created in the main frame.")
        self.main_list = [self.b0, self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8, self.b9,
                          self.b10, self.b11, self.b12]
        self.debug("Created a mainlist in which the buttons are appended {}".format(self.main_list))
        self.debug("P2 deck sorter method going to be executed next.")
        self.p2_deck.sort()
        for x in range(13):
            file = PhotoImage(file='/usr/lib/Joker3/NewImages/{}.png'.format(self.p2_deck[x]))
            self.main_list[x]['image'] = file
            self.main_list[x].image = file
            self.main_list[x]['bg'] = 'black'
            self.main_list[x]['bd'] = 8
            self.main_list[x]['relief'] = 'ridge'
            self.main_list[x]['activebackground'] = 'red'
            self.debug("{} >>> {}".format(str(self.main_list[x]), file.__repr__()))
        self.debug("Dealer's frame method is going to be executed next.")
        self.dealers_frame()
        self.debug("Waiting for the card.")
        self.current_card = self.xan.recv(1024)
        self.current_card = self.current_card.decode()
        self.debug("Received the card ***{}***".format(self.current_card))
        self.c_file = PhotoImage(file='/usr/lib/Joker3/NewImages/{}.png'.format(self.current_card))
        self.cur_but['image'] = self.ggc
        self.cur_but.image = self.ggc
        self.deck_but['image'] = self.bgc
        self.deck_but.image = self.bgc
        self.debug("The images of the current button and deck_button are set to the background images.")
        self.other_cd['image'] = self.c_file        # Trash cards is in this button
        self.debug("The image of the other card is set to the current card.")
        self.debug("_"*50 + "End GUI" + "_"*50)
    def head_enter(self, *args):
        self.heading['fg'] = 'red'
        self.heading['font'] = ('URWGothic', 30, 'bold italic')
    def head_leave(self, *args):
        self.heading['fg'] = 'black'
        self.heading['font'] = ('URWGothic', 30, 'italic')
    def heading_animation(self):
        txt = 'xanderpoker'
        text = txt[:self.head_k] + txt[self.head_k].upper() + txt[self.head_k + 1:11]
        self.heading['text'] = text
        self.head_k += 1
        if self.head_k == 10:
            self.head_k = 0
        self.heading.after(250, self.heading_animation)
    def thread_start(self):
        self.debug("+"*50 + "Start thread start" + "+"*50)
        self.debug("Started the thread.")
        self.t1 = Thread(target=self.receiving)
        self.t1.start()
        self.debug("+" * 50 + "End thread start" + "+" * 50)
    def heading_Start(self):
        if self.flag == 0:
            self.heading['text'] = 'Xanderpoker'
            self.heading_animation()
            self.flag += 1
    def head_func(self, *args):
        self.heading_Start()
        self.heading.unbind('<Button-1>')
        self.heading.unbind('<Enter>')
        self.heading.unbind('<Leave>')
        self.head_leave()
        self.win.after(300, self.receiving)
    def receiving(self  ):
        self.debug("$"*50 + "Started Receiving" + "$"*50)
        self.four_but['command'] = self.four_sub
        print("Waiting for the card.")
        self.debug("Waiting for the card.")
        self.message = self.xan.recv(1024)
        self.current_card = self.xan.recv(1024)
        self.deck_card =self.xan.recv(1024)
        self.message = self.message.decode()
        self.current_card = self.current_card.decode()
        self.deck_card = self.deck_card.decode()
        self.debug("Successfully Received.\nMessage:{}\nCurrent Card:{}\nDeck Card:{}".format(self.message, self.current_card, self.deck_card))
        if self.message == 'SHOW':
            self.lose()
        img = PhotoImage(file='/usr/lib/Joker3/NewImages/{}.png'.format(self.current_card))
        self.cur_but['image'] = img
        self.cur_but.image = img
        self.mes_label['text'] = self.message
        self.debug("The image of the current button is set to {}".format(img.__repr__()))
        self.debug("The funcition initial is going to be executed next.")
        self.initial()
        self.show['command'] = self.show_func
        self.debug("$"*50 + "End of receiving method" + "$" * 50)
    def socket(self):
        self.debug(">"*50 + "Start socket() method" + "<"*50)
        self.xan = socket.socket()
        self.debug("Successfully created a socket:{}".format(self.xan.__repr__()))
        self.xan.connect((self.ip, 8000))
        self.debug("Connection established successfully.")
        self.p2_deck_en = self.xan.recv(1024)
        self.debug("Successfully received Encyrpted deck of p2::{}".format(self.p2_deck_en.decode()))
        self.p2_deck = (self.p2_deck_en.decode()).split()
        self.debug("P2 deck after decryption:{}".format(self.p2_deck))
        self.joker = self.xan.recv(1024)
        self.joker = self.joker.decode()
        self.debug("Joker:{}".format(self.joker))
        self.debug(">" * 50 + "Ended socket() method" + "<" * 50)
    def dealers_frame(self):
        '''This functions contains the dealers' desk Gui Programming.'''
        self.debug("*"*50 + "Started Dealer's Frame" + "*"*50)
        self.d_frame = Frame(self.win,
                             background = 'lightgreen',
                             bd = 2,
                             relief = 'ridge')
        self.d_frame.place(relx=0.67, rely=0.08)
        self.debug("D_Frame or the dealer's frame is created.")
        self.t_frame = Frame(self.d_frame, background = 'lightgreen')  # Creating a top frame in dealers frame to get correct symmetry
        self.t_frame.pack(pady=30)
        self.debug("Created another top frame for the current button, deck buttons")
        self.title = Label(self.t_frame,
                           text=" Dealer's Desk ",
                           bd = 5,
                           relief = 'ridge',
                           font=('TlwgTypist', 15, 'bold'),
                           bg = 'lightgreen')
        self.title.pack()  # Packing the title dealer's desk
        self.debug("Labelling is done for the dealer's frame.")
        self.c_frame = Frame(self.d_frame, background = 'lightgreen')  # This is center frame which contains the cards
        self.c_frame.pack()
        self.debug("A center frame is created a as child frame of the dealer's frame.")
        self.cur_but = Button(self.c_frame,
                              bg = 'lightblue',
                              activebackground = 'black',
                              command=self.curr_card_func)  # curr_but means current button
        self.cur_but.pack(side=LEFT, padx=10)
        self.debug("Current Button is created in the dealer's frame")
        self.deck_frame = Frame(self.c_frame, background = 'lightgreen')
        self.deck_frame.pack(side=RIGHT, padx=5)
        self.debug("Created another frame deck frame for all the deck buttons.")
        self.deck_but = Button(self.c_frame,
                                bg = 'lightblue',
                               activebackground = 'black',
                               command=self.deck_but_func)  # It is the deck button
        self.deck_but.pack(padx=10)
        self.debug("Deck button is created in the center frame.")
        self.deck_but2 = Button(self.deck_frame,
                                text='Deck',
                                font=('Times', 11, 'bold italic'),
                                fg = 'red',
                                bg = 'lightblue',
                                activebackground = 'lightgreen',
                                command=self.deck2_but_func)
        self.deck_but2.pack()
        self.debug("Deck 2 button is created in the deck frame.")
        self.throw = Button(self.deck_frame,
                            text='Throw',
                            font=('Times', 11, 'bold italic'),
                            fg='red',
                            bg='lightblue',
                            activebackground = 'lightgreen',
                            command=self.throw_func)
        self.throw.pack()
        self.debug("Throw button is also created successfully.")
        self.b_frame = Frame(self.d_frame, background = 'lightgreen')  # This is the bottom frame of the dealer's frame
        self.b_frame.pack(pady=30)
        self.debug("Created a bottom frame and not going to be debbuged now frame.")
        self.four_but = Button(self.b_frame,
                               text='FOUR SET',
                               font=('Times', 11, 'bold italic'),
                               fg = 'green',
                               bg = 'lightblue',
                               activebackground = 'lightgreen',
                               command = self.four_sub)  # This is the four set asking button
        self.four_but.pack()
        self.show = Button(self.b_frame,
                           text='SHOW',
                           font=('Times', 11, 'bold italic'),
                           fg='green',
                           bg='lightblue',
                           command = self.show_func)  # This is the show button
        self.show.pack()
        self.other_cd = Button(self.b_frame, bg='lightgreen',
                               activebackground='black')  # This button shows the other card of player
        self.other_cd.pack()
        self.debug("The card which displays the transmission cards will be going in the other_cd button.")
        self.other_cd['image'] = self.ggc
        self.other_cd.image = self.ggc
        self.debug("The background image of the other card is set to green background.")
        self.mes_label = Label(self.b_frame,
                               text='Message',
                               font=('Times', 15, 'italic'),
                               fg='red',
                               bg='lightgreen')  # This is the message label
        self.mes_label.pack()
        self.quit_label = Button(self.b_frame,
                                 text='Quit',
                                 font=('Times', 15, 'italic'),
                                 fg='black',
                                 bg='lightblue',
                                 activebackground='lightgreen',
                                 command=self.win.destroy)
        self.quit_label.pack()
        self.debug("This is the message frame that displays whether the other player took or not took the card.")
        self.debug("*" * 50 + "Started Dealer's Frame" + "*" * 50)
    def curr_card_func(self):
        '''This function is the function related to the current card button'''
        self.debug("&"*50 + "Current Card Function" + "&"*50)
        self.show['command'] = ''
        self.debug("Show function set to none")
        print(self.p2_deck)
        self.p2_deck.append(self.current_card)
        print(self.p2_deck)
        self.throw['command'] = self.deck_but['command'] = self.deck_but2['command'] = self.show['command'] = ''
        self.message = 'Player 2 took the card.'
        if self.permit == 1:
            self.four_but['command'] = self.four_but
            self.message += "Joker Revealed."
        else:
            self.four_but['command'] = ''
        # We are gonna assign the functions of the 13 cards here
        self.cur_but['image'] = self.bgc
        self.cur_but.image = self.bgc
        self.cur_but['command'] = ''
        self.button_funcs()
        self.debug("&" * 50 + "Current Card Function" + "&" * 50)
    def deck2_but_func(self):
        '''This function is going to be binded with the deck button of the dealers desk deck.'''
        self.debug("<"*50 + "Deck 2 Button" + ">"*50)
        self.show['command'] = ''
        self.debug("Show command set to none.")
        self.trash.append(self.current_card)
        self.message = 'Player 2 goes for the deck'
        self.debug("Trash:{}\nLength{}".format(self.trash, len(self.trash)))
        self.current_card = self.deck_card
        self.debug("Current_card:{} is set to deck_card:{}".format(self.current_card, self.deck_card))
        img = PhotoImage(file='/usr/lib/Joker3/NewImages/{}.png'.format(self.current_card))
        self.deck_but['image'] = img
        self.deck_but.image = img
        self.debug("The image of deck button is set to {}".format(img.__repr__()))
        self.deck_but2['command'] = self.show['command'] = ''
        self.debug("The commands of deck_but2, four_but, show are set to ***None*** ")
        if self.permit == 1:
            self.four_but['command'] = self.four_but
            self.message += "Joker Revealed."
        else:
            self.four_but['command'] = ''
        self.deck_but['command'] = self.deck_but_func
        self.debug("The command of self.deck_but is set to self.deck_but_function.")
        self.throw['command'] = self.throw_func
        self.debug("The command of the throw button is set to throw function.")
        self.cur_but['image'] = self.bgc
        self.cur_but.image = self.bgc
        self.debug("The bg of current button is back ground.")
        self.cur_but['command'] = ''
        self.debug("The command of current button is set to ***None***")
        self.debug("<"*50 + "Deck 2 Button" + ">"*50)
    def deck_but_func(self):
        '''This function contains the functions that are to be done by the deck_button'''
        self.debug("["*50 + "DeckButtonFunction" + "]"*50)
        self.p2_deck.append(self.current_card)
        self.debug("Current_card:{}".format(self.current_card))
        self.debug("P2_deck:{}\nLength:{}".format(self.p2_deck, len(self.p2_deck)))
        self.throw['command'] = self.deck_but['command'] = self.deck_but2['command'] = self.four_but['command'] = \
        self.show['command'] = ''
        self.debug("The commands of throw, deck_but, deck_but2, four_but,show are set to ***None***")
        # This is where the 13 buttons will be get activated
        self.deck_but['image'] = self.bgc
        self.deck_but.image = self.bgc
        self.debug("The deck_but is set to image.")
        self.deck_but['command'] = ''
        self.debug("Command of deck_but to ***None***")
        self.debug("button_funcs is going to be executed which activates all the buttons.")
        self.button_funcs()
        self.debug("[" * 50 + "DeckButtonFunction" + "]" * 50)
    def throw_func(self):
        '''This function will be binded to the throw button of the dealer's desk'''
        self.debug("#"*50 + "Throw Function" + "#"*50)
        self.deck_but['command'] = self.deck_but2['command'] = self.four_but['command'] = self.show['command'] = ''
        self.debug("The commands of deck_but,deck_but2,four_but,show are set to ***None***")
        self.out_card = self.current_card
        self.debug("Out card:{} is set to current card:{}".format(self.out_card, self.current_card))
        self.deck_but['image'] = self.bgc
        self.deck_but.image = self.bgc
        self.debug("Message is set to::{}".format(self.message))
        self.deck_but['command'] = ''
        img = PhotoImage(file='/usr/lib/Joker3/NewImages/{}.png'.format(self.out_card))
        self.other_cd['image'] = img
        self.other_cd.image = img
        self.debug("Image of other card is set to {}".format(img.__repr__()))
        self.xan.send(self.message.encode())
        self.debug("Message is sent successfully.")
        self.xan.send(self.out_card.encode())
        self.debug("Out_card is sent successfully.")
        self.throw['command'] = ''
        self.debug("Throw command is set to ***None***")
        self.debug("Thread_start is going to be executed.")
        self.thread_start()
        self.debug("#"*50 + "End Throw Function" + "#"*50)
    def card012(self, ind):
        '''This function will be binded to all the 13 cards in the Graphical User Interface'''
        self.debug("!"*50 + "Card 0-12 Function" + "!"*50)
        self.out_card = self.p2_deck[ind]
        self.debug("Out_card:{}".format(self.out_card))
        self.debug("P2 deck:{}".format(self.p2_deck))
        self.debug("Index:{}, Card:{}".format(ind, self.p2_deck[ind]))
        self.p2_deck.pop(ind)
        self.debug("P2 deck:{}".format(self.p2_deck))
        self.p2_deck.sort()
        self.debug("P2 deck:{}".format(self.p2_deck))
        self.debug("Message:{}".format(self.message))
        for x in range(13):
            file = PhotoImage(file='/usr/lib/Joker3/NewImages/{}.png'.format(self.p2_deck[x]))
            self.main_list[x]['image'] = file
            self.main_list[x].image = file
            self.debug("{} >>> {}".format(str(self.main_list[x]), file.__repr__()))
        self.debug("Now p2_deck:{}\nLength{}".format(self.p2_deck, len(self.p2_deck)))
        img = PhotoImage(file='/usr/lib/Joker3/NewImages/{}.png'.format(self.out_card))
        self.other_cd['image'] = img
        self.other_cd.image = img
        self.debug("The image of other card is set to {}".format(img.__repr__()))
        self.xan.send(self.message.encode())
        self.xan.send(self.out_card.encode())
        self.debug("Message and out_card successfully sent.")
        self.debug("Thread_start function is started successully.")
        self.thread_start()
        self.button_over()
        self.debug("!" * 50 + "End Card 0-12 Function" + "!" * 50)
    def button_funcs(self):
        self.debug("{" * 50 + "Button_Function" + "}"*50)
        self.b0['command'] = lambda: self.card012(0)
        self.b1['command'] = lambda: self.card012(1)
        self.b2['command'] = lambda: self.card012(2)
        self.b3['command'] = lambda: self.card012(3)
        self.b4['command'] = lambda: self.card012(4)
        self.b5['command'] = lambda: self.card012(5)
        self.b6['command'] = lambda: self.card012(6)
        self.b7['command'] = lambda: self.card012(7)
        self.b8['command'] = lambda: self.card012(8)
        self.b9['command'] = lambda: self.card012(9)
        self.b10['command'] = lambda: self.card012(10)
        self.b11['command'] = lambda: self.card012(11)
        self.b12['command'] = lambda: self.card012(12)
        self.debug("All the functions are set to appropriate functions.")
        self.debug("{" * 50 + "End Button_Function" + "}" * 50)
    def initial(self):
        self.debug("@"*50 + "Initial" + "@"*50)
        self.cur_but['command'] = self.curr_card_func
        self.debug("Current Button command is set to curr_card_func")
        self.deck_but2['command'] = self.deck2_but_func
        self.debug("deck_but command set to deck2_but_func")
        self.deck_but['command'] = ''
        self.throw['command'] = ''
        self.four_but['command'] = self.four_sub
        self.show['command'] = ''
        self.debug("Deck_But, four_but and show function is set to ***None***")
        self.debug("Button_over Function is going to be executed next.")
        self.button_over()
        self.debug("@" * 50 + "Initial" + "@" * 50)
    def button_over(self):
        self.debug("-" *50 + "Button_Over" + "-"*50)
        for x in self.main_list:
            x['command'] = ''
        self.debug('All the 13 button commands are set to ***None***')
        self.debug("-" * 50 + "Button_Over" + "-" * 50)
    def four_sub(self):
        self.debug("|"*50 + "Four Button" + "|" * 50)
        self.z_list = [x[0] for x in self.p2_deck]
        self.dict = {x:self.z_list.count(x) for x in self.z_list}
        self.debug("Z_list:{}".format(self.z_list))
        self.debug("Dictionary:{}".format(self.dict))
        self.vals = self.dict.values()
        self.m = max(self.vals)
        self.debug("Max:{}".format(self.m))
        joker_wind = Toplevel()
        joker_wind.title("***JOKER***")
        but = Button(joker_wind)
        but.pack()
        ok = Button(joker_wind,
                    text = 'OK',
                    bg = 'black',
                    fg = 'lightgreen',
                    font = ('TlwgTypist', 12, 'bold'),
                    command = joker_wind.destroy)
        ok.pack(fill = X)
        if self.m == 4:
            img = PhotoImage(file = '/usr/lib/Joker3/NewImages/{}.png'.format(self.joker))
            but['image'] = img
            but.image = img
            self.debug("Maximum value is four")
            self.permit = 1
        else:
            but['text'] = 'You did not complete the fourth set yet.'
            self.debug("Maximum Value is not 4.")
        self.debug("|" * 50 + "End Four Button" + "|" * 50)
    def show_func(self):
        self.debug("X"*50 + "SHOW" + "X"*50)
        self.z_list = [x[0] for x in self.p2_deck]
        self.dict = {x: self.z_list.count(x) for x in self.z_list}
        self.vals = self.dict.values()
        self.m = max(self.vals)
        if self.m == 4:
            self.debug("Entered the show and true.")
            self.g_dict = {}
            self.n_jokers = 0
            for k in self.dict:
                if k != self.joker[0] and self.dict[k] != 4 and k != 'J':
                    self.g_dict[k] = self.dict[k]
                    self.debug("Condition true.")
                    self.debug("{}>>>{}".format(k, self.dict[k]))
                elif self.dict[k] != 4:
                    self.n_jokers += self.dict[k]
                    self.debug("COndition False.")
                    self.debug("{}>>>{}".format(k, self.dict[k]))
                    self.debug("JOKERS:{}".format(self.n_jokers))
            vals = list(self.g_dict.values())
            self.debug("Values:{}".format(vals))
            r_jokers = 0
            for j in vals:
                r_jokers += (3 - j)
                self.debug("{}>>>{}".format(j, (3 - j)))
            if r_jokers == self.n_jokers or r_jokers == 0:
                self.debug("You Are The Winner.")
                self.mess = self.cur_card = "SHOW"
                self.xan.send(self.mess.encode())
                self.debug("{} is sent.".format(self.mess))
                self.xan.send(self.mess.encode())
                self.debug("{} is sent".format(self.cur_card))
                self.toplevel = Toplevel()
                bg_img = PhotoImage(file = 'joker1.png')
                bg = Label(self.toplevel,
                           img = bg_img)
                bg.place(relx = 0, rely = 0)
                bg.image = bg_img
                self.label = Label(self.toplevel,
                                   text = "You Are the Winner.",
                                   font = ("TlwgTypist", 20, 'bold'),
                                   bd = 4,
                                   relief = "groove")
                self.label.pack()
                self.win.after(1000, self.win.destroy)
            else:
                self.debug("You are not the winner.")
                self.toplevel = Toplevel()
                self.label = Label(self.toplevel,
                                   text="NOT YET.",
                                   font=("TlwgTypist", 20, 'bold'),
                                   bd=4,
                                   relief="groove")
                self.label.pack()
    def lose(self):
        self.debug("x"*50 + "LOSE" + "x" * 50)
        lose_wind = Toplevel()
        bg_img = PhotoImage(file = '/usr/lib/Joker3/joker1.png')
        bg = Label(lose_wind,
                   image = bg_img)
        bg.place(relx = 0.1, rely = 0.1)
        bg.image = bg_img
        label = Label(lose_wind,
                      text = "GAME-OVER\nYou Lose",
                      font = ("TlwgTypist", 15, 'bold'))
        label.pack()
        self.win.after(1000, self.win.destroy)
        self.debug("x" * 50 + "END LOSE" + "x" * 50)
    def ok_func(self):
        self.ip = self.entry.get()
        self.window.quit()
        self.window.destroy()
    def cancel_func(self):
        self.window.quit()
        self.window.destroy()
obj = Poker_Gui()