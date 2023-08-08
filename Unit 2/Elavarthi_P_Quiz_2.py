import random

neighbors = {0:{1,10,19}, 1:{0,2,8}, 2:{1,3,6}, 3:{2,4,19}, 4:{3,5,17}, 5:{4,6,15}, 6:{2,5,7}, 7:{6,8,14}, 8:{1,7,9}, 9:{8,10,13},10:{0,9,11},11:{10,12,18},12:{11,13,16},13:{9,12,14},14:{7,13,15},15:{5,14,16},16:{12,15,17},17:{4,16,18},18:{11,17,19},19:{0,3,18}}

def check_complete(assignment, csp_table):
   for thing in assignment:
    if thing == ".":
        return False
   return True

def select_unassigned_var(assignment, csp_table):
   li = []
   for i in range(20):
      if assignment[i] == ".":
         li.append(i)
   return random.choice(li)
   
def isValid(value, var_index, assignment, neighbors):
   adjacents = neighbors[var_index]
   for thing in adjacents:
    if assignment[thing] == value:
        return False
   return True

def backtracking_search(input, csp_table): 
   return recursive_backtracking(input, csp_table)

def countChars(assignment):
    count = 0
    for char in assignment:
        if char != ".":
            count += 1
    return count

def recursive_backtracking(assignment, csp_table):
   if check_complete(assignment,csp_table):
      return assignment
   cur = select_unassigned_var(assignment, csp_table)
   for test in "ABC":
        if isValid(test, cur, assignment, csp_table):
            print(assignment, countChars(assignment))
            assignment = assignment[:cur] + str(test) + assignment[cur+1:]
            temp = recursive_backtracking(assignment, csp_table)
            if temp != None: return temp
            assignment = assignment[:cur] + '.' + assignment[cur+1:]
   return None


solution = backtracking_search(input("20-char(. and 1-6) input: "), neighbors)
if solution != None:
    print (solution)
    print (check_complete(solution, neighbors))
else: print ("It's not solvable.")
