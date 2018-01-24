
theBoard = {'topleft': ' ', 'topmid': ' ', 'topright': ' ',
            'midleft': ' ', 'midmid': ' ', 'midright': ' ',
            'lowleft': ' ', 'lowmid': ' ', 'lowright': ' '}

def printBoard(board):
    print(board['topleft'] + " | " + board['topmid'] + ' | ' + board['topright'])
    print("__+___+__")
    print(board['midleft'] + " | " + board['midmid'] + ' | ' + board['midright'])
    print("__+___+__")
    print(board['lowleft'] + " | " + board['lowmid'] + ' | ' + board['lowright'])

printBoard(theBoard)