# Name: Pranav Elavarthi
# Date: 1/2/2023

import random

class RandomBot:
	def __init__(self):
		self.logging = True
		self.white = "#ffffff" # "O"
		self.black = "#000000" # "@"
		self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
		self.opposite_color = {self.black: self.white, self.white: self.black}
		self.x_max = None
		self.y_max = None
		self.color = None

	def get_search_depth(self, stones):
		if stones > 32:
			return 5
		elif stones > 10:
			return 7
		else:
			return 9

	def get_coords(self, move):
		row = move // self.x_max
		col = move % self.y_max
		return (row, col)

	def best_strategy(self, board, color):
		self.x_max = len(board)
		self.y_max = len(board[0])
		self.color = color
		stones_left = self.stones_left(board)
		depth = self.get_search_depth(stones_left)
		moves = self.find_moves(board, color).keys()
		if 0 in moves:
			return (0,0), 0
		if 7 in moves:
			return (0, 7), 0
		if 56 in moves:
			return (7, 0), 0
		if 63 in moves:
			return (7,7), 0
		val, move = self.alphabeta(board, color, search_depth = depth, alpha = -9999999999, beta = 9999999999)   # returns state
		return self.get_coords(move), 0

	def minimax(self, board, color, search_depth):
		# returns best "value"
		return 1

	def negamax(self, board, color, search_depth):
	 # returns best "value"
		return 1
		
	def alphabeta(self, board, color, search_depth, alpha, beta, last_move=-1):
		ok = self.terminal_test(board, color)
		if search_depth <= 0 or ok:
			cur_eval = self.evaluate(board, self.color, self.find_moves(board, color))
			return cur_eval, last_move if ok else 0

		if search_depth % 2 == 1:
			min_val = float('inf')
			result = 0
			for move, flipped in self.find_moves(board, color).items():
				cur_val, _ = self.alphabeta(self.make_move(board, color, move, flipped), 
			self.opposite_color[color], search_depth - 1, alpha, beta)
				if cur_val < min_val:
					min_val = cur_val
					result = move
				if min_val < alpha:
					return min_val, result
				beta = min(beta, min_val)
			return min_val, result
		else:
			max_val = float('-inf')
			result = 0
			for move, flipped in self.find_moves(board, color).items():
				cur_val, _ = self.alphabeta(self.make_move(board, color, move, flipped), 
				self.opposite_color[color], search_depth - 1, alpha, beta)
				if cur_val > max_val:
					max_val = cur_val
					result = move
				if max_val > beta:
					return max_val, result
				alpha = max(alpha, max_val)
			return max_val, result

	def terminal_test(self, board, color):
		stones = self.stones_left(board)
		if stones == 0 or len(self.find_moves(board, color)) == 0:
			return True
		else:
			return False

	def stones_left(self, board):
		ans = 0
		for row in board:
			ans += row.count('.')
		return ans

	def make_move(self, board, color, move, flipped):
		cur_board = [row[:] for row in board]
		if color == self.black:
			color = "@"
		else:
			color = "O"
		r, c = self.get_coords(move)
		cur_board[r][c] = color
		for x, y in flipped:
			cur_board[x][y] = color
		return cur_board

	def evaluate(self, board, color, possible_moves):
		return len(possible_moves) - (0.5 * len(self.find_moves(board, self.opposite_color[color])))

	def score(self, board, color):
		if color == self.black:
			color = "@"
		else:
			color = "O"
		score = 0
		for i in range(len(board)):
			for j in range(len(board[i])):
				if board[i][j] == color:
					score += 1
				if board[i][j] != color and board[i][j] != '.':
					score -= 1
		return score

	def find_moves(self, my_board, my_color):
		moves_found = {}
		for i in range(len(my_board)):
			for j in range(len(my_board[i])):
					flipped_stones = self.find_flipped(my_board, i, j, my_color)
					if len(flipped_stones) > 0:
						moves_found.update({i*self.y_max+j: flipped_stones})
		return moves_found

	def find_flipped(self, my_board, x, y, my_color):
		if my_board[x][y] != ".":
			return []
		if my_color == self.black:
			my_color = "@"
		else:
			my_color = "O"
		flipped_stones = []
		for incr in self.directions:
			temp_flip = []
			x_pos = x + incr[0]
			y_pos = y + incr[1]
			while 0 <= x_pos < self.x_max and 0 <= y_pos < self.y_max:
					if my_board[x_pos][y_pos] == ".":
						break
					if my_board[x_pos][y_pos] == my_color:
						flipped_stones += temp_flip
						break
					temp_flip.append([x_pos, y_pos])
					x_pos += incr[0]
					y_pos += incr[1]
		return flipped_stones

