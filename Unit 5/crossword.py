import sys; args = sys.argv[1:]
import re
import random

BLOCKCHAR = "#"
OPENCHAR = "-"
PROTECTEDCHAR = "~"
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Crossword:
    def __init__(self, hxw, file, numBlocks, words) -> None:
        self.height = int(hxw.split("x")[0])
        self.width = int(hxw.split("x")[1])
        # Dictionary
        self.numBlocks = int(numBlocks)
        self.board = ["-"*self.width]*self.height
        for num in range(len(words)):
            words[num] = words[num].upper()
        for thing in words:
            match = re.search(r"^(h|v)(\d+)x(\d+)(.+)$", thing, re.I)
            direction = match.group(1)
            rowNum = int(match.group(2))
            colNum = int(match.group(3))
            letters = match.group(4)
            if direction == "H":
                row = list(self.board[rowNum])
                row[colNum:colNum+len(letters)] = letters
                row = "".join(row)
                self.board[rowNum] = row
            else:
                col = ""
                for thing in self.board:
                    col = col + thing[colNum]
                col = list(col)
                col[rowNum:rowNum+len(letters)] = letters
                for i in range(len(self.board)):
                    li = list(self.board[i])
                    li[colNum] = col.pop(0)
                    self.board[i] = "".join(li)

    def transpose(self, xw, newWidth):
        lst = self.board
        transposed_lst = [''.join(row) for row in zip(*lst)]
        return transposed_lst
    def transpose2(self, xw, newWidth):
        lst = xw
        transposed_lst = [''.join(row) for row in zip(*lst)]
        return transposed_lst

    def addBorder(self):
        xword = "".join(self.board)
        xw = BLOCKCHAR * (self.width + 3)
        xw += (BLOCKCHAR * 2).join([xword[p: p + self.width] for p in range(0, len(xword), self.width)])
        xw += BLOCKCHAR * (self.width + 3)
        self.board = self.convertStringToList(xw, self.width+2)

    def removeBorder(self):
        sBoard = ["-"*self.width]*self.height
        for i in range(self.height):
            sBoard[i] = self.board[i+1][1: self.width + 1]
        self.board = sBoard

    def cleanBoard(self):
        #self.removeBorder()
        boardCopy = [i for i in self.copyboard]
        for i in range(len(boardCopy)):
            str = boardCopy[i]
            str = str.replace("~", "-")
            boardCopy[i] = str
        return boardCopy

    def displayBoard(self):
        self.copyboard = self.board[1:len(self.board)-1]
        height = self.height
        tempBoard = self.cleanBoard()
        for i in range(height):
            str = tempBoard[i]
            str = str[1 : len(str)-1]
            print(str)

    def convertStringToList(self, str, n):
        if str == None:
            return []
        # Initialize an empty list to hold the substrings
        substrings = []
        # Loop through the string, incrementing by n each time
        for i in range(0, len(str), n):
            # Get the substring of length n starting at index i
            substring = str[i:i+n]
            substrings.append(substring)
        return substrings

    def makePalindrome(self):
        str = "".join(self.board)
        l = len(str)
        for i in range(len(str)):
            char = str[i]
            if char == BLOCKCHAR:
                str = list(str)
                if (str[l-i-1]) == OPENCHAR:
                    str[(l-i)-1] = BLOCKCHAR
                str = "".join(str)
            elif char != OPENCHAR:
                str = list(str)
                if (str[l-i-1]) == OPENCHAR:
                    str[(l-i)-1] = PROTECTEDCHAR
                str = "".join(str)
        str = self.convertStringToList(str, self.width+2)
        self.board = str

    def checkProtected(self, char):
        if char != OPENCHAR and char != BLOCKCHAR:
            return True
        return False

    def getBoard(self):
        return self.board

    def addProtected(self):
        for i in range(len(self.board)):
            self.board[i] = re.sub(r'(?<=(#(\w|~)))--', r"~~", self.board[i])
            self.board[i] = re.sub(r'(?<=(#(\w|~)(\w|~)))-', r"~", self.board[i])

            self.board[i] = re.sub(r'-(?<=((\w|~)(\w|~)#))', r"~", self.board[i])
            self.board[i] = re.sub(r'--(?<=((\w|~)#))', r"~~", self.board[i])
        self.board = self.transpose("".join(self.board), len(self.board))
        for i in range(len(self.board)):
            self.board[i] = re.sub(r'(?<=(#(\w|~)))--', r"~~", self.board[i])
            self.board[i] = re.sub(r'(?<=(#(\w|~)(\w|~)))-', r"~", self.board[i])

            self.board[i] = re.sub(r'-(?<=((\w|~)(\w|~)#))', r"~", self.board[i])
            self.board[i] = re.sub(r'--(?<=((\w|~)#))', r"~~", self.board[i])
        self.board = self.transpose("".join(self.board), len(self.board))

    def addObviousBlocks(self):
        for y in range(len(self.board)):
            self.board[y] = re.sub(r"(?<=#)(--)(?=#)", r"##", self.board[y])
            self.board[y] = re.sub(r"(?<=#)(-)(?=#)", r"#", self.board[y])
        self.board = self.transpose("".join(self.board), len(self.board))
        for x in range(len(self.board)):
            self.board[x] = re.sub(r"(?<=#)(--)(?=#)", r"##", self.board[x])
            self.board[x] = re.sub(r"(?<=#)(-)(?=#)", r"#", self.board[x])
        self.board = self.transpose("".join(self.board), len(self.board))

    def addObviousBlocks2(self, board):
        for y in range(len(board)):
            board[y] = re.sub(r"(?<=#)(--)(?=#)", r"##", board[y])
            board[y] = re.sub(r"(?<=#)(-)(?=#)", r"#", board[y])
        board = self.transpose2("".join(board), len(board))
        for x in range(len(board)):
            board[x] = re.sub(r"(?<=#)(--)(?=#)", r"##", board[x])
            board[x] = re.sub(r"(?<=#)(-)(?=#)", r"#", board[x])
        board = self.transpose2("".join(board), len(board))
        return board
    
    def addAllBlocks(self):
        blocks = self.numBlocks
        posList = []
        boardCopy = [i for i in self.board]
        bc = "".join(boardCopy)
        board = "".join(self.board)
        for i in range(len(board)):
            if board[i] == OPENCHAR:
                posList.append(i)
        board = self.addHelper(board, blocks, posList)
        self.board = self.convertStringToList(board, self.width+2)
        while self.countBlocksPlaced() != blocks or self.finalCheck() == False or self.checkConnected(board) == False:
            board = bc
            self.board = boardCopy
            board = self.addHelper(board, blocks, posList)
            self.board = self.convertStringToList(board, self.width+2)

    def finalCheck(self):
        board = self.board
        regex = r'#(\w|~|-)#'
        regex2 = r'#(\w|~|-)(\w|~|-)#'
        for line in board:
            if re.search(regex, line) != None or re.search(regex2, line) != None:
                return False
        b = self.transpose("mumbo", "jumbo")
        for line in b:
            if re.search(regex, line) != None or re.search(regex2, line) != None:
                return False
        return True


    # def area_fill(self, board, sp):
    #     dirs = [-1, self.width, 1, -1*self.width]
    #     if sp < 0 or sp >= len(board): return board
    #     if board[sp] in {OPENCHAR, PROTECTEDCHAR}:
    #         board = board[0:sp] + '?' + board[sp+1:]
    #         for d in dirs:
    #             if d == -1 and sp % self.width == 0: continue #left edge
    #             if d == 1 and sp+1 % self.width == 0: continue #right edge
    #             board = self.area_fill(board, sp+d)
    #     return board

    def area_fill(self, board, r, c):
        if r<0 or r>=len(board) or c<0 or c>=len(board[0]) or board[r][c] == "#" or board[r][c] == "?":
            return board
        if(board[r][c]!="#"):
            board[r][c] = "?"
            self.area_fill(board, r+1, c)
            self.area_fill(board, r-1, c)
            self.area_fill(board, r, c+1)
            self.area_fill(board, r, c-1)
            return board 

    def checkConnected(self, board):
        sp = -1
        for i in range(len(board)):
            if board[i] != BLOCKCHAR:
                sp = i
                break
        if sp == -1:
            return True
        board = list(board)
        for i in range(len(board)):
            char = board[i]
            if char != PROTECTEDCHAR and char != BLOCKCHAR and char != OPENCHAR:
                board[i] = PROTECTEDCHAR
        board = "".join(board)
        board = self.convertStringToList(board, self.width+2)
        board = board[1:len(board)-1]
        for i in range(len(board)):
            board[i] = board[i][1:len(board[i])-1]
        #board = "".join(board)
        print()
        x = self.area_fill(board, sp)
        x = "".join(x)
        x = self.convertStringToList(x, self.width)
        for line in x:
            print(line)
        print()
        x = "".join(x)
        for char in x:
            if char == PROTECTEDCHAR or char == OPENCHAR:
                return False
        return True


    def addHelper(self, board, numBlocks, posList):
        # for i in range(len(board)):
        #     if board[i] == OPENCHAR and i in posList:
        #         positions.append(i)
        currNumBlocks = self.countBlocksPlaced()
        if currNumBlocks >= numBlocks:
            return "".join(self.board)
        if len(posList) == 0:
            return "".join(self.board)
        board = "".join(self.board)
        for option in posList:
            #randPos = random.choice(posList)
            #randPos = posList.pop(0)
            randPos = random.choice(posList)
            # posList.remove(randPos)
            # randPos = posList.pop(0)
            if self.isValid(board, randPos):
                board = board[0:randPos] + BLOCKCHAR + board[randPos+1:]
                self.board = self.convertStringToList(board, self.width+2)
                self.addObviousBlocks()
                self.makePalindrome()
                result = self.addHelper(board,numBlocks, posList)
                if result!= None:
                    return result
            #return self.addHelper(board, numBlocks, posList)``
        return None
    
    def countBlocksPlaced(self):
        str = "".join(self.board)
        count = str.count(BLOCKCHAR)
        count = count - (2*self.height)
        count = count - (2*(self.width+2))
        return count

    def isValid(self, board, option):
        boardCopy = board[::]
        boardCopy = boardCopy[:option] + BLOCKCHAR + boardCopy[option+1:]
        
        tempBoard = boardCopy[:]
        tempBoard = list(tempBoard)
        for i in range(len(tempBoard)):
            if tempBoard[i] != "#" and tempBoard[i] != "-":
                tempBoard[i] = "~"
        tempBoard = "".join(tempBoard)
        # if self.checkConnect(tempBoard) == False:
        #     return False
        b = self.convertStringToList(boardCopy, self.width+2)
        regex = r'#(\w|~)#'
        regex2 = r'#(\w|~)(\w|~)#'
        for line in b:
            if re.search(regex, line) != None or re.search(regex2, line) != None:
                return False
        b = self.transpose("mumbo", "jumbo")
        for line in b:
            if re.search(regex, line) != None or re.search(regex2, line) != None:
                return False
        return True
    

def main():
    input = args
    intTest = [r"^(\d+)x(\d+)$", r"^\d+$", r"^(H|V)(\d+)x(\d+)(.+)$"]

    hxw = "0x0"
    file = ""
    blocks = "0"
    words = []
    for thing in input:
        thing = thing.lower()
        if re.search(r"^(\d+)x(\d+)$", thing):
            hxw = thing
        if re.search(r"^\d+$", thing):
            blocks = thing
        if re.search(r"^(h|v)(\d+)x(\d+)(.+)$", thing):
            words.append(thing)
    crossword = Crossword(hxw, "", blocks, words)
    
    crossword.addBorder()
    
    crossword.addObviousBlocks()
    
    crossword.addProtected()

    crossword.makePalindrome()

    crossword.addAllBlocks()

    crossword.displayBoard()


'''
I---TRIP-CALF
N-----------O
S-----------O
T-----------T
E-------#####
P----T---####
###-NO#ON-###
####-N-------
#####--------
-------------
-------------
-------------
-------------
'''

main()

# Pranav Elavarthi, 5, 2024