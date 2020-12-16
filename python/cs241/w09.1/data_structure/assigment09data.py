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

count_Preschool = 1
count_1st_4th =1
count_5th_6th =1
count_7th_8th =1
count_9th =1
count_10th =1
count_11th =1
count_12th = 1
count_HS_grad =1
count_Some_college =1
count_Assoc_voc =1
count_Assoc_acdm =1
count_Bachelors =1
count_Prof_school =1
count_Masters =1
count_Doctorate =1

def getComm(file_lines):
    commList={}
    Preschool = " Preschool"
    v1_4 = " 1st-4th"
    v5_6 = " 5th-6th"
    v7_8 = " 7th-8th"
    v9 = " 9th"
    v_10 = " 10th"
    v_11 = " 11th"
    v_12 = " 12th"
    v_HS = " HS-grad"
    v_Sc = " Some-college"
    v_Assoc_voc = " Assoc-voc"
    v_Assoc_acdm = " Assoc-acdm"
    v_Bachelors = " Bachelors"
    v_Prof_school = " Prof-school"
    v_Masters = " Masters"
    v_Doctorate = " Doctorate"

   
 
    for items in file_lines:
        collumns= items.split(",")        
        commList[collumns[3]] = 1
        """
        if commList[collumns[3]] == Preschool:
            count_Preschool+=1
            commList[collumns[3]] = count_Preschool
        elif commList[collumns[3]] == v1_4:
            count_1st_4th +=1
            commList[collumns[3]] = count_1st_4th
        elif commList[collumns[3]] == v5_6:
            count_5th_6th +=1
            commList[collumns[3]] = count_5th_6th

        elif commList[collumns[3]] == v7_8:
            count_7th_8th +=1            
            commList[collumns[3]] = count_7th_8th

        elif commList[collumns[3]] == v9:
            count_9th +=1
            commList[collumns[3]] = count_9th

        elif commList[collumns[3]] == v_10:
            count_10th +=1
            commList[collumns[3]] = count_10th
            
        elif commList[collumns[3]] == v_11:
            count_11th +=1
            commList[collumns[3]] = count_11th

        elif commList[collumns[3]] == v_12:
            count_12th +=1
            commList[collumns[3]] = count_12th

        elif commList[collumns[3]] == v_HS:
            count_HS_grad +=1
            commList[collumns[3]] = count_HS_grad

        elif commList[collumns[3]] == v_Sc:
            count_Some_college +=1
            commList[collumns[3]] = count_Some_college

        elif commList[collumns[3]] == v_Assoc_voc:
            count_Assoc_voc +=1
            commList[collumns[3]] = count_Assoc_voc

        elif commList[collumns[3]] == v_Assoc_acdm:
            count_Assoc_acdm +=1
            commList[collumns[3]] = count_Assoc_acdm

        elif commList[collumns[3]] == v_Bachelors:
            count_Bachelors +=1
            commList[collumns[3]] = count_Bachelors

        elif commList[collumns[3]] == v_Prof_school:
            count_Prof_school +=1
            commList[collumns[3]] = count_Prof_school

        elif commList[collumns[3]] == v_Masters:
            count_Masters +=1
            commList[collumns[3]] = count_Masters

        elif commList[collumns[3]] == v_Doctorate:
            count_Doctorate +=1
            commList[collumns[3]] = count_Doctorate  
        print(commList)
        """
    return commList

def average_item(commList_): 
    addinator=0
    for commIter in commList_:
        commFloat=float(commIter)
        addinator+=commFloat
    sumin = addinator/len(commList_)
    return sumin

def print_result(lines):
    
    return 


def main():
    lines = file_lines(prompt_file())
    commList_ = getComm(lines)
    profession = input("which profesion")
    print("la cantidad de {} es: {}".format(profession,commList_[profession]))
    print(commList_[' Bachelors'])

    #print(commList_)

if __name__ == "__main__":
    main()