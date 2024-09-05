import re

class UserRegistration:
    
    def __init__(self):
        
        self.first_name = None

    def users_first_name(self):
        
        try:
            self.first_name = input("Enter your first name: ")
            validation = re.match(r"^[A-Z][a-zA-Z]{2,}$", self.first_name)
            if not validation:
                raise ValueError("Invalid First Name")
            else:
                print("First Name registered successfully..")
            
        except ValueError as e:
            print(e)
            print("First name must start with a capital letter and have at least 3 characters")
    
    def menu(self):
        
        print("Welcome to User Registration\nEnter any option given below:")
        print("1. Enter first name : ")
        user_choice=int(input("Enter your choice : "))
        return user_choice



    def selection(self, choice):
        
        match choice:
            case 1:
                self.users_first_name()
            case _:
                print("Invalid choice..")
                
def main():
    user_registration_obj = UserRegistration()
    
    while True:
        choice = user_registration_obj.menu()
        user_registration_obj.selection(choice)

        exit = input("Do you want to exit ( yes / no ): ")
        if exit == 'yes':
            print("User Registration exited, Good Bye..")
            break

if __name__ == "__main__":
    main()