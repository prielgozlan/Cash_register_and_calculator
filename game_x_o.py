from tkinter import *
from tkinter import ttk

current_player = "X"

root = Tk()
root.title("tic tac toc")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(W, N, E, S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
current_label = ttk.Label(mainframe, text=f"current player:{current_player}")
current_label.grid(column=0, row=0, sticky=W)

winner_label = ttk.Label(mainframe, text="Winner: ")
winner_label.grid(column=0, row=4, columnspan=3)


def on_button_pressed(i, j):
    global current_player
    if button[i - 1][j - 1]['text'] == '':
        button[i - 1][j - 1]['text'] = current_player
        current_player = "O" if current_player == "X" else "X"
        current_label['text'] = f"current player: {current_player}"
        check_winner()


def check_winner():
    for i in range(3):
        if button[i][0]['text'] == button[i][1]['text'] == button[i][2]['text'] != '':
            winner_label['text'] = f"Winner: {button[i][0]['text']}"
            print(f"Player {button[i][0]['text']} wins!")
            return
        if button[0][i]['text'] == button[1][i]['text'] == button[2][i]['text'] != '':
            winner_label['text'] = f"Winner: {button[0][i]['text']}"
            print(f"Player {button[0][i]['text']} wins!")
            return
    if button[0][0]['text'] == button[1][1]['text'] == button[2][2]['text'] != '':
        winner_label['text'] = f"Winner: {button[0][0]['text']}"
        print(f"Player {button[0][0]['text']} wins!")
        return
    if button[0][2]['text'] == button[1][1]['text'] == button[2][0]['text'] != '':
        winner_label['text'] = f"Winner: {button[0][2]['text']}"
        print(f"Player {button[0][2]['text']} wins!")
        return
    if all(btn['text'] != '' for row in button for btn in row):
        winner_label['text'] = "Tie!"
        print("It's a tie!")
        return


# יצירת Button
button = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(ttk.Button(mainframe, text='', command=lambda i=i, j=j: on_button_pressed(i + 1, j + 1)))
        row[-1].grid(column=i, row=j + 1, sticky=(W, E))
    button.append(row)

root.mainloop()
