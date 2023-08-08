# Name: Pranav Elavarthi        Date: 9/30/22
import time

def generate_adjacents(current, words_set):
   ''' words_set is a set which has all words.
   By comparing current and words in the words_set,
   generate adjacents set of current and return it'''
   adj_set = set()
   # TODO 1: adjacents
   # Your code goes here
   for i in range(len(current)):
      for c in "abcdefghijklmnopqrstuvwxyz":
         if (current[:i] + c + current[i+1:] in words_set and (c!=current[i])):
            adj_set.add(current[:i]+c+current[i+1:])
   return adj_set

def check_adj(words_set):
   # This check method is written for words_6_longer.txt
   adj = generate_adjacents('listen', words_set)
   target =  {'listee', 'listel', 'litten', 'lister', 'listed'}
   return (adj == target)

def generate_path(current, explored):
   list = [current]
   count = 0
   while explored[current] != "s" and explored[current] != "g":       #assume the parent of root is "s"
      list.append(explored[current])
      current = explored[current]
      count += 1
   return (list[::-1], count+1)


def bi_bfs(start, goal, words_set):
   '''The idea of bi-directional search is to run two simultaneous searches--
   one forward from the initial state and the other backward from the goal--
   hoping that the two searches meet in the middle. 
   '''
   if start == goal: return []
   # TODO 2: Bi-directional BFS Search
   # Your code goes here
   explored = {start:"s"}
   q = [start]
   explored2 = {goal:"g"}
   q2 = [goal]
   while len(q) != 0 and len(q2) !=0:
      a = q.pop(0)
      b = q2.pop(0)

      for c in generate_adjacents(a, words_set):
            if (c not in explored):
                q.append(c)
                explored[c] = a
      for d in generate_adjacents(b, words_set):
         if (d not in explored2):
               q2.append(d)
               explored2[d] = b

      for thing in explored:
         if (thing in explored2):
            return generate_path(thing,explored)[0][0:-1] + generate_path(thing,explored2)[0][::-1]
   return None

def main():
   filename = input("Type the word file: ")
   words_set = set()
   file = open(filename, "r")
   for word in file.readlines():
      words_set.add(word.rstrip('\n'))
   #print ("Check generate_adjacents():", check_adj(words_set))
   initial = input("Type the starting word: ")
   goal = input("Type the goal word: ")
   cur_time = time.time()
   path = (bi_bfs(initial, goal, words_set))
   if path != None:
      print (path)
      print ("The number of steps: ", len(path))
      print ("Duration: ", time.time() - cur_time)
   else:
      print ("There's no path")
 
if __name__ == '__main__':
   main()

'''
Sample output 1
Type the word file: words.txt
Type the starting word: listen
Type the goal word: beaker
['listen', 'listed', 'fisted', 'fitted', 'fitter', 'bitter', 'better', 'beater', 'beaker']
The number of steps:  9
Duration: 0.0

Sample output 2
Type the word file: words_6_longer.txt
Type the starting word: listen
Type the goal word: beaker
['listen', 'lister', 'bister', 'bitter', 'better', 'beater', 'beaker']
The number of steps:  7
Duration: 0.000997304916381836

Sample output 3
Type the word file: words_6_longer.txt
Type the starting word: vaguer
Type the goal word: drifts
['vaguer', 'vagues', 'values', 'valves', 'calves', 'cauves', 'cruves', 'cruses', 'crusts', 'crufts', 'crafts', 'drafts', 'drifts']
The number of steps:  13
Duration: 0.0408782958984375

Sample output 4
Type the word file: words_6_longer.txt
Type the starting word: klatch
Type the goal word: giggle
['klatch', 'clatch', 'clutch', 'clunch', 'glunch', 'gaunch', 'paunch', 'paunce', 'pawnce', 'pawnee', 'pawned', 'panned', 'panged', 'ranged', 'ragged', 'raggee', 'raggle', 'gaggle', 'giggle']
The number of steps:  19
Duration:  0.0867915153503418
'''


