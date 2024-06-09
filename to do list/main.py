from program import * 

print("******To-do list application*******")
print()
#impoort program modul
#get user choice 
while True:
#invocation of the menu 
    display_menu()
# accepting user option 
    user_option = int(input("kindly choose from the following options: "))
    #check if the user is 1 
    if user_option ==1:
        add_task()
    elif user_option ==2:
        view_task() 
    elif user_option ==3:
        update_task()
    elif user_option ==4:
        delete_task()
    elif user_option ==5:
        pass 
    else:
        print("Invalid option, Kindly Choose from option 1 - 5")