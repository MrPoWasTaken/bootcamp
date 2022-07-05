count = 0
people = []

while True:
  user_file = input("Enter a file name (try filler.txt): ")
  try:
    driver = open(user_file,'r')
    break
  except:
    print('Could not open file :[ \n')


for line in driver:
  WordsInLine = line.strip().split(' ')
  if WordsInLine[0].lower() == 'from':
    people.append(WordsInLine[1])
    count += 1


for person in people:
  print(person)
print(f'There were {count} lines in the file with "From" as the first word: ')