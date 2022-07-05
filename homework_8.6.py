numbers = []
largest = None
smallest = None
user= None


while True:
  user = input('Enter a number: ')

  if user == 'done':
    break

  try:
    user = float(user)
  except:
    print('Please enter a number next time (type "done" to stop) \n')
    continue
  numbers.append(user)



for i in numbers:
  if largest == None:
    largest = i
    smallest = i

  if i > largest:
    largest = i
  elif i < smallest:
    smallest = i

print(f'The largest number you said was {largest}')
print(f'The smallest number you said was {smallest}')