class GPA:
    def __init__(self):
        self._gpa = 0
    
    def _get_gpa(self):
        return self._gpa
       
    @property    
    def letter(self):
        if self._gpa >= 0.0 and self._gpa < 1.0:
            return "F"
        if self._gpa >= 1.0 and self._gpa < 2.0:
            return "D"
        if self._gpa >= 2.0 and self._gpa < 3.0:
            return "C"
        if self._gpa >= 3.0 and self._gpa < 4.0:
            return "B"
        if self._gpa == 4.0:
            return "A"
    
    def _set_gpa(self, value):
        self._value = value
        if self._gpa < 0:
            self._gpa = 0
        if self._gpa >4:
            self._gpa = 4
        if self._gpa >= 0:
            self._gpa = self._value
        return self._gpa

    @letter.setter
    def letter(self, value):
        self._value = value
        if self._value == "F":
            self._gpa = 0
            return self._gpa
        if self._value == "D":
            self._gpa = 1
            return self._gpa
        if self._value == "C":
            self._gpa = 2
            return self._gpa
        if self._value == "B":
            self._gpa = 3
            return self._gpa
        if self._value == "A":
            self._gpa = 4
            return self._gpa
    
    gpa = property(_get_gpa, _set_gpa)
    #letter = property(letter, letter)

def main():
    student = GPA()

    print("Initial values:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

    value = float(input("Enter a new GPA: "))

    student.gpa = value

    print("After setting value:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

    letter = input("Enter a new letter: ")

    student.letter = letter

    print("After setting letter:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

if __name__ == "__main__":
    main()