class Best_AI_bot:
	def __init__(self):
		self.logging = True
		self.white = "#ffffff" # "O"
		self.black = "#000000" # "@"
		self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
		self.opposite_color = {self.black: self.white, self.white: self.black}
		self.x_max = None
		self.y_max = None
		self.color = None

	def get_search_depth(self, stones):
		if stones > 32:
			return 5
		elif stones > 10:
			return 7
		else:
			return 9

	def get_coords(self, move):
		row = move // self.x_max
		col = move % self.y_max
		return (row, col)

	def best_strategy(self, board, color):
		self.x_max = len(board)
		self.y_max = len(board[0])
		self.color = color
		stones_left = self.stones_left(board)
		depth = self.get_search_depth(stones_left)
		move = self.alphabeta(board, color, search_depth = depth, alpha = -9999999999, beta = 9999999999)[1]   # returns state
		return self.get_coords(move), 0

	def terminal(self, board, color, last_move):
		cur_eval = self.evaluate(board, self.color, self.find_moves(board, color))
		if self.stones_left(board)==0 or len(self.find_moves(board,color))==0:
			return cur_eval, last_move
		else:
			return cur_eval, 0

	def max_alpha_beta(self, board,color, search_depth, alpha, beta):
		m = -9999999999
		fin = 0
		for move, flipped in self.find_moves(board, color).items():
			cm = self.make_move(board, color, move, flipped)
			cc = self.opposite_color[color]
			cv = self.alphabeta(cm, cc, search_depth - 1, alpha, beta, cm)[0]
			if cv > m:
				m = cv
				fin = move
			if m > beta:
				return m, fin
			alpha = max(alpha, m)
		return m, fin

	def min_alpha_beta(self, board, color, search_depth, alpha, beta):
		m = 9999999999
		fin = 0
		for move, flipped in self.find_moves(board, color).items():
			cm = self.make_move(board, color, move, flipped)
			cc = self.opposite_color[color]
			cv = self.alphabeta(cm, cc, search_depth - 1, alpha, beta, cm)[0]
			if cv < m:
				m = cv
				fin = move
			if m < alpha:
				return m, fin
			beta = min(beta, m)
		return m, fin

	def alphabeta(self, board, color, search_depth, alpha, beta, last_move=-1):
		if search_depth <= 0 or self.stones_left(board)==0 or len(self.find_moves(board,color))==0:
			return self.terminal(board,color,last_move)
		if search_depth % 2 == 1:
			return self.min_alpha_beta(board, color, search_depth, alpha, beta)
		else:
			return self.max_alpha_beta(board, color, search_depth, alpha, beta)

	def stones_left(self, board):
		ans = 0
		for row in board:
			ans += row.count('.')
		return ans

	def make_move(self, board, color, move, flipped):
		nb = [row[:] for row in board]
		if color == self.black:
			color = "@"
		else:
			color = "O"
		r, c = self.get_coords(move)
		nb[r][c] = color
		for x, y in flipped:
			nb[x][y] = color
		return nb

	def evaluate(self, board, color, possible_moves):
		me = len(possible_moves)
		other = 0.5 * len(self.find_moves(board,self.opposite_color[color]))
		return me - other

	def find_moves(self, my_board, my_color):
		moves_found = {}
		for i in range(len(my_board)):
			for j in range(len(my_board[i])):
					flipped_stones = self.find_flipped(my_board, i, j, my_color)
					if len(flipped_stones) > 0:
						moves_found.update({i*self.y_max+j: flipped_stones})
		return moves_found

	def find_flipped(self, board, x, y, color):
		if board[x][y] != ".":
			return []
		if color == self.black:
			my_color = "@"
		else:
			my_color = "O"
		flipped_stones = []
		for incr in self.directions:
			temp_flip = []
			x_pos = x + incr[0]
			y_pos = y + incr[1]
			while 0 <= x_pos < self.x_max and 0 <= y_pos < self.y_max:
				if board[x_pos][y_pos] == ".":
					break
				if board[x_pos][y_pos] == my_color:
					flipped_stones += temp_flip
					break
				temp_flip.append([x_pos, y_pos])
				x_pos += incr[0]
				y_pos += incr[1]
		return flipped_stones
