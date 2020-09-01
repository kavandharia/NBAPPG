from tkinter import *
from tkinter import ttk
import NBA_Stats


def Points():
    global entry1
    global output
    player = str(defaultPlayer.get())
    m = NBA_Stats
    output = m.printModel(player)

root = Tk()
root.title('NBA Player Model')
root.geometry('400x100')

player = Label(root, text = 'Player:')
player.place(x = 25, y = 20)

defaultPlayer = StringVar(root)
defaultPlayer.set(NBA_Stats.playerList[0])
entry1 = ttk.Combobox(root, textvariable = defaultPlayer)
entry1.place(x = 100, y = 20)
entry1['values'] = NBA_Stats.playerList



search = Button(root, text = 'Search', command = Points)
search.place(x = 250, y = 20)


root.mainloop()