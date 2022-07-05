Lwords = []

Unique = []

while True:
  user_file = input("Enter a file name (try filler.txt): ")
  try:
    driver = open(user_file,'r')
    break
  except:
    print('Could not open file :[ \n')

f = driver.read()

Lwords = f.strip().split(' ')
for word in Lwords:
  if word not in Unique:
    Unique.append(word)
Unique.sort()
print (Unique)
