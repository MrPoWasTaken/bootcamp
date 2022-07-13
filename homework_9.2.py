weekdays = {}

while True:
  user_file = input("Enter a file name (try filler.txt): ")
  if user_file == "":
    user_file = "filler.txt"

  try:
    driver = open(user_file,'r')
    break
  except:
    print('Could not open file :[ \n')

for line in driver:
  words = line.strip().split()
  weekdays[words[2]] = weekdays.get(words[2],0) + 1
print(weekdays)
