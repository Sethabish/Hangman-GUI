import os
import sys
import random
from tkinter import *
from words import words
import tkinter.font as font


# Resource path function to help build .exe with images and folders
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


root = Tk()
root.title('Hangman - 2444 Words')
root.resizable(False, False)
root.iconbitmap(resource_path("images\hm.ico"))

frame = Frame(root)
frame.pack()

canvas = Canvas(frame, bg="#e0f0e3", width=600, height=550)
canvas.pack()

# To choose a random word from the words list and create the blank output
rand_word = list(random.choice(words))
output = list('_'*len(rand_word))
turn, n, o = 7, '', []
won, lost = 0, 0


# Function to disable all buttons
def disable_all():
    global buttons
    for i in range(26):
        buttons[i]['state'] = DISABLED


# The main function
def check(inp):
    m = ''
    global output, o, n, turn, won, lost
    images = [img13, img1, img2, img3, img4, img5, img6, img7]
    canvas.create_image(470, 160, image=img13)

    # To display the output with correctly guessed letters
    for i in range(len(rand_word)):
        if rand_word[i] == inp:
            output[i] = inp
        m = m + output[i].upper() + ' '
        Label(canvas, text=m, font=labelfont, bg="#e0f0e3", fg='#2a623d').place(x=20, y=240)

    # To display the wrong letter choices and the number of tries left
    if inp not in rand_word:
        o.append(inp)
        turn = turn - 1
        n = n + inp.upper() + ' '
        Label(canvas, text='Wrong Choices: ' + n, font=labelfont, bg="#e0f0e3", fg='#634832').place(x=10, y=160)
        Label(canvas, text='Tries Left: ' + str(turn), font=labelfont, bg="#e0f0e3", fg='#634832').place(x=10, y=110)

        # To display the number of times the word is not guessed correctly
        if turn == 0:
            lost = lost + 1
            Label(canvas, text='👎: '+str(lost), font=labelfont, bg="#e0f0e3", fg='#634832').place(x=260, y=110)

    # To build hangman with every wrong guess
    for j in range(8):
        if len(o) == j:
            canvas.create_image(470, 160, image=images[j])

    # To count and display the number of correct word guesses
    if rand_word == output:
        won = won + 1
        canvas.create_image(470, 160, image=img0)
        Label(canvas, text='👍: ' + str(won), font=labelfont, bg="#e0f0e3", fg='#634832').place(x=180, y=110)

    # To disable all buttons except restart button after 7 wrong guesses or after guessing the correct word
    if len(o) == 7 or rand_word == output:
        disable_all()


# Resets the game except the correct and wrong guesses
def restart():
    global output, turn, o, n, rand_word, buttons
    rand_word = list(random.choice(words))
    output = list('_' * len(rand_word))
    turn, o, n = 7, [], ''
    for i in range(26):
        buttons[i]['state'] = NORMAL
    canvas.create_image(470, 160, image=img13)
    canvas.create_image(470, 160, image=img14)
    Label(canvas, text='Tries Left: 7', font=labelfont, bg="#e0f0e3", fg='#634832').place(x=10, y=110)
    Label(canvas, text='                                   ', font=labelfont, bg="#e0f0e3").place(x=20, y=240)
    Label(canvas, text='_ ' * len(rand_word), font=labelfont, bg="#e0f0e3", fg='#2a623d').place(x=20, y=240)
    Label(canvas, text='Wrong Choices:                     ', font=labelfont, bg="#e0f0e3", fg='#634832').place(x=10, y=160)


# Initializing all the labels, buttons, images
labelfont = font.Font(family='Comic Sans MS', size=15, weight='bold')
Label(canvas, text='_ '*len(rand_word), font=labelfont, bg="#e0f0e3", fg='#2a623d').place(x=20, y=240)
Label(canvas, text='Tries Left: 7', font=labelfont, bg="#e0f0e3", fg='#634832').place(x=10, y=110)
Label(canvas, text='👍: '+str(won), font=labelfont, bg="#e0f0e3", fg='#634832').place(x=180, y=110)
Label(canvas, text='👎: '+str(lost), font=labelfont, bg="#e0f0e3", fg='#634832').place(x=260, y=110)
Label(canvas, text='Wrong Choices:', font=labelfont, bg="#e0f0e3", fg='#634832').place(x=10, y=160)

