class Student:
    def __init__(self, first_name, last_name, id):
        self.f_name = first_name
        self.l_name = last_name
        self.i_d = id
    '''def gfirst_name (self):
        return self.f_name
    def glast_name (self):
        return self.l_name
    def gid (self):
        return self.i_d'''

    '''def prompt_student(self):
        self.f_name = input("Please enter your first name: ")

    def display_student(self):
        return "\nYour information:\n" + str(self.i_d) + " - " + str(self.f_name)+ " " + str(self.l_name)
    

inicio = Student("","",0)
def prompt_student():
    user = Student(input("Please enter your first name: "),input("Please enter your last name: "),input("Please enter your id: "))
    return Student.display_student(user)

print(prompt_student())