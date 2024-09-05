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
    
    def users_last_name(self):
        
        try:
            self.last_name = input("Enter your last name: ")
            validation = re.match(r"^[A-Z][a-zA-Z]{2,}$", self.last_name)
            if not validation:
                raise ValueError("Invalid First Name")
            else:
                print("Last Name registered successfully..")
            
        except ValueError as e:
            print(e)
            print("Last name must start with a capital letter and have at least 3 characters")
    
    def users_email(self):
        
        try:
            self.email = input("Enter your Email : ")
            validation = re.match(r"^([a-z]+)\.([a-zA-Z0-9]+)@([a-z]+)\.([a-z]+)(\.[a-zA-Z0-9]+)?$", self.email)
            if not validation:
                raise ValueError("Invalid Email")
            else:
                print("Email registered successfully..")
                
        except ValueError as e:
            print(e)
            print("Email has 3 mandatory parts (abc, bl & co) and 2 optional (xyz & in) with precise @ and . positions.")
    
    def mobile_number(self):

        try:
            self.mobile_no = input("Enter your Mobile Number : ")
            validation = re.match(r"\d{1,3}\s[0-9]{10}$", self.mobile_no)
            if not validation:
                raise ValueError("Invalid Mobile Number")
            else:
                print("Mobile Number registered successfully..")
                
        except ValueError as e:
            print(e)
            print("You need to write Country code follow by space and 10 digit number")
    
    def menu(self):
        
        print("Welcome to User Registration\nEnter any option given below:")
        print("1. Enter first name ")
        print("2. Enter last name ")
        print("3. Enter Email ")
        print("4. Enter Mobile Number ")
        user_choice=int(input("Enter your choice : "))
        return user_choice

    def selection(self, choice):
        
        match choice:
            
            case 1:
                self.users_first_name()
            
            case 2:
                self.users_last_name()
            
            case 3:
                self.users_email()
                     
            case 4:
                self.mobile_number()
               
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