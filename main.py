import time

answer = str(input('Skills or Match '))
if (answer == 'Skills' or answer == 'skills'):
  discsScored = int(input('Discs Scored:'))
  tilesScored = int(input('Tiles Covered:'))
  rollersScored = int(input('Rollers Scored:'))
  lowgoalDiscs = int(input("Low Goal Discs:"))
  while (abs(lowgoalDiscs + discsScored) > 60):
    discsScored = int(input('Discs Scored:'))
    lowgoalDiscs = int(input("Low Goal Discs:"))
  while (abs(discsScored) > 60):
    discsScored = int(input('Discs Scored:'))
  while (abs(rollersScored) > 4):
    rollersScored = int(input('Rollers Scored:'))
  while (abs(tilesScored) > 28):
    tilesScored = int(input('Tiles Covered:'))
  totalScore = int(discsScored * 5 + tilesScored * 3 + rollersScored * 10 +lowgoalDiscs)
  print(totalScore)
if (answer == 'Match' or answer == 'match'):
  print('Blue Alliance Score:')
  discsScoredb = int(input('Discs Scored:')) * 5
  tilesScoredb = int(input('Tiles Covered:')) * 3
  rollersScoredb = int(input('Rollers Scored:')) * 10
  lowgoalDiscsb = int(input("Low Goal Discs:"))
  AutoWinB = int(input('10 for Auto win, 0 for loss '))
  SB = int(discsScoredb + tilesScoredb + rollersScoredb + lowgoalDiscsb +
           AutoWinB)
  time.sleep(1)
  print('Red Alliance Score:')
  discsScoredr = int(input('Discs Scored:')) * 5
  tilesScoredr = int(input('Tiles Covered:')) * 3
  rollersScoredr = int(input('Rollers Scored:')) * 10
  lowgoalDiscsr = int(input("Low Goal Discs:"))
  AutoWinR = int(input('10 for Auto win, 0 for loss '))
  SR = int(discsScoredr + tilesScoredr + rollersScoredr + lowgoalDiscsr +
           AutoWinR)
  print(f'Blue {SB} - Red {SR}')
  if (SB > SR):
    print('Blue wins!')
  else:
    print('Red wins!')
