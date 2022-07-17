TimeSent = {}
Lmessages = []

while True:
  user_file = input("Enter a file name (try filler.txt): ")
  if user_file == "":
    user_file = "time.txt"

  try:
    driver = open(user_file,'r')
    break
  except:
    print('Could not open file :[ \n')
'''
for line in driver:
  words = line.split()
  time = words[-2]
  hour = time.split(':')[0]
'''
for line in driver:
  hour = line.split()[-2].split(':')[0]

  TimeSent[hour] = TimeSent.get(hour, 0) + 1


for time, amount in TimeSent.items():
  Lmessages.append((time, amount))

for tup in Lmessages:
  print(f'At {tup[0]}, {tup[1]} messages were sent')


