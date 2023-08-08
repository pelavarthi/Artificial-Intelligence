# Name: Pranav Elavarthi       Date: 9/28/2022

class HeapPriorityQueue():
   def __init__(self):
      self.queue = ["dummy"]  # we do not use index 0 for easy index calulation
      self.current = 1        # to make this object iterable

   def next(self):            # define what _next_ does
      if self.current >=len(self.queue):
         self.current = 1     # to restart iteration later
         raise StopIteration
    
      out = self.queue[self.current]
      self.current += 1
   
      return out

   def __iter__(self):
      return self

   _next_ = next

   def isEmpty(self):
      return len(self.queue) == 1    # b/c index 0 is dummy

   def swap(self, a, b):
      self.queue[a], self.queue[b] = self.queue[b], self.queue[a]

   # Add a value to the heap_pq
   def push(self, value):
      self.queue.append(value)
      # write more code here to keep the min-heap property
      self.heapUp(len(self.queue) - 1)

   # helper method for push      
   def heapUp(self, k):
      parent = k // 2
      if(parent != 0 and self.queue[parent] > self.queue[k]):
         self.swap(k, parent)
         self.heapUp(parent)

   # helper method for reheap and pop
   def heapDown(self, k, size):
      left = k * 2
      right = k * 2 + 1
      if (left > size):
         return
      if (left == size):
         if (self.queue[k] > self.queue[left]):
            self.swap(k, left)
      else:
         min = left if (self.queue[left] <= self.queue[right]) else right
         if (self.queue[k] > self.queue[min]):
            self.swap(k, min)
            self.heapDown(min, size)
   
   # make the queue as a min-heap            
   def reheap(self):
      pq = HeapPriorityQueue()
      for val in self.queue:
         if val != "dummy":
            pq.push(val)
      self.queue = pq.queue
   
   # remove the min value (root of the heap)
   # return the removed value           
   def pop(self):
      return self.remove(1)
      
   # remove a value at the given index (assume index 0 is the root)
   # return the removed value   
   def remove(self, index):
      self.swap(index, len(self.queue)-1)
      temp = self.queue.pop()
      self.heapDown(index, len(self.queue)-1)
      return temp

def inversion_count(new_state, width = 4, N = 4):
   ''' 
   Depends on the size(width, N) of the puzzle, 
   we can decide if the puzzle is solvable or not by counting inversions.
   If N is odd, then puzzle instance is solvable if number of inversions is even in the input state.
   If N is even, puzzle instance is solvable if
      the blank is on an even row counting from the bottom (second-last, fourth-last, etc.) and number of inversions is even.
      the blank is on an odd row counting from the bottom (last, third-last, fifth-last, etc.) and number of inversions is odd.
   ''' 
   # Your code goes here
   inv_count = 0
   for i in range(N*width):
      for j in range(i + 1, N*width):
         if (new_state[i] != '_' and new_state[j] != '_' and new_state[i] > new_state[j]):
               inv_count += 1
   if N %2 ==1:
      return inv_count%2==0
   else:
      index = new_state.find("_")
      if (index//width %2 == 0 and inv_count %2 ==0):
         return True
      if (index//width %2 == 1 and inv_count %2 == 1):
         return True  
   return False
   
def swap(n, i, j):
   # Your code goes here
   state_arr = [*n]
   temp = state_arr[i]
   state_arr[i] = state_arr[j]
   state_arr[j] = temp
   return "".join(state_arr)
      
'''Generate a list which hold all children of the current state
   and return the list'''
def generate_children(state, size=4):
   children = []
   index = state.find('_')
   # Left
   if (index % 4 != 0):
      children.append(swap(state,index-1,index))
   # Right
   if (index % 4 != 3):
      children.append(swap(state,index,index+1))
   # Up
   if (index >= 4):
      children.append(swap(state, index-4, index))
   # Down
   if (index < 12):
      children.append(swap(state, index, index+4))
   return children


''' You can make multiple heuristic functions '''
def dist_heuristic(state, goal = "_123456789ABCDEF", size=4):
   # Your code goes here
   sum = 0
   for i in range(len(state)):
      r, c = i//size, i%size
      g = goal.find(state[i])
      g_r, g_c = g//size, g%size
      sum += abs(c-g_c) + abs(r-g_r)
   return sum



def solve(start, goal="_123456789ABCDEF", heuristic=dist_heuristic, size = 4):
   if start == goal: return []
   
   frontier = [HeapPriorityQueue()]
   frontier.append(HeapPriorityQueue())

   explored = [{start:[[], 0]}]
   explored.append({goal:[[], 0]})

   frontier[0].push((heuristic(start), start, [start]))
   frontier[1].push((heuristic(goal), goal, [goal]))
   i = 1

   while frontier[0].isEmpty() == False and frontier[1].isEmpty() == False:
      i = 1 - i
      state = frontier[i].pop()
      if state[1] in explored[1-i]:
         return state[2] + explored[1-i][state[1]][0][:-1][::-1]

      for a in generate_children(state[1]):
         c = len(state[2]) + 1
         if a not in explored[i] or c < explored[i][a][1]:
            path = state[2] + [a]
            if a not in explored[i]:
               explored[i][a] = [path, c]
            explored[i][a][1] = c
            if (i == 0):
               frontier[i].push((heuristic(a) + c, a, path))
            else:
               frontier[i].push((heuristic(a,start) + c, a, path))

   return None
