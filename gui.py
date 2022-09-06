from colorama import *
init()
Loop_variable=True

while Loop_variable == True:

    print(Fore.BLUE+'''(1)press for display
    (2)press for functionality
    (3)press for config 
    (4)press for exit'''+Style.RESET_ALL)
    input_variable=input("choose what you want to see:")
    if input_variable=="1":
        print(Fore.CYAN+"the image"+Style.RESET_ALL)
    elif input_variable=="2":
        print(Fore.GREEN+"This is an integrated jpg"+Style.RESET_ALL)
    elif input_variable=="3":
        print(Fore.LIGHTBLACK_EX+"This is made to show a jpg file"+Style.RESET_ALL)
        
    elif input_variable=="4":
        print("There is nothing else to display")
        Loop_variable=False

    else:
        ("Your requirnments can not be meet!Thank you ")