img0 = PhotoImage(file=resource_path('images\hm0.png'))
img1 = PhotoImage(file=resource_path('images\hm1.png'))
img2 = PhotoImage(file=resource_path('images\hm2.png'))
img3 = PhotoImage(file=resource_path('images\hm3.png'))
img4 = PhotoImage(file=resource_path('images\hm4.png'))
img5 = PhotoImage(file=resource_path('images\hm5.png'))
img6 = PhotoImage(file=resource_path('images\hm6.png'))
img7 = PhotoImage(file=resource_path('images\hm7.png'))
img8 = PhotoImage(file=resource_path('images\h1.png'))
img9 = PhotoImage(file=resource_path('images\h2.png'))
img10 = PhotoImage(file=resource_path('images\h3.png'))
img11 = PhotoImage(file=resource_path('images\h4.png'))
img12 = PhotoImage(file=resource_path('images\h5.png'))
img13 = PhotoImage(file=resource_path('images\o.png'))
img14 = PhotoImage(file=resource_path('images\hm8.png'))

canvas.create_image(35, 50, image=img8)
canvas.create_image(85, 50, image=img9)
canvas.create_image(135, 50, image=img10)
canvas.create_image(185, 50, image=img11)
canvas.create_image(235, 50, image=img12)
canvas.create_image(285, 50, image=img9)
canvas.create_image(335, 50, image=img10)
canvas.create_image(470, 160, image=img14)

keya = PhotoImage(file=resource_path('keys\Letter-A-icon.png'))
keyb = PhotoImage(file=resource_path('keys\Letter-B-icon.png'))
keyc = PhotoImage(file=resource_path('keys\Letter-C-icon.png'))
keyd = PhotoImage(file=resource_path('keys\Letter-D-icon.png'))
keye = PhotoImage(file=resource_path('keys\Letter-E-icon.png'))
keyf = PhotoImage(file=resource_path('keys\Letter-F-icon.png'))
keyg = PhotoImage(file=resource_path('keys\Letter-G-icon.png'))
keyh = PhotoImage(file=resource_path('keys\Letter-H-icon.png'))
keyi = PhotoImage(file=resource_path('keys\Letter-I-icon.png'))
keyj = PhotoImage(file=resource_path('keys\Letter-J-icon.png'))
keyk = PhotoImage(file=resource_path('keys\Letter-K-icon.png'))
keyl = PhotoImage(file=resource_path('keys\Letter-L-icon.png'))
keym = PhotoImage(file=resource_path('keys\Letter-M-icon.png'))
keyn = PhotoImage(file=resource_path('keys\Letter-N-icon.png'))
keyo = PhotoImage(file=resource_path('keys\Letter-O-icon.png'))
keyp = PhotoImage(file=resource_path('keys\Letter-P-icon.png'))
keyq = PhotoImage(file=resource_path('keys\Letter-Q-icon.png'))
keyr = PhotoImage(file=resource_path('keys\Letter-R-icon.png'))
keys = PhotoImage(file=resource_path('keys\Letter-S-icon.png'))
keyt = PhotoImage(file=resource_path('keys\Letter-T-icon.png'))
keyu = PhotoImage(file=resource_path('keys\Letter-U-icon.png'))
keyv = PhotoImage(file=resource_path('keys\Letter-V-icon.png'))
keyw = PhotoImage(file=resource_path('keys\Letter-W-icon.png'))
keyx = PhotoImage(file=resource_path('keys\Letter-X-icon.png'))
keyy = PhotoImage(file=resource_path('keys\Letter-Y-icon.png'))
keyz = PhotoImage(file=resource_path('keys\Letter-Z-icon.png'))
keyre = PhotoImage(file=resource_path('keys\e.png'))

