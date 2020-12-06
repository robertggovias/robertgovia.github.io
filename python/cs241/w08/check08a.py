class GPA:
    def __init__(self):
        self.gpa = 0
    
    def get_gpa(self):
        return self.gpa
       
    
    def get_letter(self):
        if self.gpa >= 0.0 and self.gpa < 1.0:
            return "F"
        if self.gpa >= 1.0 and self.gpa < 2.0:
            return "D"
        if self.gpa >= 2.0 and self.gpa < 3.0:
            return "C"
        if self.gpa >= 3.0 and self.gpa < 4.0:
            return "B"
        if self.gpa == 4.0:
            return "A"
    
    def set_gpa(self, value):
        if self.gpa < 0:
            self.gpa = 0
        if self.gpa >4:
            self.gpa = 4
        if self.gpa >= 0:
            self.gpa = value
        return self.gpa

    def set_letter(self, value):
        if value == "F":
            self.gpa = 0
            return self.gpa
        if value == "D":
            self.gpa = 1
            return self.gpa
        if value == "C":
            self.gpa = 2
            return self.gpa
        if value == "B":
            self.gpa = 3
            return self.gpa
        if value == "A":
            self.gpa = 4
            return self.gpa

def main():
    student = GPA()

    print("Initial values:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

    value = float(input("Enter a new GPA: "))

    student.set_gpa(value)

    print("After setting value:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

    letter = input("Enter a new letter: ")

    student.set_letter(letter)

    print("After setting letter:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

if __name__ == "__main__":
    main()