def display_board(board):
  print(('  |   | ').center(80,' '))
  print((' '+board[7]+' | '+board[8]+' | '+board[9]).center(80,' '))
  print(('  |   | ').center(80,' '))
  print(('-- ---- --').center(80,' '))
  print(('  |   | ').center(80,' '))
  print((' '+board[4]+' | '+board[5]+' | '+board[6]).center(80,' '))
  print(('  |   | ').center(80,' '))
  print(('-- ---- --').center(80,' '))
  print(('  |   | ').center(80,' '))
  print((' '+board[1]+' | '+board[2]+' | '+board[3]).center(80,' '))
  print(('  |   | ').center(80,' '))


def player_input():
  marker = ''
  while not(marker == 'X' or marker == 'O'):
    marker = input('\nPlayer1, Choose X or O: ')

  player1 = marker

  if player1 == 'X':
    return ('X','O')
  else:
    return ('O','X')
    
def position_choice():
  choice = ' '
  while choice not in range(1,11):
    choice = input("Enter a position (1-10): ")
    print('\n')
    if choice.isnumeric():
      if int(choice) in range(1,11):
        break
    else:
      print(("Sorry not a valid input!").center(80,' '))
  return int(choice)
  
def replacement_choice(board, pos, playerInput):
  user_placement = playerInput
  board[pos] = user_placement
  display_board(board)
  return board


def gameOn_choice():
  answer = ' '
  while answer != 'Y' and answer != 'N':
    answer = input(("\nKeep playing?: ('Y','N') ").center(80,' '))
  if answer == 'Y':
    return True
  else:
    print(("Thanks for playing!").center(80,' '))
    return False

def winnerCheck(board, player1,player2):
  if (
      (player1 == board[1] and player1 == board[2] and player1 == 
 board[3]) or
      (player1 == board[1] and player1 == board[4] and player1 == board[7]) or
      (player1 == board[1] and player1 == board[5] and player1 == board[9]) or
      (player1 == board[2] and player1 == board[5] and player1 == board[8]) or
      (player1 == board[3] and player1 == board[6] and player1 == board[9]) or
      (player1 == board[3] and player1 == board[5] and player1 == board[7]) or
      (player1 == board[4] and player1 == board[5] and player1 == board[6]) or
      (player1 == board[7] and player1 == board[8] and player1 == board[9])
  ):
    return True

  if(
    (player2 == board[1] and player2 == board[2] and player2 == board[3]) or
    (player2 == board[1] and player2 == board[4] and player2 == board[7]) or
    (player2 == board[1] and player2 == board[5] and player2 == board[9]) or
    (player2 == board[2] and player2 == board[5] and player2 == board[8]) or
    (player2 == board[3] and player2 == board[6] and player2 == board[9]) or
    (player2 == board[3] and player2 == board[5] and player2 == board[7]) or
    (player2 == board[4] and player2 == board[5] and player2 == board[6]) or
    (player2 ==  board[7] and player2 == board[8] and player2 == board[9])
  ):
    return True
            



print('TIC-TAC-TOE\n'.center(81,' '))
startGame = True
while startGame:
  
  board = ['#','1','2','3','4','5','6','7','8','9']
  gameOn = True
  winner = False
  print(('New Game!\n').center(81,' '))
  display_board(board)
  player1, player2 = player_input()
  
  while gameOn:
    print('\nPlayer1, ', end=' ')
    pos = position_choice()
    board = replacement_choice(board, pos, player1)
  
    winner = winnerCheck(board,player1,player2)
    if winner == True: 
      print('\n')
      print(("🏆").center(81,' '))
      print(("WINNER!\n").center(80,' '))
      display_board(board)
      gameOn = gameOn_choice()
      if gameOn:
        print('\n'*3)
        break;
      else:
        startGame = False
        break
    
    print('\nPlayer2, ', end=' ')
    pos = position_choice()
    board = replacement_choice(board, pos, player2)
  
    winner = winnerCheck(board,player1,player2)
    if winner == True: 
      print('\n')
      print(("🏆").center(81,' '))
      print(("WINNER!\n").center(80,' '))
      display_board(board)
      gameOn = gameOn_choice()
      if gameOn:
        print('\n'*3)
        break;
      else:
        startGame = False
        break
  
  
  
