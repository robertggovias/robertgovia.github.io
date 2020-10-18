from collections import deque

class Song:
    def __init__(self):
        self.title = "unknow"
        self.artist = "no one"
    
    def prompt(self):
        self.title = str(input("Enter the title: "))
        self.artist = str(input("Enter the artist: "))
    
    def display(self):
        print("PLaying the songn:\n{} by {}".format(self.title,self.artist))

songs = deque()

def main():
    adnew = songs.append(Song.prompt())

if __name__ == "__main__":
    main()
