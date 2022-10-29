from tkinter import *
import tkinter.messagebox

def start():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    count = 0
    clicked = True

    b1 = Button(root, width=10, height=5, bg="lavender", command=lambda:click(b1))
    b2 = Button(root, width=10, height=5, bg="lavender", command=lambda:click(b2))
    b3 = Button(root, width=10, height=5, bg="lavender", command=lambda:click(b3))

    b4 = Button(root, width=10, height=5, bg="lavender", command=lambda:click(b4))
    b5 = Button(root, width=10, height=5, bg="lavender", command=lambda:click(b5))
    b6 = Button(root, width=10, height=5, bg="lavender", command=lambda:click(b6))

    b7 = Button(root, width=10, height=5, bg="lavender", command=lambda:click(b7))
    b8 = Button(root, width=10, height=5, bg="lavender", command=lambda:click(b8))
    b9 = Button(root, width=10, height=5, bg="lavender", command=lambda:click(b9))

    b1.grid(row = 0, column = 0)
    b2.grid(row = 0, column = 1)
    b3.grid(row = 0, column = 2)

    b4.grid(row = 1, column = 0)
    b5.grid(row = 1, column = 1)
    b6.grid(row = 1, column = 2)

    b7.grid(row = 2, column = 0)
    b8.grid(row = 2, column = 1)
    b9.grid(row = 2, column = 2)
       
def check_win():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global winner
    global new_button
    winner = False
    if count == 9 and winner == False:
        tkinter.messagebox.showinfo("Конец игры", "  Ничья!!!  ")
        start()
    elif b1['text'] == b2['text'] == b3['text'] == 'X':
        winner = True
        win = 'X'
    elif b1['text'] == b2['text'] == b3['text'] == 'O':
        winner = True
        win = 'O'
    elif b4['text'] == b5['text'] == b6['text'] == 'X':
        winner = True
        win = 'X'
    elif b4['text'] == b5['text'] == b6['text'] == 'O':
        winner = True
        win = 'O'
    elif b7['text'] == b8['text'] == b9['text'] == 'X':
        winner = True
        win = 'X'
    elif b7['text'] == b8['text'] == b9['text'] == 'O':
        winner = True
        win = 'O'
    elif b1['text'] == b5['text'] == b9['text'] == 'X':
        winner = True
        win = 'X'
    elif b1['text'] == b5['text'] == b9['text'] == 'O':
        winner = True
        win = 'O'
    elif b3['text'] == b5['text'] == b7['text'] == 'X':
        winner = True
        win = 'X'
    elif b3['text'] == b5['text'] == b7['text'] == 'O':
        winner = True
        win = 'O'
    elif b1['text'] == b4['text'] == b7['text'] == 'X':
        winner = True
        win = 'X'
    elif b1['text'] == b4['text'] == b7['text'] == 'O':
        winner = True
        win = 'O'
    elif b2['text'] == b5['text'] == b8['text'] == 'X':
        winner = True
        win = 'X'
    elif b2['text'] == b5['text'] == b8['text'] == 'O':
        winner = True
        win = 'O'
    elif b3['text'] == b6['text'] == b9['text'] == 'X':
        winner = True
        win = 'X'
    elif b3['text'] == b6['text'] == b9['text'] == 'O':
        winner = True
        win = 'O'

    if winner == True:
        tkinter.messagebox.showinfo("Конец игры", "Выиграл " + win)
        start()

def click(b):
    global clicked, count
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    if b['text'] == '' and clicked == True:
        b.config(text = 'X', bg = 'white', state = 'disabled')
        clicked = False
        count+=1
        check_win()
    elif b['text'] == '' and clicked == False:
        b.config(text = 'O', bg = 'white', state  = 'disabled')
        clicked = True
        count += 1
        check_win()

root = Tk()
root.title("Крестики-нолики")
root.resizable(False, False)

start()
root.mainloop()