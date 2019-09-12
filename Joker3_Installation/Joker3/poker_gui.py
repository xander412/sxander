from tkinter import *
import time
from threading import *
import socket
import random
from logging import *
# 10.31.119.228 
class Poker(Thread, Logger):
    def __init__(self):
        '''There must be time sleep in server because it will send two cards current_card an'''
        self.head_k = 0
        self.ip = ''
        Thread.__init__(self)
        Logger.__init__(self, name='Xogger')
        with open('debug.log', 'w') as file:
            pass
        self.permit = 0
        self.setLevel(DEBUG)
        self.file_handler = FileHandler(filename="debug.log")
        self.file_handler.setLevel(DEBUG)
        self.formatter = Formatter("%(message)s")
        self.file_handler.setFormatter(self.formatter)
        self.addHandler(self.file_handler)
        self.trash = []
        self.debug("Trash created successfully {} and length is {}".format(self.trash, len(self.trash)))
        self.deck_creater()  # Creating the deck
        self.deck_divider()
        self.p2_deck_encrypter()
        self.joker_picker()
        self.win = Tk()
        self.debug("Window is created now.")
        self.win.title('Xanderpoker')
        self.win.config(bg='lightgreen')
        self.bgc = PhotoImage(file='/usr/lib/Joker3/NewImages/b.png')  # bgc stands for back ground of card
        self.ggc = PhotoImage(file='/usr/lib/Joker3/NewImages/g.png')
        self.debug("Background images created and converted to photoimages.")
        self.gui()
        self.win.mainloop()
    def thread(self):
        self.debug("-" * 50 + "Starting self.thread" + "-" * 50)
        self.n_thread = Thread(target=self.thread_func)
        self.n_thread.start()
        self.debug("-" * 50 + "End of self.thread" + "-" * 50)
    def thread_func(self):
        self.debug("_" * 50 + "Started Thread Function" + "_" * 50)
        self.four_but['command'] = self.four_set_but
        self.debug("Four Button is activated.")
        self.message = self.conn.recv(1024).decode()
        self.debug("The message is {} received.".format(self.message))
        self.current_card = self.conn.recv(1024).decode()
        self.debug("Current card {} is received.".format(self.current_card))
        if self.message == 'SHOW':
            self.lose()
        img = PhotoImage(file='/usr/lib/Joker3/NewImages/{}.png'.format(self.current_card))
        self.debug("Photoimage successfully created.{}".format(img.__repr__()))
        self.cur_but['image'] = img
        self.cur_but.image = img
        self.mes_label['text'] = self.message
        self.debug("Current Button image is changed to photoimage.")
        if 'deck' in self.message:
            self.debug("Deck is in the message.That means p2 gone for the deck.")
            self.deck.pop(0)
            self.debug("Deck after p2 taking the deck card{}\nand Length is {}".format(self.deck, len(self.deck)))
        self.debug("Executing Initial Function")
        self.initial()
        self.show['command'] = self.show_func
        self.debug("_" * 50 + "Ended Thread Function" + "_" * 50)
    def gui(self):
        '''This method is contains the structure of the graphical user interface.'''
        self.debug("*" * 50 + "Started GUI" + "*" * 50)
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
                        font=('Tlwg   Typist', 13, 'bold'),
                        command=self.cancel_func)
        cancel.pack(side=LEFT)
        self.window.mainloop()
        self.debug("Ip is taken successfully IP = {}".format(self.ip))
        self.win.attributes('-fullscreen', 'true')
        self.heading = Label(self.win,
                             text='XanderPoker',
                             bg='lightgreen',
                             fg='black',
                             font=('URWGothic', 30, 'italic'))
        self.heading.pack(pady=5)
        self.heading_animation()
        try:
            self.socket()
        except:
            print("entered")
            error_label = Label(self.win,
                                text = 'Network Error',
                                bg='lightgreen',
                                fg='red',
                                font=('TlwgTypist', 20, 'italic'))
            error_label.pack()
            steps = Label(self.win,
                          text = '1.Check whether you are connected to the network correctly.\n2.Try disconnecting and reconnecting to the network.\n3.Wait for sometime for the Server to Refresh.\n4.Check whether you entered correct IP address or not and try again.',
                          bg='lightgreen',
                          fg='black',
                          font = ('Times', 13, 'italic'))
            steps.pack()
            quit = Button(self.win,
                          text = 'Quit',
                          bg='black',
                          fg='lightgreen',
                          font = ('Times', 13, 'italic'),
                          command = self.win.destroy)
            quit.pack()
            return None
        # We have to create 13 buttons for 13 cards
        # First we will create a frame that contain thirteen cards and use grid layout to manage cards in the gui
        self.m_frame = Frame(self.win)# This is the main frame we are talking about earlier
        self.m_frame.config(background='lightgreen')
        self.m_frame.pack(side = 'left', anchor = SW)
        self.debug("Main frame is created to left and anchored to South West.")
        # We just declared the buttons so that we can use them in loop
        self.b0 = Button(self.m_frame)
        self.b0.grid(row = 0, column = 0)
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
        self.debug("All the buttons are successfully created from 1 to 13.")
        self.main_list = [self.b0, self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8, self.b9, self.b10 ,self.b11, self.b12]
        self.debug("Main list is created and all the buttons are appended to the main list::\n{}".format(self.main_list))
        self.debug("P2 deck sorter function is going to be executed now.")
        self.p1_deck.sort()
        self.debug("A for loop is going to be executed so that all the buttons in the mainlist gets their appropriate images.")
        for x in range(13):
            file = PhotoImage(file='/usr/lib/Joker3/NewImages/{}.png'.format(self.p1_deck[x]))
            self.main_list[x]['image'] = file
            self.main_list[x].image = file
            self.main_list[x]['bg'] = 'black'
            self.main_list[x]['bd'] = 8
            self.main_list[x]['relief'] = 'ridge'
            self.main_list[x]['activebackground'] = 'red'
            self.debug("{} >>> {}".format(str(self.main_list[x]), file.__repr__()))
        self.debug("Dealer's Frame is going to be executed next.")
        self.dealers_frame()
        self.current_card = self.deck[0]
        self.debug("Current is set to the zeroth card in the deck.\nCurrent Card:-{}\nDeck:{}".format(self.current_card, self.deck))
        self.deck.pop(0)
        self.debug("After the popping the zeroth card:{}".format(self.deck))
        self.debug("Going to sleep for 4 seconds.")
        time.sleep(4)
        self.conn.send(self.current_card.encode())
        self.debug("Current card is sent {}".format(self.current_card))
        self.c_file = PhotoImage(file='/usr/lib/Joker3/NewImages/{}.png'.format(self.current_card))
        self.cur_but['image'] = self.c_file
        self.cur_but.image = self.c_file
        self.debug("The image of the current button is {}".format(self.c_file.__repr__()))
        self.deck_but['image'] = self.bgc
        self.deck_but.image = self.bgc
        self.debug("The image of the deck_button if changed to the background.")
        self.debug("*"*50 + "End of the GUI method" + "*"*50)
    def heading_animation(self):
        txt = 'xanderpoker'
        text = txt[:self.head_k] + txt[self.head_k].upper() + txt[self.head_k + 1:11]
        self.heading['text'] = text
        self.head_k += 1
        if self.head_k == 10:
            self.head_k = 0
        self.heading.after(250, self.heading_animation)
    def dealers_frame(self):
        '''This functions contains the dealers' desk Gui Programming.'''
        self.debug("&"*50 + "Dealers Frame" + "&"*50)
        self.d_frame = Frame(self.win,
                             background = 'lightgreen',
                             bd = 2,
                             relief = 'ridge')
        self.d_frame.place(relx=0.67, rely=0.08)
        self.debug("D_Frame or the dealer's frame is created.")
        self.t_frame = Frame(self.d_frame,
                             background='lightgreen')  # Creating a top frame in dealers frame to get correct symmetry
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
                              command = self.curr_card_func)  # curr_but means current button
        self.cur_but.pack(side=LEFT, padx=10)
        self.debug("Current Button is created in the dealer's frame")
        self.deck_frame = Frame(self.c_frame, background='lightgreen')
        self.deck_frame.pack(side=RIGHT, padx=5)
        self.debug("Created another frame deck frame for all the deck buttons.")
        self.deck_but = Button(self.c_frame,
                                bg = 'lightblue',
                               activebackground = 'black',
                               command = self.deck_but_func)  # It is the deck button
        self.deck_but.pack(padx=10)
        self.debug("Deck button is created in the center frame.")
        self.deck_but2 = Button(self.deck_frame,
                                text='Deck',
                                font=('Times', 11, 'bold italic'),
                                fg = 'red',
                                bg = 'lightblue',
                                activebackground = 'lightgreen',
                                command = self.deck2_but_func)
        self.deck_but2.pack(fill = X)
        self.debug("Deck 2 button is created in the deck frame.")
        self.throw = Button(self.deck_frame,
                            text='Throw',
                            font=('Times', 11, 'bold italic'),
                            fg='red',
                            bg='lightblue',
                            activebackground = 'lightgreen',
                            command = self.throw_func)
        self.throw.pack()
        self.debug("Throw button is also created successfully.")
        self.b_frame = Frame(self.d_frame, background='lightgreen')  # This is the bottom frame of the dealer's frame
        self.b_frame.pack(pady=30)
        self.debug("Created a bottom frame and not going to be debbuged now frame.")
        self.four_but = Button(self.b_frame,
                               text='FOUR SET',
                               font=('Times', 11, 'bold italic'),
                               fg = 'green',
                               bg = 'lightblue',
                               activebackground = 'lightgreen',
                               command = self.four_set_but)  # This is the four set asking button
        self.four_but.pack()
        self.four_but['command'] = self.four_set_but
        self.show = Button(self.b_frame,
                           text='SHOW',
                           font=('Times', 11, 'bold italic'),
                           fg='green',
                           bg='lightblue',
                           activebackground = 'lightgreen',
                           command = self.show_func)  # This is the show button
        self.show.pack()
        self.other_cd = Button(self.b_frame, bg = 'lightgreen',activebackground = 'black')  # This button shows the other card of player
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
                                text = 'Quit',
                                 font=('Times', 15, 'italic'),
                                 fg='black',
                                 bg='lightblue',
                                 activebackground = 'lightgreen',
                                 command = self.win.destroy)
        self.quit_label.pack()
        self.debug("This is the message frame that displays whether the other player took or not took the card.")
        self.deck_but['command'] = self.throw['command'] = ''
        self.debug("Commands of the deck_button and throw button set to **None**")
        for x in self.main_list:
            x['command'] = ''
            self.debug("All the 13 buttons commands are set to None")
        self.debug("&" * 50 + "End Dealers Frame" + "&" * 50)
    def socket(self):
        '''This method contains the base of socket programming that will be mingled with gui '''
        self.debug(">"*50 + "Socket Method" + "<"*50)
        self.xan = socket.socket()# Creating a socket
        self.xan.bind((self.ip, 8000))  # Binding the socket to ip and port
        self.debug("Created a socket and binded to the ip")
        self.xan.listen(1)  # Listening for clients
        self.debug("Listening for the connections.")
        self.conn, addr = self.xan.accept() #Accepting the connection
        self.debug("Connection established successfully.")
        self.conn.send(self.p2_deck_en.encode())
        self.debug("Sending the Encrpyted P2 deck to the Player2::\n{}".format(self.p2_deck_en))
        self.conn.send(self.joker.encode())
        self.debug("Sending the joker{}".format(self.joker))
        self.debug(">"*50 + "End of the Socket" + "<"*50)
    def deck_creater(self):
        '''This method contains the mechanism of deck creation.'''
        self.debug("<"*50 + "Deck_Creator" + ">"*50)
        suits = ['h', 'c', 's', 'd']
        self.deck = []
        for x in range(2, 11):
            for j in suits:
                self.deck.append(str(x) + j)
        self.debug("Creating the total Deck\n{}\n:Length{}".format(self.deck, len(self.deck)))
        faces = ['k', 'q', 'j', 'a']
        for j in faces:
            for k in suits:
                self.deck.append(j + k)
        self.deck.append('Joker')
        self.debug("Full Deck\n{}\n:Length:{}".format(self.deck, len(self.deck)))
        random.shuffle(self.deck)
        self.debug("Shuffled Deck {}\nLength{}".format(self.deck, len(self.deck)))
        self.debug("<"*50 + "End Deck Creator" + ">"*50)
    def deck_divider(self):
        self.debug("["*50 + "Deck Divider" + "]"*50)
        self.p1_deck = []
        self.p2_deck = []
        self.debug("Created the two lists p1_deck and p2_deck")
        for j in range(26):
            if j % 2 == 0:
                self.p1_deck.append(self.deck[j])
                self.debug("P1card:{}".format(self.deck[j]))
            else:
                self.p2_deck.append(self.deck[j])
                self.debug("P2card:{}".format(self.deck[j]))
        self.debug("P1 Deck:{}\nLength:{}\nP2deck:{}\nLength:{}".format(self.p1_deck, len(self.p1_deck), self.p2_deck, len(self.p2_deck)))
        self.deck = self.deck[26:54]
        self.debug("Rest of the Deck:{}\nLength:{}".format(self.deck, len(self.deck)))
        self.debug("["*50 + "End of Deck divider" + "]"*50)
    def p2_deck_encrypter(self):
        '''This method converts p2_deck from list to string for sending it to the client'''
        self.debug("{"*50 + "P2 Deck Encrypter" + "}"*50)
        self.p2_deck_en = ''
        for x in range(13):
            self.p2_deck_en += self.p2_deck[x] + ' '
        self.debug("P2 deck encrypted.{}".format(self.p2_deck_en))
        self.debug("{" * 50 + "P2 Deck Encrpyter" + "}"*50)
    def joker_picker(self):
        self.debug("+"*50 + "Joker Picker" + "+"*50)
        self.joker = self.deck[0]
        self.debug("Joker card is {}".format(self.deck[0]))
        self.deck.pop(0)
        self.debug("After popping the joker deck is {}\nLength:{}".format(self.deck, len(self.deck)))
        self.debug("+"*50 + "Joker Picker End" + "+"*50)
        return self.joker
    def curr_card_func(self):
        '''This function is the function related to the current card button'''
        self.debug("="*50 + "Current Card Function" + "="*50)
        self.show['command'] = ''
        self.debug("Show function set to None.")
        self.debug("P1 deck is {} and Length{}".format(self.p1_deck, len(self.p1_deck)))
        self.p1_deck.append(self.current_card)
        self.debug("P1 Deck is {} and length{}".format(self.p1_deck, len(self.p1_deck)))
        self.message = "Player 1 took the card."
        # We are gonna assign the functions of the 13 cards here
        self.cur_but['image'] = self.bgc
        self.cur_but.image = self.bgc
        self.debug("The image of the current button set to ***BG***")
        self.throw['command'] = self.deck_but['command'] = self.deck_but2['command'] = self.show['command'] = ''
        self.cur_but['command'] = ''
        if self.permit == 1:
            self.four_but['command'] = self.four_set_but
            self.message += "Joker Revealed."
        else:
            self.four_but['command'] = ''
        self.debug("All the buttons throw,deck_but, deck_but2, dealer's deck Buttons and current button function set to none.")
        self.debug("Button funcs is going to be executed next.")
        self.button_funcs()
        self.debug("=" * 50 + "End Current Card Function" + "=" * 50)
    def deck2_but_func(self):
        '''This function is going to be binded with the deck button of the dealers desk deck.'''
        self.debug("#"*50 + "Deck2_Button_Function" + "#"*50)
        self.show['command'] = ''
        self.debug("Show function set to None.")
        self.trash.append(self.current_card)
        self.message = 'Player 1 goes for the deck.'
        self.debug("Trash is {} and length {}".format(self.trash, len(self.trash)))
        self.deck_refiller()
        self.current_card = self.deck[0]
        self.debug("The current card is set to the zeroth card of deck ***{}**".format(self.current_card))
        self.deck.pop(0)
        self.debug("The zeroth is removed and deck is {} and \nlength is {}".format(self.deck, len(self.deck)))
        img = PhotoImage(file = '/usr/lib/Joker3/NewImages/{}.png'.format(self.current_card))
        self.debug("Created an image file of the current card.{}".format(img.__repr__()))
        self.deck_but['image'] = img
        self.deck_but.image = img
        self.debug("The image of the deck button is changed to img that means current card.")
        self.cur_but['image'] = self.bgc
        self.cur_but.image = self.bgc
        self.debug("Current Button image is set to bg")
        self.deck_but2['command'] = self.cur_but['command'] = self.show['command'] = ''
        if self.permit == 1:
            self.four_but['command'] = self.four_set_but
            self.message += "Joker Revealed."
        else:
            self.four_but['command'] = ''
        self.debug("Deck_buttton2||Current_button||four_button||show|| buttons commands set to ***none***")
        self.deck_but['command'] = self.deck_but_func
        self.debug("Deck button command is set to self.deck_but_func")
        self.throw['command'] = self.throw_func
        self.debug("Throw button command is set self.throw_func")
        self.debug("#" * 50 + "End Deck2_Button_Function" + "#" * 50)
    def deck_but_func(self):
        '''This function contains the functions that are to be done by the deck_button'''
        self.debug("$"*50 + "Deck_but_function" + "$"*50)
        self.show['command'] = ''
        self.p1_deck.append(self.current_card)
        self.debug("P1deck:{}\nLength{}\nCurrent Card:{}".format(self.p1_deck, len(self.p1_deck), self.current_card))
        # This is where the 13 buttons will be get activated
        self.deck_but['image'] = self.bgc
        self.deck_but.image = self.bgc
        self.debug("The image of the deck_button is set the back ground.")
        self.deck_but['command'] = self.throw['command'] = self.four_but['command'] = ''
        self.debug("The commands of deck_but and throw are set to ***None***")
        self.debug("All the button are going to be activated by calling the throw_func function.")
        self.button_funcs()
        self.debug("$" * 50 + "End Deck_but_function" + "$" * 50)
    def throw_func(self):
        '''This function will be binded to the throw button of the dealer's desk'''
        self.debug("("*50 + "Throw Function" + ")"*50)
        self.deck_but['command'] = self.deck_but2['command'] =  self.show['command'] = ''
        self.debug("Deck_but; deck_but2; four_but; show; commands are set to ***None")
        self.out_card = self.current_card
        self.debug("The out_card is set to the current card that is {}".format(self.out_card))
        self.deck_but['image'] = self.bgc
        self.deck_but.image = self.bgc
        self.debug("Deck_button image is set to the background.")
        self.deck_but['command'] = self.throw['command'] = ''
        self.debug("Commands of deck_but and throw aare set to ***None")
        img = PhotoImage(file='/usr/lib/Joker3/NewImages/{}.png'.format(self.out_card))
        self.other_cd['image'] = img
        self.other_cd.image = img
        self.debug("The imgage of the button other card is set to {}".format(img.__repr__()))
        self.conn.send(self.message.encode())
        self.debug("Message **{}** is sent to the player 2.".format(self.message))
        self.conn.send(self.out_card.encode())
        time.sleep(1)
        self.debug("Out_card is sent to player 2 {}".format(self.out_card))
        self.deck_refiller()
        self.conn.send(self.deck[0].encode())
        self.debug("The next card is also sent {}".format(self.deck[0]))
        self.debug("The receiving thread is gonna start.")
        self.thread()
        self.debug("(" * 50 + "End Throw Function" + ")" * 50)
    def card012(self, ind):
        '''This function will be binded to all the 13 cards in the Graphical User Interface'''
        self.debug(")"*50 + "Card 0-12 function" + "("*50)
        self.out_card = self.p1_deck[ind]
        self.debug("Out_card**{}** is the index that is gonna passed to the function.".format(self.out_card))
        self.debug("P1 deck is {}".format(self.p1_deck))
        self.debug("The index is {}".format(ind))
        self.p1_deck.pop(ind)
        self.debug("Out_card is popped out is \np1_deck:{}\nLength***{}*** of index ****{}***".format(self.p1_deck, len(self.p1_deck), ind))
        self.debug("P1_deck is going to be sorted now.")
        self.p1_deck.sort()
        self.debug("A loop is going to be executed such that the buttons can acquire the sorted deck order.")
        for x in range(13):
            file = PhotoImage(file='/usr/lib/Joker3/NewImages/{}.png'.format(self.p1_deck[x]))
            self.main_list[x]['image'] = file
            self.main_list[x].image = file
        self.debug("Now p1_deck:{}\nLength{}".format(self.p1_deck, len(self.p1_deck)))
        img = PhotoImage(file = '/usr/lib/Joker3/NewImages/{}.png'.format(self.out_card))
        self.debug("Image is created for the out_card.")
        self.other_cd['image'] = img
        self.other_cd.image = img
        self.debug("Out card image is change to {}".format(img.__repr__()))
        self.conn.send(self.message.encode())
        self.debug("The message ***{}*** is sent.".format(self.message))
        self.conn.send(self.out_card.encode())
        self.debug("The out_card is sent ***{}***".format(self.other_cd))
        time.sleep(1)
        self.deck_refiller()
        self.conn.send(self.deck[0].encode())
        self.debug("The deck card ***{}*** is also sent.".format(self.deck[0]))
        self.debug("All the buttons 0-13 card commands are set to ***None***")
        self.thread()
        self.button_over()
        self.debug(")"*50 + "End Card 0-12 function" + "("*50)
    def button_funcs(self):
        self.debug("!"*50 + "Button_Functions" + "!"*50)
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
        self.debug("All the buttons commands are set to ***None***")
        self.debug("!"*50 + " End Button_Functions" + "!"*50)
    def initial(self):
        self.debug("@"*50 + "Initial Button Function" + "@"*50)
        self.cur_but['command'] = self.curr_card_func
        self.debug("Current button function is set to self.curr_card_function")
        self.deck_but2['command'] = self.deck2_but_func
        self.debug("Deck_button2 command is set self.deck2_but_func")
        self.deck_but['command']= ''
        self.throw['command'] = ''
        self.show['command'] = ''
        self.four_but['command'] = self.four_set_but
        self.debug("deck_but, throw, four_but, show are set to ***None***")
        self.debug("Button_over function is going to be executed.")
        self.button_over()
        self.debug("@" * 50 + " End Initial Button Function" + "@" * 50)
    def button_over(self):
        self.debug("^"*50 + "Button_Over" + "^"*50)
        for x in self.main_list:
            x['command'] = ''
        self.debug("All the commands of the 13 cards are set to ***None***")
        self.debug("^"*50 + "End Button_Over" + "^"*50)
    def deck_refiller(self):
        self.debug("%"*50 + "Start Deck Refiller" + "%"*50)
        self.debug("Entered this method.")
        self.debug("Deck is {}.\nLength:{}".format(self.deck, len(self.deck)))
        self.debug("self.deck==0>>>{}".format(len(self.deck) == 0))
        if len(self.deck) == 0:
            self.debug("Length is zero.")
            self.debug("Statement if true and entered the if block.")
            random.shuffle(self.trash)
            self.deck = self.trash
            self.trash = []
            self.debug("Deck:{}".format(self.deck))
            self.debug("Trash:{}".format(self.trash))
        self.debug("%" * 50 + "End  Deck Refiller" + "%" * 50)
    def four_set_but(self):
        self.debug("|"*50 + "Four   _Set" + "|" * 50)
        self.z_list = []
        for k in self.p1_deck:
            self.z_list.append(k[0])
        self.debug("Z_list:{}".format(self.z_list))
        self.dict = {x:self.z_list.count(x) for x in self.z_list}
        self.m = max(list(self.dict.values()))
        self.debug("Dict:{}\nMax:{}".format(self.dict, self.m))
        joker_wind = Toplevel()
        joker_wind.title('*****JOKER*****')
        but = Button(joker_wind,
                     bd = '3')
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
            self.debug("Maximum value is 4 now.")
            self.permit = 1
        else:
            but['text'] = 'You did not complete the fourth set yet.'
            self.debug("Maximum value is not 4.")
        self.debug("|"*50 + "End Four Set " + "|"*50)
    def show_func(self):
        self.debug("X"*50 + "SHOW" + "X"*50)
        self.debug("|" * 50 + "Four_Set" + "|" * 50)
        self.z_list = []
        for k in self.p1_deck:
            self.z_list.append(k[0])
        self.debug("Z_list:{}".format(self.z_list))
        self.dict = {x: self.z_list.count(x) for x in self.z_list}
        self.m = max(list(self.dict.values()))
        if self.m == 4:
            self.debug("Entered the show and true:")
            self.g_dict = {}    # This implies general dict
            self.n_jokers = 0   #this implies number of jokers
            for k in self.dict:    # This means general dictionary
                if k != self.joker[0] and self.dict[k] != 4 and k != 'J':
                    self.g_dict[k] = self.dict[k]
                    self.debug("Condition true.")
                    self.debug("{}>>>{}".format(k, self.dict[k]))
                elif self.dict[k] != 4:
                    self.n_jokers += self.dict[k]
                    self.debug("Condition False.")
                    self.debug("{}>>>{}".format(k, self.dict[k]))
                    self.debug("JOKERS:{}".format(self.n_jokers))
            vals = list(self.g_dict.values())
            self.debug("Values:{}".format(vals))
            r_jokers = 0    # This means required_jokers
            for j in vals:
                r_jokers += (3 - j)
                self.debug("{}>>>{}".format(j, (3 - j)))
            if r_jokers == self.n_jokers or r_jokers == 0:
                self.debug("You are the winner.")
                self.mess = self.cur_card = self.d_card = "SHOW"
                self.conn.send(self.mess.encode())
                self.debug("{} is sent.".format(self.mess))
                self.conn.send(self.cur_card.encode())
                self.debug("{} is sent.".format(self.cur_card))
                time.sleep(1)
                self.conn.send(self.d_card.encode())
                self.debug("{} is sent.".format(self.d_card))
                self.top_level = Toplevel()
                self.debug("Top level created.")
                self.label = Label(self.top_level,
                                   text = "YOUR ARE THE WINNER",
                                   font = ("TlwgTypist", 20, "bold"))
                self.label.pack()
                self.win.after(1000, self.win.destroy)
        else:
            self.debug("You are not the winner.")
            self.top_level = Toplevel()
            self.label = Label(self.top_level,
                               text="NOT SHOW",
                               font=("TlwgTypist", 20, "bold"),
                               bd=4,
                               relief="groove")
            self.label.pack()
        self.debug("X" * 50 + "END SHOW" + "X" * 50)
    def lose(self):
        self.debug("x"* 50 + "LOSE" + "x" * 50)
        lose_wind = Toplevel()
        bg_img = PhotoImage(file = '/usr/lib/Joker3/joker1.png')
        bg = Label(lose_wind,
                    image = bg_img)
        bg.place(relx = 0.1, rely = 0.1)
        bg.image = bg_img
        label = Label(lose_wind,
                      text = "GAME-OVER\nYou Loose",
                      font =('TlwgTypist', 15, 'bold'))
        label.pack()
        self.win.after(400, self.win.destroy)
        self.debug("x" * 50 + "END LOSE" + "x" * 50)
    def ok_func(self):
        self.ip = self.entry.get()
        self.window.quit()
        self.window.destroy()
    def cancel_func(self):
        self.window.quit()
        self.window.destroy()
obj = Poker()