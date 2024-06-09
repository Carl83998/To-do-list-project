tasks=[]
#menu function
def display_menu():
    print("1.select 1 to add task")
    print("2.select 2 to View task") 
    print("3.select 3 to view Update task")  
    print("4.select 4 to Delete task")  
    print("5.select 5 to Exit")
      
def add_task():
    user_tasks = input("kindly enter your task: \n")
    tasks.append(user_tasks)
    print("Task added successfully")

def view_task():
    if not tasks:
        print("to-do list is empty!!!kindly add task")
    else:
        for i, task in enumerate(tasks, 1):
         print(f"{i}.{task}")

#if not task:
    #print("to do list is empty !! Kindly add task")
#else 
def update_task():
    #display current task
    print("These are your available task")
    view_task()
    task_number = int (input("enter task number your  \n"))
    if 1 <= task_number <= len(tasks):
        updated_task = input("Enter update: ")
        tasks[task_number -1] = update_task
def delete_task():
    view_task()
    task_number= int(input("Enter task number to delete"))
    if 1 <=task_number <=len(tasks):
        #delete_task = tasks.pop(task_number -1)
        del tasks[task_number -1]
        print("print delete successfully")
    else: 
        print("invalid task number")
    
    print(tasks)
def exit_program():
    exit(1)
