''' This project helps a small business to be able to manage tasks
    assigned to each member of the team.
'''

#=====importing libraries===========
'''Imported libraries'''
from datetime import date
from datetime import datetime

#Global variables
username = ""
user_list = []

#=====All Functions===========

#login function
def login():
    ''' In this section the user will be allowed to login if
        they enter the correct username and password.
        The correct usernames and passwords are stored in
        a textfile called user.txt.
    '''
    global username
    global user_list
    are_details_incorrect = True
    #0 - both password and username wrong
    #1 - username available but wrong password
    #2 - username and password correct
    result_search = 0

    print("-----Login Page-----")
    print("---Tino and Sons----")

    #Reading the user textfile to get username and password from database(textfile)
    with open('user.txt', 'r') as user_textfile:
        for row in user_textfile:
            row = row.replace(",", "")
            user_list.append(row.split())
            

    #Loop until correct username and password are entered
    while are_details_incorrect:
        username = input("Please enter your username: ")
        #loop if user doesn't enter anything
        while len(username) == 0:
            username = input("Please enter your username: ")

        password = input("Please enter your password: ")
        #loop if user doesn't enter anything
        while len(password) == 0:
            password = input("Please enter your password: ")

        #checking if password and username entered match
        for i in user_list:
            username_stored = i[0]
            password_stored = i[1]

            ''' Comparing user input and data stored on textfile to
                see if user can login, if credintials don't match
                repeat until correct credintials are entered. Exit
                loop when credentials are both correct
            '''
            if username == username_stored:
                if password == password_stored:
                    #both username and password correct, stop loop and go to main menu
                    result_search = 2
                    are_details_incorrect = False
                    break
                else:
                    ''' Print message if username exists but
                        the password entered is incorrect
                    '''
                    #incorrect password loop again
                    result_search = 1
                    break
            else:
                #loop again as both username and password are incorrect
                result_search = 0
                
        #printing appropriate message
        if result_search == 0:
            print("Incorrect username and password!" + "\n")
        elif result_search == 1:
            print("Incorrect password!" + "\n")
        elif result_search == 2:
            print("Success! Logging into your profile..." + "\n")
        else:
            print("Error!" + "\n")


#Register new user function
def reg_user():
        
    new_password_incorrect = True

    #Reading the user textfile to get username from database(textfile)
    with open('user.txt', 'r') as user_textfile:
        for row in user_textfile:
            row = row.replace(",", "")
            user_list.append(row.split())

    
    #Loop until user has entered a matching password
    while new_password_incorrect:            
        ''' ask user to input the credentials of new user
            to be added, loop if nothing is entered
        '''          
        new_username = input("Please enter username: ")
        while len(new_username) == 0:
            new_username = input("Please enter username: ")

        username_exist = True

        #checking if username entered doesn't already exist, if it does loop until it's not
        while username_exist:
                    
            #loop if nothing entered
            while len(new_username) == 0:
                new_username = input("Please enter username: ")
        
            #check if username already exists using for loop though list    
            for i in user_list:
                              
                if i[0] == new_username:
                    #1 - username found in list
                    #0 - username not found in list
                    username_found = 1 
                    break
                                                                         
                else:
                    username_found = 0
                    
            if username_found == 1:                    
                username_exist = True
                print("Username already exists!")
                new_username = input("Please enter username: ")
                
            elif username_found == 0:
                username_exist = False
                
            else:
                print("Error")          
            
        new_password = input("Please enter password: ")
        while len(new_password) == 0:
            new_password = input("Please enter password: ")
            
        new_password_conf = input("Please confirm password: ")

        #check if the passwords entered match each other
        if new_password == new_password_conf:          
            with open('user.txt', 'a') as user_textfile:
                #append new user to the textfile
                user_textfile.write("\n" + new_username + ", " + new_password)
                new_password_incorrect = False
                print("New user successfully added! Yeeeey :) " + "\n")
        else:
            print("Passwords don't match!" + "\n")

    


#Add a task function
def add_task():
    
    #Prompting the user to enter all the details needed for the new task
    task_username = input("Enter username of the person the task is to be assigned to: ")
    while len(task_username) == 0:
        task_username = input("Enter username of the person the task is to be assigned to: ")
        
    title_task = input("Enter title of task: ")
    while len(title_task) == 0:
        title_task = input("Enter title of task: ")
        
    description_task = input("Enter task description: ")
    while len(description_task) == 0:
        description_task = input("Enter task description: ")
        
    due_date = input("Enter due date of task in following format '7 May 2022': ")
    while len(due_date) == 0:
        due_date = input("Enter due date of task in following format '7 May 2022': ")

    #Get today's date
    today = date.today()
    date_assigned = today.strftime("%d %B %Y")        

    #Adding all the information to the tasks textfile
    with open('tasks.txt', 'a') as user_textfile:
        user_textfile.write(task_username + ", " + title_task + ", " + description_task + ", " + date_assigned + ", " + due_date + ", " + "No" + "\n")
        
        print("New Task successfully added! Yeeeey :) " + "\n")


    
