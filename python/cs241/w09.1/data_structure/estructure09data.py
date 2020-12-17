import os

os.getcwd()
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__)) # Gets the folder to the current file
my_file = os.path.join(THIS_FOLDER, 'file.txt') # Generates the absolute path to the file
os.chdir(THIS_FOLDER)

def prompt_file():
    file_name = input("Please enter the data file: ")
    return file_name

def file_lines(xfile):
    xfile_r=open(xfile,"r")
    lines=xfile_r.readlines()
    return lines

def getComm(file_lines):
    commList = {}
    for item in file_lines:
        collumns= item.split(",")        
        commList[collumns[3]] = commList.get(collumns[3], 0) +1                              
    return commList

def print_result(commList):
    for i in commList:
        print ("{} -- {}".format(commList[i],i))
    

def main():
    lines = file_lines(prompt_file())
    commList_ = getComm(lines)
    print_result(commList_)    

if __name__ == "__main__":
    main()