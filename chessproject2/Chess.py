import numpy as np
'''
    말 id: 폰=1, 나이트=2, 룩=4, 비숍=3, 퀸=5, 킹=6
    player_id: white = 1, black = -1
'''

board = np.zeros((8, 8), dtype=int)
board[1][:] = -1
board[6][:] = 1
for i in range(3):
    board[0][i] = board[0][7 - i] = i - 4
    board[7][i] = board[7][7 - i] = 4 - i
board[0][3] = -5
board[7][3] = 5
board[0][4] = -6
board[7][4] = 6

self.board = board
self.turn = 0
self.record = []

def straight_move(self, curr_position):
    # curr_position = [curr_position_x, curr_position_y]

    able_position = []
    curr_position_x = curr_position[0]
    curr_position_y = curr_position[1]

    for i in range(8):
        able_position.append([curr_position_x, i])
        able_position.append([i, curr_position_y])

    return able_position

def diagonal_move(self, curr_position):
    # curr_position = [curr_position_x, curr_position_y]

    able_position = []
    curr_position_x = curr_position[0]
    curr_position_y = curr_position[1]
    
    for i in range(-7, 8):
        able_position.append([max(-1, curr_position_x + i), max(-1, curr_position_y + i)])
        able_position.append([max(-1, curr_position_x - i), max(-1, curr_position_y + i)])

    for next_position_x, next_position_y in able_position:
        if next_position_x == -1 or next_position_y == -1:
            able_position.remove([next_position_x, next_position_y])
    
    return able_position

def knight_move(self, curr_position):
    # curr_position = [curr_position_x, curr_position_y]

    able_position = []
    curr_position_x = curr_position[0]
    curr_position_y = curr_position[1]

    for i in range(-1, 2, 2):
        able_position.append([curr_position_x + 1, curr_position_y + 2 * i])
        able_position.append([curr_position_x - 1, curr_position_y + 2 * i])
        able_position.append([curr_position_x + 2, curr_position_y + 1 * i])
        able_position.append([curr_position_x - 2, curr_position_y + 1 * i])

    for next_position_x, next_position_y in able_position:
        if next_position_x < 0 or next_position_y < 0:
            able_position.remove([next_position_x, next_position_y])

    return able_position

def king_move(self, curr_position):
    # curr_position = [curr_position_x, curr_position_y]

    able_position = []
    curr_position_x = curr_position[0]
    curr_position_y = curr_position[1]

    for i in range(-1, 2):
        for j in range(-1, 2):
            able_position.append([curr_position_x + i, curr_position_y + j])

    able_position.remove([curr_position_x, curr_position_y]) 

    return able_position

def pawn_move(self, curr_position, player_id):
    # curr_position = [curr_position_x, curr_position_y]

    able_position = []
    curr_position_x = curr_position[0]
    curr_position_y = curr_position[1]

    if curr_position_y == 1 and player_id == -1:
        able_position.append([curr_position_x, curr_position_y + 1])
        able_position.append([curr_position_x, curr_position_y + 2])
    elif curr_position_y == 6 and player_id == 1:
        able_position.append([curr_position_x, curr_position_y - 1])
        able_position.append([curr_position_x, curr_position_y - 2])
    else:
        for i in range(-1, 2):
            able_position.append([curr_position_x + i, curr_position_y - player_id])

    for next_position_x, next_position_y in able_position:
        if next_position_x < 0 or next_position_y < 0:
            able_position.remove([next_position_x, next_position_y])

    return able_position

def interpreter(self):

    command = input('')
    listed_command = list(command)
    listed_command_alphabet = []
    listed_command_number = []
    piece = None

    for item in listed_command:
        if item.isdigit():
            listed_command_number.append(item)
        else:
            if item.isupper():
                piece = item
            else:
                listed_command_alphabet.append(item)

    def able_take(listed_command_alphabet):
        if 'x' in listed_command_alphabet:
            return True
        return False
    
    def position_converter(listed_command_alphabet, listed_command_number):
        command_x = []
        command_y = []

        for alphabet in listed_command_alphabet:
            command_x.append(ord(alphabet) - 97)
        for number in listed_command_number:
            command_y.append(int(number) - 1)
        
        return command_x, command_y

                
    if piece == None: # 폰
        
    elif piece == 'N': # 나이트
        pass
    elif piece == 'B': # 비숍
        pass
    elif piece == 'R': # 룩
        pass
    elif piece == 'Q': # 퀸
        pass
    elif piece == 'K' # 킹
        pass
    else:
        print('errorcode : 1\nwrong piece')


'''폰 움직임
직선 움직임
대각선 움직임
킹 움직임
나이트 움직임

가능한 이동인지 검사

들어오는 기호 해석

메이트

체크

강제수

앙파상

캐슬링

행마법(폰 끝까지 가면 바꾸기)'''




            
        