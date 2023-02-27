def RunMenu(menuList):

  #3
  print(menuList[0])

  for x in range(1, len(menuList)):
    print(x, ": ", menuList[x])

  menuChoice  = int(input("\nPlease make a selection from the list provided:\n"))

  return menuChoice 


continueLoop = True
while continueLoop == True:

  menuList = ["\n----menu------\n", "Registered Student", "Assigns Student to class", "Take Registartion", "Exit"]

  menuChoice = RunMenu(menuList)

  if menuChoice == 1:
    print("\n1. Register Student....\n")
  elif menuChoice == 2:
    print("\n2. Assign students....\n")
  elif menuChoice == 3:
    print("\n3. Take Register.....\n")
  else:
    print("Goodbye")
    continueLoop = False