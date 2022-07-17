alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
characters = []
amount = {}
letters = []

while True:
  user_file = input("Enter a file name (try filler.txt): ")
  if user_file == "":
    user_file = "filler.txt"

  try:
    driver = open(user_file,'r')
    break
  except:
    print('Could not open file :[ \n')

text = driver.read()
text = text.split()

for item in text:
  item = item.strip()
  item = list(item)
  characters.extend(item)

for char in characters:
  if char in alphabet:
    char = char.lower()
    letters.append(char)

for speclet in letters:
  amount[speclet] = amount.get(speclet, 0) + 1
print(amount)

