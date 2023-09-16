import tkinter as tk
from tkinter import messagebox


current_player = 'X'
board = [['' for _ in range(3)] for _ in range(3)]

def check_winner():
    
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != '':
            return board[0][i]
    
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]

    return None

def on_click(row, col):
    global current_player

    
    if board[row][col] == '' and check_winner() is None:
       
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)
        
        
        winner = check_winner()
        if winner:
            messagebox.showinfo("Tic Tac Toe", f"Player {winner} wins!")
            reset_game()
        elif all(board[i][j] != '' for i in range(3) for j in range(3)):
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            reset_game()
        else:
           
            current_player = 'O' if current_player == 'X' else 'X'

def reset_game():
    global current_player, board
    current_player = 'X'
    board = [['' for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text='', state=tk.NORMAL)


root = tk.Tk()
root.title("Tic Tac Toe")


buttons = []
for i in range(3):
    row_buttons = []
    for j in range(3):
        button = tk.Button(root, text='', width=10, height=3, command=lambda row=i, col=j: on_click(row, col))
        button.grid(row=i, column=j)
        row_buttons.append(button)
    buttons.append(row_buttons)


reset_button = tk.Button(root, text="Reset Game", command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3)

root.mainloop()
