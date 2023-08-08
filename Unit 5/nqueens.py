import random
import sys
input = sys.argv[1:]
print(input)

def newBoard(n):
    board = [0] * len(range(1,n+1))
    positions = list(range(1, n+1))
    for i in range(len(board)):
        choice = random.choice(positions)
        board[i] = choice
        positions.remove(choice)
    return board

def display(board):
    for r in range(1, len(board)+1):
        fin = ""
        for c in range(0, len(board)):
            if board[c] == r:
                fin += "Q "
            else:
                fin += ". "
        print(fin)

def mutate(board):
    rand = random.randint(1, len(board))
    randPos = random.randint(0, len(board)-1)
    board[randPos] = rand

def countConflicts(board):
    n = len(board)
    conflicts = 0
    for x in range(0, n):
        num = board[x]
        for z in range(x+1, n):
            num2 = board[z]
            if abs(num-num2) == z-x:
                conflicts += 1
                break
    return conflicts

# For backtracking: board does not have to be full to be "valid"
def valid(cfg):
    n = len(cfg)
    for i in range(n):
        for j in range(n):
            if i != j and abs(i-j) == abs(cfg[i]-cfg[j]):
                return False
    return True



# need to implement mutations
def babyBoard(n, board1, board2):
    pivot = int(n*0.5) # change coefficient
    part1 = board1[0:pivot]
    part2 = [x for x in board2 if x not in part1]
    return part1 + part2

# Conflict distribution stats, stats = True or False
# Setting stats = True causes a considerable slowdown.
def checkSolution(n, pool, gen, stats):
    if stats:
        dist = [len([t for t in pool if countConflicts(t) == m]) for m in range(n)]
        print("Gen", gen, dist)
        print("Conflicts", countConflicts(gen))
        if dist[0] > 0:
            return min(pool, key=lambda b:countConflicts(b))

    return None
def genetic(n, pop):
    if n < 4:
        print()
        print("NOT POSSIBLE")
        print()
        return []
    pool = [newBoard(n) for b in range(pop)]
    gen = 0
    while True:
        s = checkSolution(n, pool, gen, True)
        if s:
            return s
        gen += 1
        newpool = []
        while len(pool) > 0:
            t1 = pool.pop()
            t2 = pool.pop()
            newpool.append(t1)
            newpool.append(t2)
            child = babyBoard(n, t1, t2)
            while child in newpool:
                mutate(child)
            newpool.append(child)
        newpool.sort(key=lambda board:countConflicts(board))
        pool = newpool[:pop]
        random.shuffle(pool)
        

if (len(input) != 2):
    print()
    print("BAD INPUT")
    print()
else:
    numQueens = int(input[0])
    populationSize = int(input[1])
    result = genetic(numQueens,populationSize)
    display(result)