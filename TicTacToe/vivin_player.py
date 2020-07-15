import random
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

def have_we_won(board):
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

# [['X','O','-'],
# ['X','O','-'],
# ['X','-','-']]
# col0 = [row[0] for row in board]

my_player = "O"
row1 = list(input())
row2 = list(input())
row3 = list(input())
board = [row1, row2, row3]
# print(board[1][1])
free_places = []
rowno = 0
colno = 0
for row in board:
    colno = 0
    for square in row:
        if square == "-":
            free_places.append((rowno,colno))
        colno += 1
    rowno += 1
# print(free_places)

for place in free_places:
    new_row1 = row1.copy()
    new_row2 = row2.copy()
    new_row3 = row3.copy()
    new_board = [new_row1,new_row2,new_row3]
    new_board[place[0]][place[1]] = "O" 
    if have_we_won(new_board):
        print(place[0],place[1])
        exit(0) 

for place in free_places:
    new_row1 = row1.copy()
    new_row2 = row2.copy()
    new_row3 = row3.copy()
    new_board = [new_row1,new_row2,new_row3]
    new_board[place[0]][place[1]] = "X" 
    if has_X_won(new_board):
        print(place[0],place[1])
        exit(0) 

random_chooser = random.randint(0,len(free_places)-1)
print(free_places[random_chooser][0],free_places[random_chooser][1])