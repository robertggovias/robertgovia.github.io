#todavia no funciona porque no he logrado crear el miembro nombre de la clase.
class InvalidStudentError(Exception):
    def __init__(self,message):
        # No te olvides de pasar el mensafe a la clase base
        super().__init__(message)


class Student:
    def __init__(self):
        self.name = ""
    def inputing(self):
         self.name=input("student name: ")


student = Student()
student.inputing()
if student.name == None:
    raise InvalidStudentError("The student must have a name")

