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
  input_line = int(input("enter the line"))
  element_number = int(input("enter the element number"))
  list[input_line][element_number]= player


def main():
    while player_turn(modified_board_state) != None:
      move(player_turn(modified_board_state),modified_board_state)
      print(*modified_board_state,sep="\n")










if __name__ == "__main__":
    main()



















