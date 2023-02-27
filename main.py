class MenuOutOfRange(Exception):
    #This class is for triggering a custom exception
    pass

def RunMenu(menuList):

    continueLoop = True
    while continueLoop == True:

        try: #Tells the compiler to attempt the code indented, passing to an exception if an error occurs
            
           
            print(menuList[0])  #Start text to the screen with the initial value in the passed list

            for x in range(1, len(menuList)): #Loops from 1 (because be have used index 0 already), until the end of the indexes in our passed list
                print(str(x) + ": " + menuList[x]) #Prints out a formatted text screen, using the text passed up to the function inside the list, using x as the index counter

            menuChoice = int(input("\nPlease make a selection from the list provided:\n")) #Requests the user enter an int - then saves it into the variable assignment

            if menuChoice > len(menuList) - 1 or menuChoice < 1:
                raise MenuOutOfRange #Raises the custom exception if the IF statement validates as TRUE

        except MenuOutOfRange: #Triggers when the user enters a value outside of the list range provided

            print("\n\nError! PLease only enter a number from the list indicated, please try again...")
            input("[Press Enter to Try Again]\n\n")

        except ValueError: #Triggers when the user enters a non-integer value

            print("\n\nError! PLease only enter a valid whole number, please try again...")
            input("[Press Enter to Try Again]\n\n")

        except: #Triggers exception - no specific condition required.

            print("\n\nError! An unknown bug as occurred, please try again...")
            input("[Press Enter to Try Again]\n\n")

        else: #Triggers only when no exception has been raised!

            continueLoop = False
            return menuChoice #Returns the user's input

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
    