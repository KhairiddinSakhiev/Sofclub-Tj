users_db = []
main_user = None
class User:
    def __init__(self,first_name,last_name,email,username,password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email} {self.username} {self.password}"
    
class UserManager:
    def register(self):
        user = User(
            input("First name : "),
            input("Last name : "),
            input("Email : "),
            input("Username : "),
            input("Password : ")
        )
        global users_db
        users_db.append(user)
        print("Registration has passed succesifully!")
    
    def login(self, username, password):
        for user in users_db:
            if user.username==username:
                if user.password==password:
                    global main_user
                    main_user = user
                    print("Your loged in successifully")
                    return user
                else:
                    print("Your password is incorrect!")
            else:
                print(f"User with name {username} is not found")

    def logout(self):
        global main_user
        main_user = None
        print("Log out")


from datetime import datetime\

database = []

class Task:
    id = 0
    def __init__(self, user, task_name, due_date, description, is_done=False):
        self.id += 1
        self.user = user
        self.task_name = task_name
        self.due_date = due_date
        self.description = description
        self.is_done = is_done
        self.created_at = datetime.now()
        Task.id+=1
    
    def __str__(self):
        return f"{self.user} {self.task_name}, {self.due_date}, {self.is_done}"


class TaskManager:
    def add_task(self, username):
        new_task = Task(
            username,
            input("Task name: "),
            input("Due date: "),
            input("Description: ")
        )
        database.append(new_task)

    def get_task_by_id(self, id):
        for task in database:
            if task.id == id :
                return task

    def get_all_tasks(self, username):
        for task in database:
            if task.user == username:
                print(task)

    def edit_task(self, id):
        task = self.get_task_by_id(id)
        task.task_name = input("Task_name")
        task.is_done = True

    def delete_task(self, id):
        task = self.get_task_by_id(id)
        database.remove(task)




user_nameger = UserManager()
manager = TaskManager()
while True:
    match input("-> "):
        case "register":
            user_nameger.register()
        case "login":
            user_nameger.login(
                input("username: "),
                input("password: ")
            )
            print(main_user.username)
        case "logout":
            user_nameger.logout()
            print(main_user)
        case "profile":
            if main_user:
                print(
                    main_user.first_name,
                    main_user.last_name,
                    main_user.email,
                )
            else:
                print("You should login")
        case "tasks":
            # baroi controli taskho login shudan lozim. Vaqte ki main_user kholi naboshad
            print("test1")
            if main_user:
                while True:
                    user_input = int(input("-> "))
                    print("test2")
                    if user_input == 1:
                        manager.add_task(main_user.username)
                    elif user_input == 2:
                        task = manager.get_task_by_id(
                            int(input("Pleese enter task id: ")),
                        )
                        print(task)
                    elif user_input == 3:
                        manager.get_all_tasks(),
                        main_user.username,
                    elif user_input == 4:
                        manager.edit_task(
                            int(input("Pleese enter task id to edit: "))
                        )
                    elif user_input == 5:
                        manager.delete_task(
                            int(input("Pleese enter task id to delete: "))
                        )
                    elif user_input == 6:
                        break
                    else:
                        print("Pleese enter a number in range 1 to 6")
        case "exit":
            break


