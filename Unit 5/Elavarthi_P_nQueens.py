import sys
import random
input = sys.argv[1:]

# Returns best solution otherwise nothing
def checkSolution(n, pool):
    dist = [len([t for t in pool if fitness(t) == m]) for m in range(n)]
    if dist[0] > 0:
        return min(pool, key=lambda b:fitness(b))
    return None

# Generates a random new board
def newBoard(n):
    board = [0] * len(range(1,n+1))
    positions = list(range(1, n+1))
    for i in range(len(board)):
        choice = random.choice(positions)
        board[i] = choice
        positions.remove(choice)
    return board

# Prints out the board
def display(board):
    for row in range(1, len(board)+1):
        fin = ""
        for col in range(0, len(board)):
            if board[col] == row:
                fin += "Q"
            else:
                fin += "-"
        print(fin)

# Helper function for reproduce, splits the two parents and combines them
def crossover(n, b1, b2):
    splitIndex = random.randint(1,len(b1)-1)
    x = b1[:splitIndex]
    y = [i for i in b2 if i not in x]
    return x + y

# Reproduces with two parents and makes baby
def reproduce(n, board1, board2):
    board = crossover(n, board1, board2)
    mutate(board)
    return board

# Mutates the board by swapping two columns in the board
def mutate(board):
    a = random.randint(0, len(board)-1)
    b = random.randint(0, len(board)-1)
    temp = board[a]
    temp2 = board[b]
    board[a] = temp2
    board[b] = temp

# Counts the number of conflicts in the board (I'm not doing the max conflicts - conflicts)
def fitness(board):
    l = len(board)
    conflicts = 0
    for i in range(0, l):
        x = board[i]
        for j in range(i+1, l):
            y = board[j]
            if abs(x-y) == j-i:
                conflicts += 1
                break
    return conflicts

def geneticAlgorithm(queens, size):
    # Generates initial population
    pop = []
    for i in range(size):
        pop.append(newBoard(queens))
    
    while True:
        # Calculates solution and returns if it is viable
        bestSol = checkSolution(queens, pop)
        if bestSol != None:
            return bestSol
        
        nextGen = []
        while len(pop) > 0:
            # Takes two parents and makes child
            parent1 = pop.pop()
            parent2 = pop.pop()

            child = reproduce(queens, parent1, parent2)
            # Adds parents and child to the new generation
            nextGen.append(parent1)
            nextGen.append(parent2)
            nextGen.append(child)

        # Sorts and only takes the best boards
        nextGen.sort(key=lambda board:fitness(board))
        pop = nextGen[:size]

        # Shuffles the population each time
        temp = []
        for i in range(len(pop)):
            rand = random.choice(pop)
            temp.append(rand)
            pop.remove(rand)
        pop = temp[:]

# Checks for bad input
if len(input) != 2:
    print()
    print("BAD INPUT")
    print()
else:
    # Runs genetic algorithm
    child = geneticAlgorithm(int(input[0]), int(input[1]))
    display(child)