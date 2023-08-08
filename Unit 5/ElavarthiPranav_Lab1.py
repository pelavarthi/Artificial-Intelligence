width = 10
height = 4
xword = "##--##--###------######--######--------#"
OPENCHAR = "-"
PROTECTEDCHAR = "~"
BLOCKCHAR = "#"

def area_fill(board, sp, dirs = [-1, width, 1, -1*width]):
    if sp < 0 or sp >= len(board): return board
    if board[sp] in {OPENCHAR, PROTECTEDCHAR}:
        board = board[0:sp] + '?' + board[sp+1:]
        for d in dirs:
            if d == -1 and sp % width == 0: continue #left edge
            if d == 1 and sp+1 % width == 0: continue #right edge
            board = area_fill(board, sp+d, dirs)
    return board

def checkConnected(board):
    sp = -1
    for i in range(len(board)):
        if board[i] != BLOCKCHAR:
            sp = i
            break
    if sp == -1:
        return True
    x = area_fill(xword, 2)
    for i in range(height):
        print(x[i*width:i*width+width])
    for char in x:
        if char == PROTECTEDCHAR or char == OPENCHAR:
            return False
    return True

print(checkConnected(xword))