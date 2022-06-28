numbers = []
largest = None
smallest = None
user= None


while True:
  try:
    user = input('Enter a number: ')
    user = float(user)
    numbers.append(user)

  except:
    if user == "stop":
      break
    print('Please enter a number')


for i in numbers:
  if largest == None:
    largest = i
    smallest = i

  if i > largest:
    largest = i
  if i < smallest:
    smallest = i

print(f'The largest number you said was {largest}')
print(f'The smallest number you said was {smallest}')