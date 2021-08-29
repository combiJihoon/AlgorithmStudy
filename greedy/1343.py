import sys

input = sys.stdin.readline
board = str(input()).strip()

board = board.replace('XXXX', 'AAAA')
board = board.replace('XX', 'BB')

if 'X' not in board:
    print(board)
else:
    print(-1)
