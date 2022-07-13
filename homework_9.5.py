emails = {}
domains = {}

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
  words = line.strip().split()
  emails[words[1]] = emails.get(words[1],0) + 1

  NameAndDomain = words[1].split("@")
  NameAndDomain = NameAndDomain[-1]
  domains[NameAndDomain] = emails.get(NameAndDomain,0) + 1

print(f'List of emails: {emails}')
print(f'List of domains: {domains}')