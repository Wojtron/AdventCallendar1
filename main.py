# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def welcome():
    greet = "Hello Elf! \n Here is your manager, where you should input calories of every meal you'll eat. \n"
    choice = input("Do you want to create new list or display sample list? (type 'new' or 'sample' : ")
    choiceFlag = False
    while(choiceFlag == False):
        if choice == "new" :
            choiceFlag = True
            userList()
        elif choice == "sample" :
            choiceFlag = True
            sampleList()
        else:
            print("Sorry i didn't understood :( ")


def userList():

    user = []
    userSingeElf = 0
    userSum =[]
    print("Ok! Remember, that every empty line means equipment of next Elf!")

    def addToList():
        newCalories = input()
        user.append(newCalories)

    def showList():

        elfNumber = 0
        if user == None:
            print("New list hasn't beet created yet. ")
        else:
            for x in user:
                print(user[x])
                if isinstance(user[x],int):
                    print(user[x])
                    userSingeElf = userSingeElf+user[x]
                else:
                    elfNumber = elfNumber+ 1
                    print("Elf number" + elfNumber + "equipment")
                    userSum.append(userSingeElf)
                    userSingeElf = 0
        print("sum of Elfs meals calories: " + sum(userSum))







 #            for x in user:
 #               print(user[x])
  #              if isinstance(user[x], int):
   #                 print("Elf Number" + elfCounter + ":   \n" + singleElf + "\n\n" )
    #                elfCounter = elfCounter + 1
#
 #               else


  #              elif x == len(user):
   #                 print(allElfs)






    def editList():
        showList()
        editedPosition = input("Which position should be edited? ")
        editedAmount = input ("What amount should be instead?")

        user[int(editedPosition)] = str(editedAmount)


    def getBack():
        return

def sampleList():

    sample = ["1000","2000","3000","","4000","","5000","6000","","7000","8000","9000","1000"]
    print("Here is your list")



def print_hi(name):
    welcome()


    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
