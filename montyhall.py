from tqdm import tqdm
from random import randint, seed

class Experiment:
  def __init__(self):
    seed()
    self.car_door = randint(0, 100000000000) % 3

  def run(self):
    player_choice = randint(0, 100000000000) % 3
    if player_choice == self.car_door:
      showman_choice = randint(0, 100000000000) % 2
      if player_choice == 0:
        if showman_choice == 0:
          showman_choice = 1
        else:
          showman_choice = 2
      elif player_choice == 1:
        if showman_choice == 1:
          showman_choice = 2
    else:
      for i in range(3):
        if i not in (player_choice, self.car_door):
          showman_choice = i
    for i in range(3):
      if i not in (player_choice, showman_choice):
        switch_choice = i
    switch = randint(0, 100000000000) % 2
    if switch == 1:
      player_choice = switch_choice
    return (player_choice == self.car_door, switch)


switch_wins_amount = 0
non_switch_amount = 0
tries = 1000000
for i in tqdm(range(tries), total=tries, position=0, leave=True):
  e = Experiment()
  res, switch = e.run()
  if res and switch == 1:
    switch_wins_amount += 1
  elif res:
    non_switch_amount += 1
  #if i % 1000 == 0 and i != 0:
  #  print("Cur wins rate", wins_amount / i)

print("\nResult switch wins rate", switch_wins_amount / tries)
print("Result non switch wins rate", non_switch_amount / tries)
