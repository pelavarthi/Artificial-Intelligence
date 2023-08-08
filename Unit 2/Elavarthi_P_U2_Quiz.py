# Name: Pranav Elavarthi
import random

def solve(line):
   assignment = formatInput(line)
   i = recurSolve(assignment)
   return i

def formatInput(line):
   line = line.split()
   line = "".join(line)
   line = list(line)
   numTerms = int(line[0])
   del line[0]
   assignment = ["."]*(9)
   for i in range(len(line)):
      if i % 2 == 0:
         var = int(line[i])
         var = var-1
         assignment[var] = line[i+1]
   return "".join(assignment)

def recurSolve(assignment):
   if check_complete(assignment):
      return assignment
   cur = select_unassigned_var(assignment)
   for test in "ABC":
      if isValid(test, cur, assignment):
         assignment = assignment[:cur] + str(test) + assignment[cur+1:]
         temp = recurSolve(assignment)
         if temp != None: return temp
         assignment = assignment[:cur] + '.' + assignment[cur+1:]
   return None

def check_complete(assignment):
   for letter in assignment:
      if letter == ".":
         return False
   return True
   
def select_unassigned_var(assignment):
   """ your code goes here """
   li = []
   for i in range(9):
      if assignment[i] == ".":
         li.append(i)
   return random.choice(li)
   
def isValid(value, var_index, assignment):
   # check each row for duplicates
   test = assignment[::]
   test = list(test)
   test[var_index] = value
   test = "".join(test)
   r1 = list(test[0:3])
   if (r1.count("A") > 1 or r1.count("B") > 1 or r1.count("C") > 1):
      return False
   r2 = list(test[3:6])
   if (r2.count("A") > 1 or r2.count("B") > 1 or r2.count("C") > 1):
      return False
   r3 = list(test[6:9])
   if (r3.count("A") > 1 or r3.count("B") > 1 or r3.count("C") > 1):
      return False

   # check each column for duplicates
   c1 = list(test[0]+test[3]+test[6])
   if (c1.count("A") > 1 or c1.count("B") > 1 or c1.count("C") > 1):
      return False
   c2 = list(test[1]+test[4]+test[7])
   if (c2.count("A") > 1 or c2.count("B") > 1 or c2.count("C") > 1):
      return False
   c3 = list(test[2]+test[5]+test[8])
   if (c3.count("A") > 1 or c3.count("B") > 1 or c3.count("C") > 1):
      return False
   return True

print(solve("3 1 A 3 C 8 A"))