#View all tasks function
def view_all():
    task_list = []
    #Reading the tasks textfile to get all the information from database(textfile)
    with open('tasks.txt', 'r') as tasks_textfile:            
        #store textfile data of tasks in list task_list, split by the commas
        for row in tasks_textfile:               
            row = row.replace("\n", "")
            task_list.append(row.split(", "))
              
        #display tasks to console in a readable format
        print("\n" + "----------------- All Tasks -----------------")
        
        for i in task_list:              
            print("Task:            \t" + str(i[1]) + "\n" +
                  "Assigned To:     \t" + str(i[0]) + "\n" +
                  "Date Assigned:   \t" + str(i[3]) + "\n" +
                  "Due Date:        \t" + str(i[4]) + "\n" +
                  "Task Complete?   \t" + str(i[5]) + "\n" +
                  "Task Description:\t" + str(i[2]) + "\n" )
            
        print("----------------- All Tasks -----------------" + "\n")



#View my tasks function
def view_mine():

    no_tasks = 0
    task_list = []
    #Reading the tasks textfile to get all the information from database(textfile)
    with open('tasks.txt', 'r') as tasks_textfile:            
        #store textfile data of tasks in list task_list, split by the commas
        for row in tasks_textfile:               
            row = row.replace("\n", "")
            task_list.append(row.split(", "))
              
    #display tasks to console in a readable format
    print("\n" + "----------------- All My Tasks -----------------")
    
    for i in task_list:
        if i[0] == username:
            
            no_tasks += 1
            #Only print the user who is logged in tasks 
            print(str(no_tasks) + ".\t" + "Task:            \t" + str(i[1]) + "\n" +
                  " \t" + "Assigned To:     \t" + str(i[0]) + "\n" +
                  " \t" + "Date Assigned:   \t" + str(i[3]) + "\n" +
                  " \t" + "Due Date:        \t" + str(i[4]) + "\n" +
                  " \t" + "Task Complete?   \t" + str(i[5]) + "\n" +
                  " \t" + "Task Description:\t" + str(i[2]) + "\n" )
            
                        
    if no_tasks == 0:
        print("You don't have any tasks!")
        print("----------------- All My Tasks -----------------" + "\n")
    else:
        print("----------------- All My Tasks -----------------" + "\n")
        
        #Allowing user to edit their tasks
        user_selection = int(input("Please select task number to edit or '-1' to return to main menu: "))
        task_num = 0

        #checking if the task has already been marked as complete and if yes don't allow user to edit by setting input to -1
        for i in task_list:      
            if i[0] == username:
                task_num += 1
                if user_selection == task_num:
                    if i[5] == "Yes":
                        print("Task already marked as complete!" + "\n")
                        user_selection = -1
                        break
        
        if user_selection > 0:

            
            edit_complete = input('''Would you like to edit this task or mark as complete?
                                     edit task - e
                                     mark as complete - c
                                     : ''').lower()
            if edit_complete == "e":

                task_num = 0
                
                edit_usern_due = input('''Would you like to edit both username assigned to task and due date or one or the other?
                                          Both username and due date - b
                                          Username - u
                                          Due date - d
                                          : ''').lower()
                if edit_usern_due == "b":
                    new_task_username = input("Enter new task username: ")
                    new_due_date = input("Enter new due date: ")
                    #looping through user tasks
                    for i in task_list:
                        if i[0] == username:
                            task_num += 1
                            #if task number matches the user selected number modify data in task list                            
                            if user_selection == task_num:
                                i[0] = new_task_username
                                i[4] = new_due_date
                                print("Task username and due date changed successfully")
                                break
                            
                elif edit_usern_due == "u":
                    new_task_username = input("Enter new task username: ")
                    #looping through user tasks
                    for i in task_list:
                        if i[0] == username:
                            task_num += 1
                            #if task number matches the user selected number modify data in task list                            
                            if user_selection == task_num:
                                i[0] = new_task_username
                                print("Task username changed successfully")
                                break
                            
                elif edit_usern_due == "d":
                    new_due_date = input("Enter new due date: ")
                    #looping through user tasks
                    for i in task_list:
                        if i[0] == username:
                            task_num += 1
                            #if task number matches the user selected number modify data in task list                            
                            if user_selection == task_num:
                                i[4] = new_due_date
                                print("Task due date successfully changed")
                                break

                else:
                    print("Incorrect Input!")
                                                            
                
            elif edit_complete == "c":
                
                #looping through user tasks
                task_num = 0
                for i in task_list:
                    if i[0] == username:
                        task_num += 1
                        #if task number matches the user selected number modify data in task list
                        if user_selection == task_num:
                            
                            i[5] = "Yes"
                            print("Task marked as complete")
                            break
            else:
                print("Incorrect input!")

            #Adding edited information to the tasks textfile
            with open('tasks.txt', 'w') as user_textfile:
                for i in task_list:                    
                    user_textfile.write(i[0] + ", " + i[1] + ", " + i[2] + ", " + i[3] + ", " + i[4] + ", " + i[5] + "\n") 
            
        elif user_selection == -1:
            print("No change made" + "\n")
            
        else:
            print("Incorrect input" + "\n")


