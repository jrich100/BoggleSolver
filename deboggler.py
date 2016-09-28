#!/usr/bin/env python

"""Deboggler.py: Solution to the Idea Evolver coding challenge 2016"""

from sys import stdin

dictionary = set(open("dictionary.txt"))

prefixes = set()
for word in dictionary:
	[prefixes.add(word[:i]) for i in xrange(len(word)+1)]

def solve(board_input):
	global board, rows, cols

	board = [line for line in board_input if line]
	if not validate(board): return []

	rows, cols = len(board),len(board[0])

	#start dfs on each letter
	solution = []
	for i, row in enumerate(board):
		for j, start in enumerate(row):
			solution += find_words(start, [(i,j)])

	return sorted(set(solution))

def validate(board):
	return (3 <= len(board) <= 100 and 
			3 <= len(board[0]) <= 100 and
			all(row.isalpha() for row in board))

def find_words(prefix, used):
	found = []

	if prefix not in prefixes:
		return found

	if (len(prefix) >= 3 and prefix+"\n" in dictionary):
		found.append(prefix)

	pos = used[-1]
	for dy in xrange(-1, 2):
		for dx in xrange(-1, 2):
			next = (pos[0]+dy, pos[1]+dx)
			if (0 <= next[0] < rows and
				0 <= next[1] < cols and 
				next not in used):

				found += find_words(prefix + board[next[0]][next[1]], used + [next])

	return found

if __name__ == '__main__':
	board_input = [line.rstrip('\n').lower() for line in stdin]

	for word in solve(board_input):
		print word