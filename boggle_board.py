import random

class BoggleBoard:
  dice = [
    ["AAEEGN", "ELRTTY", "AOOTTW", "ABBJOO"],
    ["EHRTVW", "CIMOTU", "DISTTY", "EIOSST"],
    ["DELRVY", "ACHOPS", "HIMNQU", "EEINSU"],
    ["EEGHNW", "AFFKPS", "HLNNRZ", "DEILRX"]
  ]
  
  def __init__(self):
    self.board = [
      "----",
      "----",
      "----",
      "----"
    ]
  
  def print_board(self):
    for row in self.board:
      print(row)

  def shake(self):
    new_board = []
    for row in self.dice:
      letters_lst=[]
      for die in row:
        randindex = random.randint(0,len(row[0])-1)
        if die[randindex] == "Q":
          letters_lst.append("Qu")
        else:
          letters_lst.append(die[randindex]) 
      new_board.append("".join(letters_lst))
    self.board = new_board
    self.print_board()


board = BoggleBoard()
board.print_board()
board.shake()