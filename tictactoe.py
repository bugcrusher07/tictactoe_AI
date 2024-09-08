x = 1
o = 0
empty = None
a =None
initial_board_state = [[a,a,a],
                       [a,a,a],
                       [a,a,a]]


modified_board_state = initial_board_state
def player_turn (list):
  no_of_empty = 0
  for element in list:
    for sub_element in element:
      if sub_element == None:
        no_of_empty+=1
  if no_of_empty%2 ==1:
    return x
  elif no_of_empty == 0:
    return empty
  else:
    return o

def move(player,list):
  input_line = int(input("enter the line\n"))
  element_number = int(input("enter the element number\n"))
  list[input_line][element_number]= player
  who_won(input_line,element_number,list)

def who_won(row,column,list):
  player = list[row][column]
  winner =  player
  if row and column != 1:
    if row or column == 1:
      for index,element in list:
        if index != row:
          continue
        for subElement in element:
          if subElement != player:
            winner = None



def main():
    counter = 0
    winner = None
    turn = player_turn(modified_board_state)
    while turn != None:
      move(turn,modified_board_state)
      if counter <= 4:
         counter +=1
      else:
         winner = who_won(modified_board_state)

      print(*modified_board_state,sep="\n")
      if winner != None:
         print(f"{winner} Won LOL")
         break
      turn = player_turn(modified_board_state)
      if turn ==None:
        print("Game Over \n Nobody Won")
        break









if __name__ == "__main__":
    main()



















