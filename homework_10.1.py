emails = {}
Counts = []

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
  email = line.split()[1]

  emails[email] = emails.get(email, 0) + 1

for email, number in emails.items():
  Counts.append((number, email))

Counts.sort(reverse = True)
largest = Counts[0]

print(f'{largest[1]} had sent the most emails with {largest[0]}')