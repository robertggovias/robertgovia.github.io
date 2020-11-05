class Book:
    def __init__(self):
        self.title = ""
        self.author = ""
        self.year = 0
    
    def prompt_book_info(self):
        self.title = str(input("Title: "))
        self.author = str(input("Author: "))
        self.year = int(input("Publication Year: "))
    
    def display_book_info(self):
        print("\n{} ({}) by {}".format(self.title,self.year,self.author))
    
class TextBook(Book):
    def __init__(self):

        super().__init__()
        self.subject = ""
    
    def prompt_subject(self):        
        Book.prompt_book_info(self)
        self.subject = str(input("Subject: "))

    def display_subject(self):
        Book.display_book_info(self)
        print("Subject: {}".format(self.subject))

class PictureBook(Book):
    def __init__(self):

        super().__init__()
        self.illustrator = ""

    def prompt_illustrator(self):
        Book.prompt_book_info(self)
        self.illustrator = str(input("Illustrator: "))

    def display_illustrator(self):
        Book.display_book_info(self)
        print("Illustrated by {}".format(self.illustrator))



def main():
    main = Book()
    main.prompt_book_info()
    main.display_book_info()
    print()

    main_text = TextBook()    
    main_text.prompt_subject()
    main_text.display_subject()

    print()
    main_illustrator = PictureBook()
    main_illustrator.prompt_illustrator()
    main_illustrator.display_illustrator()

if __name__ == "__main__":
    main()