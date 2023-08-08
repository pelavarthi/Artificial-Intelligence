# Name: Pranav Elavarthi

def check_complete(assignment, csp_table):
   for letter in assignment:
      if letter == ".":
         return False
   return True
   
def select_unassigned_var(assignment, variables, csp_table):
    if "." in assignment:
        return assignment.find(".")

def isValid(value, var_index, assignment, variables, csp_table):
    for i in range(len(csp_table)):
        a = csp_table[i]
        if var_index in a:
            for j in a:
                if j != var_index and assignment[j] == str(value):
                    return False   
    return True

def ordered_domain(var_index, assignment, variables, csp_table):
   return [1,2,3,4,5,6,7,8,9]

def update_variables(value, var_index, assignment, variables, csp_table):
   return None

def solve(puzzle):
   csp = sudoku_csp()
   return backtracking_search(puzzle, initial_variables(csp), csp)

def backtracking_search(puzzle, variables, csp_table): 
   return recursive_backtracking(puzzle, variables, csp_table)

def recursive_backtracking(assignment, variables, csp_table):
    if check_complete(assignment, csp_table):
        display(assignment)
        return assignment
    cur = select_unassigned_var(assignment, variables, csp_table)
    for test in range(1,10):
      if isValid(test, cur, assignment, variables, csp_table):
         assignment = assignment[:cur] + str(test) + assignment[cur+1:]
         temp = recursive_backtracking(assignment, variables, csp_table)
         if temp != None: return temp
         assignment = assignment[:cur] + '.' + assignment[cur+1:]
    return None


def display(solution):
   s = ""
   c = 0
   for j in range(9):
    i = j*9
    s += solution[i:i+3] + "\t"
    s += solution[i+3:i+6] + "\t"
    s += solution[i+6:i+9] + "\n"
    c+=1
    if c %3 == 0:
        s+="\n"
   return s

def sudoku_csp():
   return [[0, 1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16, 17],[18, 19, 20, 21, 22, 23, 24, 25, 26], [27, 28, 29, 30, 31, 32, 33, 34, 35],[36, 37, 38, 39, 40, 41, 42, 43, 44], [45, 46, 47, 48, 49, 50, 51, 52, 53],[54, 55, 56, 57, 58, 59, 60, 61, 62], [63, 64, 65, 66, 67, 68, 69, 70, 71],[72, 73, 74, 75, 76, 77, 78, 79, 80], [0, 9, 18, 27, 36, 45, 54, 63, 72],[1, 10, 19, 28, 37, 46, 55, 64, 73], [2, 11, 20, 29, 38, 47, 56, 65, 74],[3, 12, 21, 30, 39, 48, 57, 66, 75], [4, 13, 22, 31, 40, 49, 58, 67, 76],[5, 14, 23, 32, 41, 50, 59, 68, 77], [6, 15, 24, 33, 42, 51, 60, 69, 78],[7, 16, 25, 34, 43, 52, 61, 70, 79], [8, 17, 26, 35, 44, 53, 62, 71, 80],[0, 1, 2, 9, 10, 11, 18, 19, 20], [3, 4, 5, 12, 13, 14, 21, 22, 23],[6, 7, 8, 15, 16, 17, 24, 25, 26], [27, 28, 29, 36, 37, 38, 45, 46, 47],[30, 31, 32, 39, 40, 41, 48, 49, 50], [33, 34, 35, 42, 43, 44, 51, 52, 53],[54, 55, 56, 63, 64, 65, 72, 73, 74], [57, 58, 59, 66, 67, 68, 75, 76, 77],[60, 61, 62, 69, 70, 71, 78, 79, 80]]

def initial_variables(puzzle, csp_table):
   return {}
