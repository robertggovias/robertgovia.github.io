import os
# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

os.getcwd()
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__)) # Gets the folder to the current file
my_file = os.path.join(THIS_FOLDER, 'file.txt') # Generates the absolute path to the file
os.chdir(THIS_FOLDER)

def prompt_file():
    file_name = input("Please enter the data file: ")
    return file_name

def file_lines(xfile):
    xfilei = xfile + ".csv"
    xfile_r=open(xfilei,"r")
    lines=xfile_r.readlines()
    return lines

def getComm(file_lines):
    commList=[]    
    for items in file_lines:
        collumns= items.split(";")   
        print("{}\n{}\n{}".format(collumns[0],collumns[1],collumns[2]))
        #commList.append(collumns[0])
        #commList.append(collumns[1])
        #commList.append(collumns[2])        
    return collumns

def main():
    t = prompt_file()
    lines = file_lines(t)
    commList_ = getComm(lines)
    print(commList_)
    
    f = t + ".srt"
    c = open(f,"w")
    c.writelines(commList_)
    print("{}\n{}\n{}\n ".format(commList_[0],commList_[1],commList_[2]))
if __name__ == "__main__":
    main()