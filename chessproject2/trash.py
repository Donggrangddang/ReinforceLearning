import numpy as np




board = np.zeros((8, 8), dtype=int)
board[1][:] = board[6][:] = 1
for i in range(3):
    board[0][i] = board[0][7 - i] = 4 - i
    board[7][i] = board[7][7 - i] = 4 - i
board[0][3] = board[7][3] = 5
board[0][4] = board[7][4] = 6
print(board)