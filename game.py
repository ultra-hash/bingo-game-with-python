"""
    1. Board with 25 squares
    2. fill numbers in those squares
    3. pick a number 
    4. strike 5 numbers in a line vertical, horizontal , diagonal
    5. strike 5 lines to win game

    class
    1. board
        * squars
        * check win
        * next turn
    2. game
        * check win
        * check numbers used
        * update score
    3. player
        * score
        * input move
    4. computer
        * score
        * input move


"""


import random, time

def main():
    
    player1 = player('swamy')
    player2 = player('damu')
    engine = game(player1, player2)

    player1.board = board()
    player2.board = board()
    
    #player1.board.print_board()
    while len(engine.set) != 25 and engine.game_not_over:
        next = engine.who_is_next()
        if isinstance(player1, player) and isinstance(player2, player):
            next.board.print_board()
        else:
            player1.board.print_board()
        engine.strike(next,engine)
        winner = engine.gamewinner
    print()
    print('Printing Both Players Boards & Score')
    print(' Player1'.center(15," ")+'   '+' player2'.center(15," "))
    print(f' name : {player1.name}'.center(15," ")+'   '+f' name : {player2.name}'.center(15," "))
    print(f' score : {player1.score}'.center(15," ")+'   '+f' score : {player2.score}'.center(15," "))

    for i in range(5):
        print('|'+ '|'.join(player1.board.board[i*5:(i*5)+5])+ '|', end= "  ")
        print('|'+ '|'.join(player2.board.board[i*5:(i*5)+5])+ '|')
        

    return (player1.name,player2.name,winner)

def max_games(count):
    (c,p1,p2) = (0,0,0)
    while c != count:
        (player1,player2,winner) = main()
        if winner == player1:
            p1+=1
        elif winner == player2:
            p2+=1
        c+=1
        #print(winner)
    print(player1,' wins :', p1 ,player2,'wins :',p2)

class board:
    def __init__(self):
        self.boardsize = 25
        self.board = [str(x).rjust(2, ' ') for x in range(1,26)]
        random.shuffle(self.board)
    
    def print_board(self):
        print()
        for i in range(5):
            print('|'+ '|'.join(self.board[i*5:(i*5)+5])+ '|')

class game:
    def __init__(self, player1, player2):
        self.set = set()
        self.next = player2
        self.player1 = player1
        self.player2 = player2
        self.game_not_over = True
        self.gamewinner = ''

    def who_is_next(self):
        if self.next == self.player1:
            self.next = self.player2
        elif self.next == self.player2:
            self.next = self.player1
        return self.next

    def strike(self, player , gameobj):
        P_or_C_input = player.c_input(gameobj) if isinstance(player, computer) else player.game_input(gameobj)
        gameobj.set.add(P_or_C_input)
        number = str(P_or_C_input).rjust(2, ' ')
        player.board.board[player.board.board.index(number)] = '*'.rjust(2, ' ')
        self.sync_both_board(player,number)

    def sync_both_board(self,player,number):
        temp = self.player1 if player == self.player2 else self.player2
        temp.board.board[temp.board.board.index(number)] = '*'.rjust(2, ' ')
        return self.update_score(player)

    def update_score(self, player):
        temp_board = [player.board.board[i*5:(i*5)+ 5] for i in range(5)]
        player.score = 0
        #check for horizontal lines
        for i in range(5):
            horizontal = []
            for j in range(5):
                horizontal.append('*' in temp_board[i][j])
            if all(horizontal):
                player.score+=1
                
        #check for vertical lines
        for i in zip(*temp_board):
            vertical = []
            for j in range(5):
                vertical.append('*' in i[j])
            #print(vertical)
            if all(vertical):
                player.score+=1

        #check for diagonal lines
        lt_to_rb = []
        rt_to_lb = []
        diagonal = [[],[]]
        for i in range(5):
            for j in range(5):
                if i == j:
                    lt_to_rb.append(temp_board[i][j])
                    rt_to_lb.append(temp_board[i][-j-1])
                    diagonal[0].append('*' in lt_to_rb[i])
                    diagonal[1].append('*' in rt_to_lb[i])
        
        for i in diagonal:
            #print(i)
            if all(i):
                player.score+=1
        print('name :',player.name, '| score :', player.score)
        
        return self.winner(player)

    def winner(self, player):
        if player.score >= 5:
            return self.gameover(player)

    def gameover(self,player):
        self.game_not_over = False
        if not self.game_not_over:
            print('B I N G O', player.name,'won')
            self.gamewinner = player.name


class player:
    def __init__(self, name):
        self.score = 0
        self.name = name

    def game_input(self, gameobj):
        self.input = input(f'Your move now {self.name} : ').rjust(2, ' ')
        while self.input in gameobj.set or self.input not in self.board.board:
            print('number already used or invalid, try other number')
            self.input = input(f'Your move now {self.name} : ').rjust(2, ' ')
        print('player1 choose', self.input)
        return self.input



class computer:
    def __init__(self,name):
        self.name = name
        self.score = 0

    def c_input(self,gameobj):
        #time.sleep(1)
        self.cinput = random.choice([str(x) for x in range(1,26) if x not in gameobj.set]).rjust(2, ' ')
        while self.cinput in gameobj.set or self.cinput not in self.board.board:
            self.cinput = random.choice([str(x) for x in range(1,26) if x not in gameobj.set]).rjust(2, ' ')

        print(self.name,'choose', self.cinput)
        return self.cinput



'''
class supercomputer:
    def __init__(self,name):
        self.name = name
        self.score = 0

    def c_input(self,gameobj):
        self.cinput = random.choice([str(x) for x in range(1,26) if x not in gameobj.set]).rjust(2, ' ')
        while self.cinput in gameobj.set or self.cinput not in self.board.board:
            self.cinput = random.choice([str(x) for x in range(1,26) if x not in gameobj.set]).rjust(2, ' ')

        print(self.name,'choose', self.cinput)
        return self.cinput

    def state(self,gameobj):
        self.init_board = [self.board.board[i*5:(i*5)+ 5] for i in range(5)]
        """
            if 1 star or less presnet in borad try star in corners and mid point
            if more than 1 star identify star's location and put a start striking max star's 
        """
'''        



#max_games(100)
main()
