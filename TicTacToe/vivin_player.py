import random
# function to check if X has won
def has_X_won(board):
    row1 = board[0]
    row2 = board[1]
    row3 = board[2]
    col1 = [row[0] for row in board]
    col2 = [row[1] for row in board]
    col3 = [row[2] for row in board]
    diag1 = [row[x] for x,row in enumerate(board)]
    diag2 = [row[2-x] for x, row in enumerate(board)]
    lines = [row1, row2, row3, col1, col2, col3, diag1, diag2]
    for line in lines:
        if line == ["X", "X", "X"]:
            return True
    return False

# function to check if we've won
def has_O_won(board):
    row1 = board[0]
    row2 = board[1]
    row3 = board[2]
    col1 = [row[0] for row in board]
    col2 = [row[1] for row in board]
    col3 = [row[2] for row in board]
    diag1 = [row[x] for x,row in enumerate(board)]
    diag2 = [row[2-x] for x, row in enumerate(board)]
    lines = [row1, row2, row3, col1, col2, col3, diag1, diag2]
    for line in lines:
        if line == ["O", "O", "O"]:
            return True
    return False

def get_free_places(board):
    free_places = []
    # going through each place to see if it's a free place
    rowno = 0
    colno = 0
    for row in board:
        colno = 0
        for square in row:
            if square == "-":
                free_places.append((rowno,colno))
            colno += 1
        rowno += 1
    return free_places


def minimax(board,is_X_turn):
    if has_X_won(board):
        return [0,0,1]
    if has_O_won(board):
        return [0,0,-1]
    free_places = get_free_places(board)
    if len(free_places) == 0:
        return [0,0,0]
    if is_X_turn:
        best_move = [-1,-1,-2]
        for move in free_places:
            new_row1 = board[0].copy()
            new_row2 = board[1].copy()
            new_row3 = board[2].copy()
            new_board = [new_row1,new_row2,new_row3]
            new_board[move[0]][move[1]] = "X"
            score = minimax(new_board,False)
            if score[2] > best_move[2]:
                best_move[2] = score[2]
                best_move[0] = move[0] 
                best_move[1] = move[1]
    else:
        best_move = [-1,-1,+2]
        for move in free_places:
            new_row1 = board[0].copy()
            new_row2 = board[1].copy()
            new_row3 = board[2].copy()
            new_board = [new_row1,new_row2,new_row3]
            new_board[move[0]][move[1]] = "O"
            score = minimax(new_board,True)
            if score[2] < best_move[2]:
                best_move[2] = score[2]
                best_move[0] = move[0] 
                best_move[1] = move[1]
    return best_move
    



    

# [['X','O','-'],
# ['X','O','-'],
# ['X','-','-']]
# col0 = [row[0] for row in board]

# making board a 2D array, making free places an array of tuples
my_player = "O"
row1 = list(input())
row2 = list(input())
row3 = list(input())
board = [row1, row2, row3]
# print(board[1][1])


# # plays each possibility to see if we have won
# for place in free_places:
#     new_row1 = row1.copy()
#     new_row2 = row2.copy()
#     new_row3 = row3.copy()
#     new_board = [new_row1,new_row2,new_row3]
#     new_board[place[0]][place[1]] = "O" 
#     if has_O_won(new_board):
#         print(place[0],place[1])
#         exit(0) 

# # plays each possibility to see if x has won
# for place in free_places:
#     new_row1 = row1.copy()
#     new_row2 = row2.copy()
#     new_row3 = row3.copy()
#     new_board = [new_row1,new_row2,new_row3]
#     new_board[place[0]][place[1]] = "X" 
#     if has_X_won(new_board):
#         print(place[0],place[1])
#         exit(0) 

# # if neither of the above options work, we randomize the place
# random_chooser = random.randint(0,len(free_places)-1)
# print(free_places[random_chooser][0],free_places[random_chooser][1])

best_move = minimax(board,False)
print(best_move[0],best_move[1])