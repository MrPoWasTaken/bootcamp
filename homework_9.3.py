emails = {}
PersonWithMax = ""
max = 0
ties = ""

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
  emails[words[1]] = emails.get(words[1],0) + 1
print(emails)

for sender in emails.keys():
  if emails[sender] > max:
    max = emails[sender]
    PersonWithMax = sender

for sender2 in emails.keys():
  if emails[sender2] == max and sender2 !=PersonWithMax:
    ties = f" and {sender2}"

print(f'{PersonWithMax}{ties} has/have sent the most emails at {max}')