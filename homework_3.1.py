hrs = float(input('How many hours do you work? '))
pay = float(input('How much do you make in a hour? '))
if hrs >40:
  DifFrom40 = (hrs-40)*1.5
else:
  DifFrom40 = hrs-40
totalP = 40*pay + DifFrom40*pay
print(f"Your total pay is {totalP}")
