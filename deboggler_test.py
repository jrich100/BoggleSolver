#!/usr/bin/env python

from deboggler import solve
import os

board_fns = [fn for fn in os.listdir("boards/")]
boards = [[line.rstrip('\n').lower() for line in open("boards/"+fn,'r')] for fn in board_fns]

solutions = [[line.rstrip('\n').lower() for line in open("solutions/"+fn,'r')] 
			  for fn in os.listdir("solutions/")]


if __name__ == '__main__':
	print "--- Testing Boggle Solver ---\n"
	
	tests = [solve(board) == solutions[i] for i, board in enumerate(boards)]

	for i, test in enumerate(tests):

		print 'Test {0}: {1} -- {2}\n'.format(i, board_fns[i], tests[i])

	print "--- Done ---"