buta = Button(canvas, image=keya, borderwidth=0, bg="#e0f0e3", activebackground="#e0f0e3", command=lambda: [check('a')])
butb = Button(canvas, image=keyb, borderwidth=0, bg="#e0f0e3", activebackground="#e0f0e3", command=lambda: [check('b')])
butc = Button(canvas, image=keyc, borderwidth=0, bg="#e0f0e3", activebackground="#e0f0e3", command=lambda: [check('c')])
butd = Button(canvas, image=keyd, borderwidth=0, bg="#e0f0e3", activebackground="#e0f0e3", command=lambda: [check('d')])
bute = Button(canvas, image=keye, borderwidth=0, bg="#e0f0e3", activebackground="#e0f0e3", command=lambda: [check('e')])
butf = Button(canvas, image=keyf, borderwidth=0, bg="#e0f0e3", activebackground="#e0f0e3", command=lambda: [check('f')])
butg = Button(canvas, image=keyg, borderwidth=0, bg="#e0f0e3", activebackground="#e0f0e3", command=lambda: [check('g')])
buth = Button(canvas, image=keyh, borderwidth=0, bg="#e0f0e3", activebackground="#e0f0e3", command=lambda: [check('h')])
buti = Button(canvas, image=keyi, borderwidth=0, bg="#e0f0e3", activebackground="#e0f0e3", command=lambda: [check('i')])
butj = Button(canvas, image=keyj, borderwidth=0, bg="#e0f0e3", activebackground="#e0f0e3", command=lambda: [check('j')])
butk = Button(canvas, image=keyk, borderwidth=0, bg="#e0f0e3", activebackground="#e0f0e3", command=lambda: [check('k')])
butl = Button(canvas, image=keyl, borderwidth=0, bg="#e0f0e3", activebackground="#e0f0e3", command=lambda: [check('l')])
butm = Button(canvas, image=keym, borderwidth=0, bg="#e0f0e3", activebackground="#e0f0e3", command=lambda: [check('m')])
butn = Button(canvas, image=keyn, borderwidth=0, bg="#e0f0e3", activebackground="#e0f0e3", command=lambda: [check('n')])
buto = Button(canvas, image=keyo, borderwidth=0, bg="#e0f0e3", activebackground="#e0f0e3", command=lambda: [check('o')])
butp = Button(canvas, image=keyp, borderwidth=0, bg="#e0f0e3", activebackground="#e0f0e3", command=lambda: [check('p')])
butq = Button(canvas, image=keyq, borderwidth=0, bg="#e0f0e3", activebackground="#e0f0e3", command=lambda: [check('q')])
butr = Button(canvas, image=keyr, borderwidth=0, bg="#e0f0e3", activebackground="#e0f0e3", command=lambda: [check('r')])
buts = Button(canvas, image=keys, borderwidth=0, bg="#e0f0e3", activebackground="#e0f0e3", command=lambda: [check('s')])
butt = Button(canvas, image=keyt, borderwidth=0, bg="#e0f0e3", activebackground="#e0f0e3", command=lambda: [check('t')])
butu = Button(canvas, image=keyu, borderwidth=0, bg="#e0f0e3", activebackground="#e0f0e3", command=lambda: [check('u')])
butv = Button(canvas, image=keyv, borderwidth=0, bg="#e0f0e3", activebackground="#e0f0e3", command=lambda: [check('v')])
butw = Button(canvas, image=keyw, borderwidth=0, bg="#e0f0e3", activebackground="#e0f0e3", command=lambda: [check('w')])
butx = Button(canvas, image=keyx, borderwidth=0, bg="#e0f0e3", activebackground="#e0f0e3", command=lambda: [check('x')])
buty = Button(canvas, image=keyy, borderwidth=0, bg="#e0f0e3", activebackground="#e0f0e3", command=lambda: [check('y')])
butz = Button(canvas, image=keyz, borderwidth=0, bg="#e0f0e3", activebackground="#e0f0e3", command=lambda: [check('z')])
butre = Button(canvas, image=keyre, borderwidth=0, bg="#e0f0e3", activebackground="#e0f0e3", command=restart)

buttons = [buta, butb, butc, butd, bute, butf, butg, buth, buti, butj, butk, butl, butm, butn, buto, butp, butq, butr,
           buts, butt, butu, butv, butw, butx, buty, butz]

buta.place(x=55, y=340)
butb.place(x=110, y=340)
butc.place(x=165, y=340)
butd.place(x=220, y=340)
bute.place(x=275, y=340)
butf.place(x=330, y=340)
butg.place(x=385, y=340)
buth.place(x=440, y=340)
buti.place(x=495, y=340)
butj.place(x=55, y=400)
butk.place(x=110, y=400)
butl.place(x=165, y=400)
butm.place(x=220, y=400)
butn.place(x=275, y=400)
buto.place(x=330, y=400)
butp.place(x=385, y=400)
butq.place(x=440, y=400)
butr.place(x=495, y=400)
buts.place(x=55, y=460)
butt.place(x=110, y=460)
butu.place(x=165, y=460)
butv.place(x=220, y=460)
butw.place(x=275, y=460)
butx.place(x=330, y=460)
buty.place(x=385, y=460)
butz.place(x=440, y=460)
butre.place(x=495, y=460)

root.mainloop()
