def RunMenu(menuList):

  continueLoop = True
  while continueLoop == True:

    try: #tells the compiler to attempt the code indented, passing to an exception if an error occurs
      
      
      print(menuList[0]) #start txt to the screen with the initial value in the passed list
    
      for x in range(1, len(menuList)): #Loops from 1
        print(x, ": ", menuList[x]) #prints out a formatted txt screen
    
      menuChoice  = int(input("\nPlease make a selection from the list provided:\n")) 
    
      return menuChoice #returns the user's input

    except ValueError: #triggers when the user enters a non-integer value
      print("\nError! An unknown bug as occured, please try again...")
      input("[Press Enter to Try Again]\n\n") 
      
    except: #triggers exception - no specific condition required
      print("\nError! An unknown bug as occured, please try again...")
      input("[Press Enter to Try Again]\n\n") 


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