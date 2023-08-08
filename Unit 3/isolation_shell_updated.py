# Name: Austin Thomas
# Date: 12/8/2022
import random

class RandomPlayer:
   def __init__(self):
      self.white = "#ffffff" #"O"
      self.black = "#000000" #"X"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = 5
      self.y_max = 5
      self.first_turn = True
      
   def best_strategy(self, board, color):
      # Terminal test: when there's no more possible move
      #                return (-1, -1), 0
      # returns best move
      # (column num, row num), 0
      moveset = self.find_moves(board, color)
      if moveset == set():
         return (-1, -1), 0
      else:
         choice = random.choice(list(moveset))
         return (choice//5, choice%5), 0
      
     
   def find_moves(self, board, color):
      # finds all possible moves
      # returns a set, e.g., {0, 1, 2, 3, ...., 24} 
      # 0 5 10 15 20
      # 1 6 11 16 21
      # 2 7 12 17 22
      # 3 8 13 18 23
      # 4 9 14 19 24
      # if 2 has 'X', board = [['.', '.', 'X', '.', '.'], [col 2], .... ]
      moves_found = set()
      for i in range(len(board)):
         for j in range(len(board[i])):
               if self.first_turn and board[i][j] == '.': 
                  moves_found.add(i*self.y_max+j)
                  self.first_turn = False
               elif (color == self.black and board[i][j] == 'X') or (color == self.white and board[i][j] == 'O'):
                  for incr in self.directions:
                     x_pos = i + incr[0]
                     y_pos = j + incr[1]
                     stop = False
                     while 0 <= x_pos < self.x_max and 0 <= y_pos < self.y_max:
                           if board[x_pos][y_pos] != '.':
                              stop = True
                           if not stop:    
                              moves_found.add(x_pos*self.y_max+y_pos)
                           x_pos += incr[0]
                           y_pos += incr[1]
      return moves_found

class CustomPlayer:

   def __init__(self):
      self.white = "#ffffff" #"O"
      self.black = "#000000" #"X"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = 5
      self.y_max = 5
      self.first_turn = True

   def best_strategy(self, board, color):
      # returns best move
      return self.minimax(board, color, 3)

   def minimax(self, board, color, search_depth):
      # search_depth: start from 3
      # returns best "value"
      max_val = self.maxval(board, color, search_depth)
      print(max_val)
      return max_val
      
            
   def minval(self, board, color, search_depth):
      min_val = 99999999999999
      state = ()
      for move in self.find_moves(board, color):
         board = self.make_move(board, color, move)
         if self.evaluate(board, color, self.find_moves(board, color)) == -1:
            return move, -1
         else:
            if search_depth != 0:
               search_depth -= 1
               state, value = self.maxval(board, self.opposite_color[color], search_depth)
               if value < min_val:
                  min_val = value
                  state = move
      return state, min_val

   def maxval(self, board, color, search_depth):
      max_val = -99999999999999
      state = ()
      for move in self.find_moves(board, color):
         board = self.make_move(board, color, move)
         if self.evaluate(board, color, self.find_moves(board, color)) == 1:
            return move, 1
         else:
            if search_depth != 0:
               search_depth -= 1
               state, value = self.minval(board, self.opposite_color[color], search_depth)
               if value > max_val:
                  max_val = value
                  state = move
      return state, max_val
   
   def negamax(self, board, color, search_depth):
      # returns best "value"
      return 1
      
   def alphabeta(self, board, color, search_depth, alpha, beta):
      # returns best "value" while also pruning
      pass

   def make_move(self, board, color, move):
      # returns board that has been updated
      if color == self.white:
         board[move[0]][move[1]] = 'O'
      else:
         board[move[0]][move[1]] = 'X'
      return board

   def evaluate(self, board, color, possible_moves):
      # returns the utility value
      # count possible_moves (len(possible_moves)) of my turn at current board
      # opponent's possible_moves: self.find_moves(board, self.opposite_color(color))
      my_moveset = self.find_moves(board, color)
      opp_moveset = self.find_moves(board, self.opposite_color[color])
      if my_moveset == set():
         return -1
      elif opp_moveset == set():
         return 1
      else:
         return len(my_moveset) - len(opp_moveset)

   def find_moves(self, board, color):
      moves_found = set()
      for i in range(len(board)):
         for j in range(len(board[i])):
               if self.first_turn and board[i][j] == '.': 
                  index = i*self.y_max+j
                  moves_found.add((index//5, index%5))
                  self.first_turn = False
               elif (color == self.black and board[i][j] == 'X') or (color == self.white and board[i][j] == 'O'):
                  for incr in self.directions:
                     x_pos = i + incr[0]
                     y_pos = j + incr[1]
                     stop = False
                     while 0 <= x_pos < self.x_max and 0 <= y_pos < self.y_max:
                           if board[x_pos][y_pos] != '.':
                              stop = True
                           if not stop:    
                              index = x_pos*self.y_max+y_pos
                              moves_found.add((index//5, index%5))
                           x_pos += incr[0]
                           y_pos += incr[1]
      return moves_found