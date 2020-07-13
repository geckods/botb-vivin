import random
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
random_chooser = random.randint(0,len(free_places)-1)
print(free_places[random_chooser][0],free_places[random_chooser][1])