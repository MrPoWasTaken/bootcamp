def computepay (hrs, rate):
  if hrs >40:
    DifFrom40 = (hrs-40)*1.5
  else:
    DifFrom40 = hrs-40
  totalP = 40*pay + DifFrom40*pay
  return totalP

hrs = float(input('How many hours do you work? '))
pay = float(input('How much do you make in a hour? '))

totalMoney = computepay(hrs,pay)

print(f"Your total pay is {totalMoney}")
