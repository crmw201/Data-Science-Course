
#=====importing libraries===========
import datetime  # Importing datetime to import current date & time

#====Login Section====
# Read the usernames and passwords from user.txt into a dictionary
users = {}
with open('user.txt', 'r') as user_file:
    for line in user_file:
        # Split each line in user.txt by ', ' to get the username and password
        username, password = line.strip().split(', ')
        # Store the username as the key and the password as the value in the 
        # users dictionary
        users[username.lower()] = password

# Loop until the user provides valid credentials
logged_in = False
while not logged_in:
    # Request username and password from the user
    username = input("Enter your username: ").lower()
    password = input("Enter your password: ").lower()

    # Check if the entered username exists and if the password matches
    if username in users and users[username] == password:
        print("Login successful!")
        logged_in = True  # Exit loop after successful login
    else:
        # If either username or password is incorrect, print an error and 
        # loop again
        print("Invalid username or password. Please try again.")

# Menu loop to allow the user to perform various actions after logging in
while True:
    # Display a menu and convert input to lowercase to make it case-insensitive
    menu = input('''Select one of the following options:
r - register a user (admin only)
a - add task
va - view all tasks
vm - view my tasks
s -stats (admin only)
e - exit
: ''').lower()

    #==== Registering a new user (Only admin is allowed (Compulsory Task 2 
    # part 1)) ====
    if menu == 'r':
        if username == 'admin':  # Check if the current user is 'admin'
            # Request a new username, password, and confirm password from the 
            # admin
            new_username = input("Enter new username: ").lower()
            new_password = input("Enter new password: ").lower()
            confirm_password = input("Confirm new password: ")

            # If the password matches the confirmation, add the new user to 
            # user.txt
            if new_password == confirm_password:
                with open('user.txt', 'a') as user_file:
                    # Write the new username and password in the required 
                    # format
                    user_file.write(f"\n{new_username}, {new_password}")
                print("New user has been added successfully!")
            else:
                # If the passwords don't match, inform the admin and ask again
                print("Passwords do not match. Please try again.")
        else:
            # If a non-admin user tries to register a new user, deny permission
            print("Only the admin can register new users.")

    #==== Adding a new task ====
    elif menu == 'a':
        # Prompt the user for task details: username, title, description, 
        # and due date
        task_username = input("Enter the username of the person the task is assigned to: ")
        task_title = input("Enter the title of the task: ")
        task_description = input("Enter the description of the task: ")
        task_due_date = input("Enter the due date of the task (e.g., 2023-09-30): ")
        
        # Get the current date for task assignment in YYYY-MM-DD format
        task_assigned_date = datetime.datetime.now().strftime("%Y-%m-%d")
        task_complete = "No"
        
        # Append the task data to tasks.txt, including 'No' to mark it 
        # as incomplete with clear formatting
        with open('tasks.txt', 'a') as task_file:
            task_file.write(f"{task_username}, {task_title}, {task_description}, "
                            f"{task_assigned_date}, {task_due_date}, {task_complete} \n")

        print("Task added successfully!")

    #==== Viewing all tasks (va) ====
    elif menu == 'va':
        with open('tasks.txt', 'r') as task_file:
            for line in task_file:
                #Split each line into components based on ', ' separator
                line = line.strip()
                task_parts = line.split(',')
                # Print the task details
                print(f"Task: {task_parts[1]}")
                print(f"Assigned to: {task_parts[0]}")
                print(f"Task description: {task_parts[2]}")
                print(f"Date assigned: {task_parts[3]}")
                print(f"Due date: {task_parts[4]}")
                print(f"Task complete? {task_parts[-1]}")
                print("-" * 60)  # Separator for readability
                               
    #==== Viewing tasks assigned to the logged-in user (vm) ====
    elif menu == 'vm':
        print("\nYour Tasks:\n")

        with open('tasks.txt', 'r') as task_file:
            tasks_found = False  # Flag to track if any tasks are found for the user

            for line in task_file:
                # Split each line into components based on ', ' separator
                task_parts = line.strip().split(', ')

                # Ensure that the line has the expected number of components
                if len(task_parts) == 6:
                    task_username, task_title, task_description, task_assigned_date, task_due_date, task_complete = task_parts
                    # When I tried to shorten this to one line (under 72 characters
                    # It wouldn't work, so have left as is
                    if task_username.lower() == username:
                        # Print the task details
                        print(f"Task: {task_title}")
                        print(f"Assigned to: {task_username}")
                        print(f"Task description: {task_description}")
                        print(f"Date assigned: {task_assigned_date}")
                        print(f"Due date: {task_due_date}")
                        print(f"Task complete: {task_complete}")
                        print("-" * 60)  #Separator for readability
                        tasks_found = True  # Set flag to indicate a task has been found

            # If no tasks were found for the user, print a message
            if not tasks_found:
                print(f"No tasks assigned to {username}.\n")

    #Compulsory Task 2 part 2 Displaying statistics
    elif menu == 's':
        if username.lower() == 'admin':
            with open('user.txt', 'r') as users:
                user_data = users.readlines()

            with open('tasks.txt', 'r') as tasks:
                task_data = tasks.readlines()

            print("---------STATISTICS---------")
            print('=' * 60)
            print(f" The number of users registered:\t {len(user_data)}")
            print(f" The number of tasks captured: \t {len(task_data)}")
            print('=' * 60)

        else:
            print("Sorry only for admin users")
    #==== Exiting the program ====
    elif menu == 'e':
        print("Goodbye!!!")
        exit()  

    #==== Handling invalid inputs ====
    else:
        print("You have entered an invalid input. Please try again.")
