run = True
while run == True:
  score = input('What is your score? ')
  try:
    score = float(score)
    run = False
  except:
    print('You need to enter a number')


if score >= .9:
  print('You got a A')
elif score >= .8:
  print('You got a B')
elif score >= .7:
  print('You got a C')
elif score >= .6:
  print('You got a D')
else:
  print('You got a F')