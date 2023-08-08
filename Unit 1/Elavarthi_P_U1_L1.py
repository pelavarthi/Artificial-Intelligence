import random, time

def getInitialState():
   x = "_12345678"
   l = list(x)
   random.shuffle(l)
   y = ''.join(l)
   return y
   
'''precondition: i<j
   swap characters at position i and j and return the new state'''
def swap(state, i, j):
   '''your code goes here'''
   return state[:i] + state[j] + state[i+1:j] + state[i] + state[j+1:]
   
'''Generate a list which hold all children of the current state
   and return the list'''
def generate_children(state):
   '''your code goes here'''
   children = []
   index = state.index("_")
   # Left
   if (index % 3 != 0):
      children.append(swap(state,index-1,index))
   # Right
   if (index % 3 != 2):
      children.append(swap(state,index,index+1))
   # Up
   if (index > 2):
      children.append(swap(state, index-3, index))
   # Down
   if (index < 6):
      children.append(swap(state, index, index+3))
   return children

def display_path(n, explored): #key: current, value: parent
   l = []
   while explored[n] != "s": #"s" is initial's parent
      l.append(n)
      n = explored[n]
   print ()
   l = l[::-1]
   for i in l:
      print (i[0:3], end = "   ")
   print ()
   for j in l:
      print (j[3:6], end = "   ")
   print()
   for k in l:
      print (k[6:9], end = "   ")
   return len(l)

'''Find the shortest path to the goal state "_12345678" and
   returns explored and an empty string or "No solution".
   You can make other helper methods, but you must use dictionary for explored.'''
def BFS(initial_state, goal = "_12345678"):
   explored = {initial_state: "s"}
   '''Your code goes here'''
   Q = [initial_state]
   while (len(Q) != 0):
      s = Q.pop(0)
      if (s == goal):
         return explored, ''
      else:
         for a in generate_children(s):
            if a not in explored:
               Q.append(a)
               explored[a] = s
   # goal test is passed? return explored, ""
   return explored, "No solution"

'''Find the path to the goal state "_12345678" and
   returns explored and an empty string or "No solution".
   You can make other helper methods, but you must use dictionary for explored.'''
def DFS(initial_state, goal = "_12345678"):
   explored = {initial_state: "s"}
   '''Your code goes here'''
   Q = [initial_state]
   while (len(Q) != 0):
      s = Q.pop()
      if (s == goal):
         return explored, ''
      else:
         for a in generate_children(s):
            if a not in explored:
               Q.append(a)
               explored[a] = s
   # goal test is passed? return explored, ""
   return explored, "No solution"


def main():
   initial = getInitialState()
   goal = "_12345678"
   # Fun of 8 puzzle
   #initial = "1234567_8"
   #initial = "14725836_"
   #initial = "12345678_"
   #initial = "84765231_"
   start = time.time()
   print ("BFS start with:\n", initial[0:3], "\n", initial[3:6], "\n", initial[6:], "\n")
   bfs_result = BFS(initial)
   print ("\n\nThe number of nodes explored:", len(bfs_result[0]))
   if bfs_result[1] != "No solution": 
      print ("\nThe shortest path length is :", display_path(goal, bfs_result[0]))
   print ("BFS duration:", time.time() - start)
   start = time.time()
   print ("\n\nDFS start with:\n", initial[0:3], "\n", initial[3:6], "\n", initial[6:], "\n")
   dfs_result = DFS(initial)
   print ("\n\nThe number of nodes explored:", len(dfs_result[0])) 
   if dfs_result[1] != "No solution":
      print ("\nThe path length is :", display_path(goal, dfs_result[0]))
   print ("DFS duration:", time.time() - start) 

if __name__ == '__main__':
   main()
