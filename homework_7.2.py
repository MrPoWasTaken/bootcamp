amount = 0
total = 0


while True:
  user_file = input("Enter a file name (try filler.txt): ")
  if user_file == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd")


  try:
    driver = open(user_file,'r')
    break
  except:
    print('Could not open file :[ \n')

driver = open(user_file,'r')

for line in driver:
  if line.startswith('X-DSPAM-CONFIDENCE:'):
    number = float(line[19:].strip())
    total += number
    amount += 1

print(f'Average spam confidence: {total/amount}')