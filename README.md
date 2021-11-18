# bingo-game-with-python
type of plays possible
1. player vs computer
2. player vs player
3. computer vs computer


game is built with 4 objects
classes
1.game
2.board
3.player
4.computer
5.super_computer (in progress)

# game class
game class contains game logic
## methods in game class
  1. who_is_next
  2. strike
  3. sync_both_boards
  4. update_score
  5. winner
  6. gameover

# board class
board class contains single method and is main objective is to hold board data

## methods in the board class
  1.print_board
  
# player class
player classs is the player object which contain name , score, input to the game

## Methods in the player class
  1. game_input
  
# computer class
computer class is same as player object but the computer class takes the input all by itself using 'random.choice'

## Methods in the computer class
  1. c_input
  
# super_computer class
super_Computer class is the same as computer class but it is made for winning game unlike computer class which just inputs random number in the allowed numbers

## methods in the super_computer class in progress
