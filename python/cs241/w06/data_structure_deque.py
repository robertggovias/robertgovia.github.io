from  collections import deque

class Student:
    def __init__(self):
        self.name=""
        self.course=""

    def prompt(self):
        self.name = str(input("Enter name: "))
        self.course = str(input("Enter course: "))
        return self.name, self.course    

    def display(self):
        return "Now helping {} with {}".format(self.name, self.course)

class HelpSystem(Student):
    def __init__(self):
        super().__init__()
        self.waiting_list = deque([])
    
    def is_student_waiting(self):
        if len(self.waiting_list) > 0:
            return True
        else:
            return False
    
    def add_to_waiting_list(self,Student):
        Student = self.prompt()
        self.waiting_list.append(self.display())
            
    def help_next_student(self):
        if  self.is_student_waiting() == True:
            x=self.waiting_list.popleft()            
            print(x)
        else:
            print("No one to help")
        
def question():
    first = "1. Add a new student"
    second = "2. Help next student"
    third = "3. Quit"
    print("Options:\n{}\n{}\n{}".format(first,second,third))    

def main():
    he=HelpSystem()
    question()
    option = int(input("Enter selection: "))
    
    while option != 3:
        if option == 1:
            print()          
            he.add_to_waiting_list(Student)
            print()        
            question()
            option = int(input("Enter selection: "))
            
        elif option == 2:            
            he.help_next_student()
            print()
            question()
            option = int(input("Enter selection: "))
            print()
        else:
            print("answer must be 1, 2 or 3")
            question()
            option = int(input("Enter selection: "))
            print()
    #he.display()
    
if __name__ == "__main__":
    main()