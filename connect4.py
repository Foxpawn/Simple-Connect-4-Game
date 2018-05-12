'''Eric Zhen'''
''' I pledge my honor that I have abided by the Stevens honor System'''

class Board:
    def __init__ ( self,width = 7,height = 6 ):
        '''constructor for board'''
        self.width = width
        self.height = height
        self.board = []                  
        for row in range (self.height):
            boardRow = []
            for col in range (self.width):
                boardRow += [' ']       
            self.board += [ boardRow ]

    def __str__ (self):
        ''' returns a str of the board'''
        b = ''
        for row in range ( self.height ):
            b += '|'
            for col in range ( self.width ):
                b += self.board [row][col] + '|'
            b += '\n'
        b += '--' * self.width + '-\n'
        for col in range ( self.width ):
            b+= ' ' + str(col)
        b += '\n'
        return b

    def allowsMove (self,col):
        """Checks if a move is available """
        if 0 <= col < self.width:
            if self.board [0][col] == ' ':
                return True
        return False

    def addMove (self,col,ox):
        """Makes the move on the board"""
        if self.allowsMove(col):
            for row in range (self.height):
                if self.board [row][col] != ' ':
                    self.board [row-1][col] = ox
                    return
            self.board [self.height-1][col] = ox


    def delMove ( self , col ):
        """Deletes a move"""
        for row in range (self.height):
            if self.board[row][col] != ' ':
                self.board[row][col] = ' '
                return
    def isFull (self):
        """Checks if the board is full inorder to call a tie"""
        for col in range(self.width):
            if self.board[0][col] == ' ':
                return False
        return True

    def winsFor (self,ox):
        """Checks to see whos the winner"""
        # check for horizontal wins
        for row in range (0,self.height):
            for col in range (0,self.width-3):
                if self.board [row][col] == ox and \
                    self.board [ row ][ col + 1 ] == ox and \
                    self.board [ row ][ col + 2 ] == ox and \
                    self.board [ row ][ col + 3 ] == ox:
                    return True
        # check for vertical wins
        for row in range (0,self.height -3):
            for col in range (0,self.width):
                if self.board [row][col] == ox and \
                    self.board [ row + 1 ][ col ] == ox and \
                    self.board [ row + 2 ][ col ] == ox and \
                    self.board [ row + 3 ][ col ] == ox:
                    return True
        # check for diagonal wins NW to SE  
        for row in range (0,self.height-3):
            for col in range (0,self.width-3):
                if self.board [row][col] == ox and \
                    self.board [ row + 1 ][ col + 1 ] == ox and \
                    self.board [ row + 2 ][ col + 2 ] == ox and \
                    self.board [ row + 3 ][ col + 3 ] == ox:
                    return True
        # check for diagonal wins NE to SW   
        for row in range (0,self.height-3):
            for col in range (3,self.width):
                if self.board [row][col] == ox and \
                    self.board [ row + 1 ][ col - 1 ] == ox and \
                    self.board [ row + 2 ][ col - 2 ] == ox and \
                    self.board [ row + 3 ][ col - 3 ] == ox:
                    return True
        return False

    def hostGame( self ):
        """Hosts the game"""
        while True:
            print(self)
            while True:                     
                m = int(input ('Xs choice:' ))
                if self.allowsMove(m):
                    break
                else:
                    print("Invalid Move")       
            self.addMove (m,'x')
            if self.winsFor('x') == True:
                print ('X wins -- Congratulations!')
                print (self)
                return
            elif self.isFull() == True:
                print ('The game is a tie, the board is full.')
                print (self)
                return
            print(self)
            while True:                     
                m = int(input ('Os choice:'))
                if self.allowsMove(m):
                    break
                else:
                    print ("Invalid move")      
            self.addMove (m,'o')
            if self.winsFor('o') == True:
                print ('O wins -- Congratulations!')
                print (self)
                return
            elif self.isFull() == True:
                print ('The game is a tie, the board is full.')
                print (self)
                return


   
