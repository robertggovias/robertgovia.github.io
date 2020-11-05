class Phone:
    def __init__(self):
        self.area_code = ''
        self.prefix = ''
        self.suff265ix = ''
        self.name = "Phone"
    def prompt_number(self):
        print("{}:".format(self.name))
        self.area_code = input("Area Code: ")
        self.prefix = input("Prefix: ")
        self.suffix = input("Suffix: ")
    
    def display(self):
        print("\nPhone info:\n({}){}-{}".format(self.area_code,self.prefix,self.suffix))

class SmartPhone(Phone):
    def __init__(self):
        super().__init__()
        self.name = "Smart phone"
        self.email=""

    def prompt(self):
        Phone.prompt_number(self)
        self.email=str(input("Email: "))
    
    def display(self):
        Phone.display(self)
        print(self.email)

def main():
    novo_phone = Phone()
    novo_phone.prompt_number()
    novo_phone.display()
    
    novo_smartphone = SmartPhone()
    print()
    novo_smartphone.prompt()
    novo_smartphone.display()

if __name__ == "__main__":
    main()