from collections import deque

class Song:
    def __init__(self):
        self.title = "title"
        self.artist = "artist"
    
    def get_title(self):
        return self.title
    def get_artist(self):
        return self.artist

    
    def prompt(self):
        self.title = str(input("Enter the title: "))
        e = self.title
        return e
    def prompta(self):
        self.artist = str(input("Enter the artist: "))
        p = self.artist
        return p
    
    def display(self):
        print("PLaying the song:\n{} by {}".format(self.title,self.artist))

    
'''
print("test")
newsong=Song()
Song.prompt(newsong)
print(Song.prompt(newsong))
hola=Song.get_artist(newsong)
perro=Song.get_title(newsong)
print(Song.get_artist(newsong))
print(hola,perro)
hola=Song.prompt(newsong)
perro=Song.prompta(newsong)
print(hola,perro)'''


def main():
    newsongs=Song()    
    songs = deque()    
    question = "1. Add new song to the end of the playlist.\n2. Insert a new song at the beginning of the playlist.\n3. Play the next song.\n"
    print(question)
    selected = int(input("Enter selection: "))        
    while selected < 4 and selected > 0:
        if selected == 1:
            Song.prompt(newsongs)
            Song.prompta(newsongs)
            songs.append([Song.get_title(newsongs),(Song.get_artist(newsongs))])
            print(question)
            selected = int(input("Enter selection: "))        
        elif selected == 2:
            Song.prompt(newsongs)
            Song.prompta(newsongs)
            songs.appendleft([Song.get_title(newsongs),(Song.get_artist(newsongs))])
            print(question)
            selected = int(input("Enter selection: "))        
        elif selected == 3:
            if len(songs) > 0:                            
                Song.display(newsongs) 
                songs.pop()
                print(question)
                selected = int(input("Enter selection: "))     
            else:
                print("The playlist is currently empty.")
                print(question)
                selected = int(input("Enter selection: "))     
        else:
            print("wrong answer")
    print("Good Bye")
    print(songs)
    
if __name__ == "__main__":
    main()