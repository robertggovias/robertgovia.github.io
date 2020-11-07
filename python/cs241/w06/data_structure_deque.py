from  collections import deque

class Student:
    def __init__(self):
        self.name=""
        self.course=""

    def prompt(self):
        self.name = str(input("Enter name: "))
        self.course = str(input("Enter course: "))
    pass

    def display(self):
        print("Now helping {} with {}".format(self.name, self.course))
class HelpSystem(Student):
    def __init__(self):
        super().__init__()
        self.waiting_list = deque([])
        


    
    def is_student_waiting(self):
        if len(self.waiting_list) > 0:
            return True
        else:
            return False
    
    def add_to_waiting_list(self, Student):
        Student.prompt()
        pass
    def help_next_student(self):
        pass