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
    commList=[]    
    for items in file_lines:
        collumns= items.split(",")   
        commList.append(collumns[6])
    comm = commList[1:len(commList)]    
    return comm

def average_item(commList_): 
    addinator=0
    for commIter in commList_:
        commFloat=float(commIter)
        addinator+=commFloat
    sumin = addinator/len(commList_)
    return sumin

def min_index(commList_):
    minimo=min(commList_)    
    min_id=commList_.index(minimo)        
    return min_id

def max_index(commList_):    
    maximo=max(commList_)    
    max_id=commList_.index(maximo)    
    return max_id

def print_result(lines, i_avg, i_maxim, i_minim):
    i_min=lines[i_minim+1].split(",")
    i_max=lines[i_maxim+1].split(",")
    print()
    print("The average commercial rate is: {}".format(i_avg))
    print()
    print("The highest rate is:")
    print("{} ({}, {}) - ${}".format(i_max[2],i_max[0],i_max[3],i_max[6]))
    print()
    print("The lowest rate is:")
    print("{} ({}, {}) - ${}".format(i_min[2],i_min[0],i_min[3],float(i_min[6])))
    return 
   
def main():
    lines = file_lines(prompt_file())
    commList_ = getComm(lines)
    return print_result(lines, average_item(commList_), max_index(commList_), min_index(commList_))
if __name__ == "__main__":
    main()