#generate reports function
def generate_reports():

    total_tasks = 0
    total_complete = 0
    total_incomplete = 0
    total_overdue = 0
    percentage_incomplete = 0
    percentage_overdue = 0

    total_users = 0

    task_list = []
    list_users = []
    user_stats_list = []
    new_user_stats_list = []

    #Get today's date
    today = datetime.now()

    #This section generates the task overview report
    #looping though task list to determine stats and writing them to textfile task_overview
    with open('tasks.txt', 'r') as tasks_textfile:            
        #store textfile data of tasks in list task_list, split by the commas
        for row in tasks_textfile:               
            row = row.replace("\n", "")
            task_list.append(row.split(", "))
            
    for i in task_list:
        #counting total tasks
        total_tasks += 1

        #removing spaces before and after string
        i[4] = i[4].strip()
        i[5] = i[5].strip()

        #converting date from string to date
        due_date = datetime.strptime(i[4], "%d %B %Y")

        #check if task is complete or not and check if overdue or not
        if i[5].lower() == "yes":
            total_complete += 1
        elif i[5].lower() == "no":
            total_incomplete += 1
            if due_date < today:
                total_overdue += 1
        else:
            print("Error!")
            
    #calculating percentages
    percentage_incomplete = round((total_incomplete/total_tasks)*100, 2)
    percentage_overdue = round((total_overdue/total_incomplete)*100, 2)       

    #writing data to text file of tasks report               
    with open('task_overview.txt', 'w') as user_textfile:
        user_textfile.write("Total tasks: " + str(total_tasks) +"\n" +
                             "Total completed tasks: " + str(total_complete) + "\n" +
                             "Total incomplete tasks: " + str(total_incomplete) + "\n" +
                             "Total overdue tasks: " + str(total_overdue) + "\n" +
                             "Percentage incomplete tasks: " + str(percentage_incomplete) + "%" + "\n" +
                             "Percentage overdue tasks: " + str(percentage_overdue) + "%" )
                            
    print("Task Report successfully generated!")


    #This section generates the user overview report
    #Reading the user textfile to get usernames from database(textfile)
    with open('user.txt', 'r') as user_textfile:
        for row in user_textfile:
            list_users.append(row.split(", "))

    #looping though the users list         
    for i in list_users:
        total_users += 1
        
        #set numbers per user and reset for every new user
        total_user_tasks = 0
        total_user_tasks_complete = 0
        total_user_tasks_incomplete = 0
        total_user_tasks_overdue = 0
        
        i[0] = i[0].strip()
        
        for j in task_list:
            
            j[4] = j[4].strip()
            j[5] = j[5].strip()
            
            #check for every user the tasks assigned to them and do the calculations
            if i[0] == j[0]:
                user_due_date = datetime.strptime(j[4], "%d %B %Y")
                total_user_tasks += 1
                
                #check if task is complete or not and check if overdue or not
                if j[5].lower() == "yes":
                    total_user_tasks_complete += 1
                elif j[5].lower() == "no":
                    total_user_tasks_incomplete += 1
                    if user_due_date < today:
                        total_user_tasks_overdue += 1
                else:
                    print("Error!")

        #calculate the percentages for the user tasks
        if total_user_tasks == 0 or total_tasks == 0:
            percentage_user_tasks = 0
            percentage_user_complete = 0
            percentage_user_tocomplete = 0
            percentage_user_overdue = 0
        else:     
            percentage_user_tasks = round((total_user_tasks/total_tasks)*100, 2)
            percentage_user_complete = round((total_user_tasks_complete/total_user_tasks)*100, 2)
            percentage_user_tocomplete = round((total_user_tasks_incomplete/total_user_tasks)*100, 2)
            percentage_user_overdue = round((total_user_tasks_overdue/total_user_tasks)*100, 2)

        #store each user information in a list        
        user_stats_list.append(i[0] + "," + str(total_user_tasks) + "," + str(percentage_user_tasks) + "," +
                                 str(percentage_user_complete) + "," + str(percentage_user_tocomplete) + "," + str(percentage_user_overdue) + "\n")

    
    #split the list to access each data entry   
    for row in user_stats_list:
        row = row.replace("\n", "")
        new_user_stats_list.append(row.split(','))

    #store task overview of user in the task overview file           
    with open('user_overview.txt', 'w') as user_textfile:
        user_textfile.write("Total users: " + str(total_users) +"\n" +
                             "Total tasks: " + str(total_tasks) + "\n" + "-" + ": " + "-" + "\n")

        #run through every element in the list and write it in the textfile
        for i in new_user_stats_list:              
            user_textfile.write("Username: " + i[0] + "\n" +
                                "Total user tasks: " + i[1] + "\n" +
                                "Percentage user tasks: " + i[2] + "%" + "\n" +
                                "Percentage user tasks complete: " + i[3] + "%" + "\n" +
                                "Percentage tasks to complete: " + i[4] + "%" + "\n" +
                                "Percentage tasks overdue: " + i[5] + "%" + "\n" + "-" + ": " + "-" + "\n")
                                           
    print("User Report successfully generated!\n")
    

    
