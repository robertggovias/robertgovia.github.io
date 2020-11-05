import os

os.getcwd()
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__)) # Gets the folder to the current file
my_file = os.path.join(THIS_FOLDER, 'file.txt') # Generates the absolute path to the file
os.chdir(THIS_FOLDER)
theFile = open("file.txt","r")
print(theFile.read())