while True:
  user_file = input("Enter a file name (try filler.txt): ")
  try:
    driver = open(user_file,'r')
    break
  except:
    print('Could not open file :[ \n')

print('\n')
for line in driver:
  print(line.upper(), end = "")
print("\n")