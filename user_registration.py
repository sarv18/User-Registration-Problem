import re

class UserRegistration:
    
    def __init__(self):
        
        self.first_name = None
        self.last_name = None
        self.email = None
        self.mobile_no = None
        self.password = None

    def users_first_name(self, first_name):
        
        #try:
            self.first_name = first_name
            validation = re.match(r"^[A-Z][a-zA-Z]{2,}$", first_name)
            if not validation:
                return False
            else:
                print("First Name registered successfully..")
                return True
            
        # except ValueError as e:
        #     print(e)
        #     print("First name must start with a capital letter and have at least 3 characters")
    
    def users_last_name(self, last_name):
        
        #try:
            self.last_name = last_name
            validation = re.match(r"^[A-Z][a-zA-Z]{2,}$", self.last_name)
            if not validation:
                return False
            else:
                print("Last Name registered successfully..")
                return True
            
        # except ValueError as e:
        #     print(e)
        #     print("Last name must start with a capital letter and have at least 3 characters")
    
    def users_email(self, email):
        
        # try:
            self.email = email
            validation = re.match(r"^([a-z]+)\.([a-zA-Z0-9]+)@([a-z]+)\.([a-z]+)(\.[a-zA-Z0-9]+)?$", self.email)
            if not validation:
                return False
            else:
                print("Email registered successfully..")
                return True
                
        # except ValueError as e:
        #     print(e)
        #     print("Email has 3 mandatory parts (abc, bl & co) and 2 optional (xyz & in) with precise @ and . positions.")
    
    def mobile_number(self, mobile_no):

        # try:
            self.mobile_no = mobile_no
            validation = re.match(r"\d{1,3}\s[0-9]{10}$", self.mobile_no)
            if not validation:
                return False
            else:
                print("Mobile Number registered successfully..")
                return True
                
        # except ValueError as e:
        #     print(e)
        #     print("You need to write Country code follow by space and 10 digit number")
    
    def password_rules(self, password):
        
        # try:
            self.password = password
            validation= re.match(r"^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()-_+=]{1}).{8,}$", self.password)
            if not validation:
                return False
            else:
                print("Password registered successfully..")
                return True

        # except ValueError as e:
        #     print(e)
        #     print("You need to enter minimum 8 characters and atleast one upper case and atleast one digit and exact one special character.")

    
    def menu(self):
        
        print("Welcome to User Registration\nEnter any option given below:")
        print("1. Enter first name ")
        print("2. Enter last name ")
        print("3. Enter Email ")
        print("4. Enter Mobile Number ")
        print("5. Enter Password ")
        user_choice=int(input("Enter your choice : "))
        return user_choice

    def selection(self, choice):
        
            if choice == 1:
                first_name = input("Enter your first name: ")
                self.users_first_name(first_name)
            
            elif choice == 2:
                last_name = input("Enter your last name: ")
                self.users_last_name(last_name)
            
            elif choice == 3:
                email = input("Enter your Email : ")
                self.users_email(email)
                     
            elif choice == 4:
                mobile_no = input("Enter your Mobile Number : ")
                self.mobile_number(mobile_no)
               
            elif choice ==5:
                password = input("Enter your password : ")
                self.password_rules(password)
               
            else:
                print("Invalid choice..")
                

if __name__ == "__main__":
    
    user_registration_obj = UserRegistration()
    
    while True:
        choice = user_registration_obj.menu()
        user_registration_obj.selection(choice)

        exit = input("Do you want to exit ( yes / no ): ")
        if exit == 'yes':
            print("User Registration exited, Good Bye..")
            break