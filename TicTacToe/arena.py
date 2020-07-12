#arena.py
import subprocess

board =[['-','-','-'],
['-','-','-'],
['-','-','-']]

def validate(board):
	assert(len(board)==3)
	assert(len(board[0])==3)
	assert(len(board[1])==3)
	assert(len(board[2])==3)
	for row in board:
		for square in row:
			assert(square == '-' or square == 'X' or square == 'O')

def isXLine(line):
	return line[0]=='X' and line[1]=='X' and line[2]=='X'

def isOLine(line):
	return line[0]=='O' and line[1]=='O' and line[2]=='O'


def isLineFinished(line):
	return isXLine(line) or isOLine(line)

def getEmptySpaces(board):
	arr = []
	for i in range(3):
		for j in range(3):
			if (board[i][j]=='-'):
				arr.append((i,j))
	return arr

def isFinished(board):
	
	row0 = board[0]
	row1 = board[1]
	row2 = board[2]

	col0 = [row[0] for row in board]
	col1 = [row[1] for row in board]
	col2 = [row[2] for row in board]

	diag0 = [row[i] for i,row in enumerate(board)]
	diag1 = [row[2-i] for i,row in enumerate(board)]

	lines = [row0,row1,row2,col0,col1,col2,diag0,diag1]

	for line in lines:
		if isLineFinished(line):
			return True

	if len(getEmptySpaces(board))==0:
		return True
	return False

def hasXWon(board):
	row0 = board[0]
	row1 = board[1]
	row2 = board[2]

	col0 = [row[0] for row in board]
	col1 = [row[1] for row in board]
	col2 = [row[2] for row in board]

	diag0 = [row[i] for i,row in enumerate(board)]
	diag1 = [row[2-i] for i,row in enumerate(board)]

	lines = [row0,row1,row2,col0,col1,col2,diag0,diag1]

	for line in lines:
		if isXLine(line):
			return True
	return False


def hasOWon(board):
	row0 = board[0]
	row1 = board[1]
	row2 = board[2]

	col0 = [row[0] for row in board]
	col1 = [row[1] for row in board]
	col2 = [row[2] for row in board]

	diag0 = [row[i] for i,row in enumerate(board)]
	diag1 = [row[2-i] for i,row in enumerate(board)]

	lines = [row0,row1,row2,col0,col1,col2,diag0,diag1]

	for line in lines:
		if isOLine(line):
			return True
	return False

def isDraw(board):
	return len(getEmptySpaces(board))==0 and (not hasXWon(board)) and (not hasOWon(board))

def readBoardFromInput():
	board1 = list(input())
	board2 = list(input())
	board3 = list(input())
	return [board1,board2,board3]

def boardToString(board):
	myStr = ""
	for row in board:
		for x in row:
			myStr += x
		myStr += "\n"
	return myStr

def isValidMove(board, x, y):
	if x<0 or x> 2 or y < 0 or y> 2:
		return False
	if board[x][y]!='-':
		return False
	return True


isPlayerOneTurn = True
while not isFinished(board):

	print(boardToString(board))

	print()

	if isPlayerOneTurn:
		playerInput = [-1,-1]
		while(not isValidMove(board,playerInput[0],playerInput[1])):
			playerInput = list(map(int,input().split()))
		board[playerInput[0]][playerInput[1]]='X'
	else:
		result = subprocess.run(["python","random_player.py"],input=boardToString(board), capture_output=True, text=True)

		# print(result.stdout)
		# print(result.stderr)

		programInput = list(map(int,result.stdout.split()))
		board[programInput[0]][programInput[1]]='O'

	isPlayerOneTurn = not isPlayerOneTurn


print(boardToString(board))
print()

print("THE GAME IS FINISHED")
if(hasXWon(board)):
	print("X HAS WON")
elif(hasOWon(board)):
	print("O HAS WON")
else:
	print("IT IS A DRAW")
exit(0)

# result = subprocess.run(["python","random_player.py"],input=boardToString(board), capture_output=True, text=True)
# print(result.stdout)
# process = Popen(["python", "random_player.py"], stdout=PIPE)
# (output, err) = process.communicate()
# exit_code = process.wait()


#MAIN