def stats_admin():

    user_overview_list = []
    user_task_overview_list = []

    #generate reports
    generate_reports()
    
    #Reading the task overview textfile to get report
    with open('task_overview.txt', 'r') as task_overview_textfile:
        for row in task_overview_textfile:
            row = row.replace("\n", "")
            user_task_overview_list.append(row.split(": "))

    #print task overview report
    print("--------------------")
    print("TASK OVERVIEW REPORT\n")
    for i in user_task_overview_list:
        print(i[0] + ": " + i[1])
    
    print("--------------------")

    #Reading the user overview textfile to get report
    with open('user_overview.txt', 'r') as user_overview_textfile:
        for row in user_overview_textfile:
            row = row.replace("\n", "")
            user_overview_list.append(row.split(": "))
            
    

    #print user overview report
    print("USER OVERVIEW REPORT\n")      
    for i in user_overview_list:
        if i[0] == "-":
            print(i[0] + "" + i[1])
        else:        
            print(i[0] + ": " + i[1])
        
    print("--------------------\n")


#Main function
def main():
    
    #====Login function====

    login()
    
    #====Main Menu Section====
    
        #===Admin Section=== 
    if username == "admin":    
        while True:
            #presenting the menu to the user and 
            #making sure that the user input is converted to lower case.
            menu = input('''Select one of the following Options below:
            r - Registering a user
            a - Adding a task
            va - View all tasks
            vm - View my task
            gr - Generate reports
            ds - Display statistics
            e - Exit
            : ''').lower()

            #This section of code is for a user to register a new user   
            if menu == 'r':

                #call register function
                reg_user()


            #This section of code is for user to add a new task        
            elif menu == 'a':

                #call add new task function
                add_task()          

                    
            #This section of code is for user to view all tasks
            elif menu == 'va':

                #call view all function
                view_all()
               

            #This section of code is for user to view their own tasks
            elif menu == 'vm':

                #call view my tasks function
                view_mine()                    

            #This section of code is for user to generate reports stored in two text files #####
            elif menu == 'gr':

                #call genrate reports function
                generate_reports()
                
            #This section of code is if user wants to see the statistics of tasks
            elif menu == 'ds':

                #call stats function to calculate statistics
                stats_admin()


            #This section of code is if user wants to exit program
            elif menu == 'e':
                print('Goodbye!!!')
                exit()

            else:
                print("You have made a wrong choice, Please Try again")


                
        #===User Section=== 
    else:
        while True:
            #presenting the menu to the user and 
            #making sure that the user input is converted to lower case.
            menu = input('''Select one of the following Options below:
            a - Adding a task
            va - View all tasks
            vm - View my task
            e - Exit
            : ''').lower()

            #This section of code is for user to add a new task        
            if menu == 'a':

                #call add task function
                add_task()           

                    
            #This section of code is for user to view all tasks
            elif menu == 'va':
                
                #call view all tasks function
                view_all()
               

            #This section of code is for user to view their own tasks
            elif menu == 'vm':
                        
                #call view my tasks function
                view_mine()

            #This section of code is if user wants to exit program
            elif menu == 'e':
                print('Goodbye!!!')
                exit()

            else:
                print("You have made a wrong choice, Please Try again")




if __name__=="__main__":
    main()
