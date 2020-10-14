class Student:
    def __init__(self, name="", last_name="", id=0):
        self.name = name
        self.last_nanme = last_name
        self.id = id

    def promp_student(self):
        self.name = input("Please enter your first name: ")
        self.last_name = input("Please enter your last name: ")
        self.id += 1        
    
    def display_student(self):
        print(str(self.name), str(self.last_nanme), str(self.id))
        return
y = Student("raul","paulo",8)


print(y.display_student)